"""The approval gate: nothing is sent unless the exact text was approved."""
import os
import unittest
from unittest import mock

from lib import backend_selector, publish, text_digest, render_approval_card
from lib.approval import ApprovalError, check_approved
from lib.threads_rules import ThreadsRuleError

TEXT = "Un post prêt à partir.\n\nSans hashtag ni lien."
URL = "https://www.threads.com/"


class FakePublora:
    """Stands in for PubloraClient: records what would have been sent."""

    created = []
    managed = ["threads-1"]

    def __init__(self, *args, **kwargs):
        pass

    def list_connections(self):
        return [{"platformId": p, "username": "demo"} for p in type(self).managed]

    def create_post(self, **kwargs):
        type(self).created.append(kwargs)
        return {"success": True, "postGroupId": "grp-1"}


class DigestTests(unittest.TestCase):
    def test_digest_is_short_and_stable(self):
        self.assertEqual(len(text_digest(TEXT)), 12)
        self.assertEqual(text_digest(TEXT), text_digest(TEXT))

    def test_digest_ignores_trailing_spaces_and_newline_style(self):
        self.assertEqual(text_digest("a\nb"), text_digest("a  \r\nb \n"))

    def test_any_word_change_changes_the_digest(self):
        self.assertNotEqual(text_digest("Bonjour"), text_digest("Bonsoir"))

    def test_check_approved_needs_a_digest(self):
        with self.assertRaises(ApprovalError):
            check_approved(TEXT, None)

    def test_check_approved_rejects_a_changed_text(self):
        digest = text_digest(TEXT)
        check_approved(TEXT, digest)
        with self.assertRaises(ApprovalError):
            check_approved(TEXT + " Modifié.", digest)

    def test_card_shows_the_digest_the_account_and_the_three_actions(self):
        card = render_approval_card(kind="post", preview_text=TEXT, account="@demo",
                                    key_source="~/.needythreads/.env")
        self.assertIn(text_digest(TEXT), card)
        self.assertIn("@demo", card)
        for word in ("brouillon", "programme", "publie maintenant"):
            self.assertIn(word, card)
        self.assertIn("ne créent rien", card)

    def test_card_says_when_the_account_is_not_verified(self):
        card = render_approval_card(kind="post", preview_text=TEXT)
        self.assertIn("non vérifié", card)


class PublishGateTests(unittest.TestCase):
    def setUp(self):
        FakePublora.created = []
        FakePublora.managed = ["threads-1"]
        env = mock.patch.dict(os.environ, {"PUBLORA_API_KEY": "sk_test", "THREADS_PLATFORM_ID": "threads-1"})
        env.start()
        self.addCleanup(env.stop)
        for target in ("lib.publora_client.PubloraClient",):
            patcher = mock.patch(target, FakePublora)
            patcher.start()
            self.addCleanup(patcher.stop)

    def send(self, text=TEXT, **kwargs):
        return publish("post", text, URL, **kwargs)

    def test_no_fingerprint_sends_nothing(self):
        with self.assertRaises(ApprovalError):
            self.send()
        self.assertEqual(FakePublora.created, [])

    def test_text_changed_after_approval_sends_nothing(self):
        digest = text_digest(TEXT)
        with self.assertRaises(ApprovalError):
            self.send(text=TEXT + " Ajout.", approved_digest=digest)
        self.assertEqual(FakePublora.created, [])

    def test_approved_text_becomes_a_draft_by_default(self):
        result = self.send(approved_digest=text_digest(TEXT))
        self.assertEqual(result["action"], "draft")
        self.assertEqual(len(FakePublora.created), 1)
        self.assertIsNone(FakePublora.created[0]["scheduled_time"])

    def test_going_public_needs_its_own_confirmation(self):
        digest = text_digest(TEXT)
        with self.assertRaises(ApprovalError):
            self.send(approved_digest=digest, action="now")
        with self.assertRaises(ApprovalError):
            self.send(approved_digest=digest, action="schedule", scheduled_time="2030-01-01T10:00:00Z")
        self.assertEqual(FakePublora.created, [])

    def test_publish_now_sets_a_time_when_confirmed(self):
        self.send(approved_digest=text_digest(TEXT), action="now", confirm_public=True)
        self.assertTrue(FakePublora.created[0]["scheduled_time"].endswith("Z"))

    def test_schedule_keeps_the_requested_time(self):
        self.send(approved_digest=text_digest(TEXT), action="schedule", confirm_public=True,
                  scheduled_time="2030-01-01T10:00:00Z")
        self.assertEqual(FakePublora.created[0]["scheduled_time"], "2030-01-01T10:00:00Z")

    def test_schedule_without_a_time_and_draft_with_a_time_are_refused(self):
        digest = text_digest(TEXT)
        with self.assertRaises(ValueError):
            self.send(approved_digest=digest, action="schedule", confirm_public=True)
        with self.assertRaises(ValueError):
            self.send(approved_digest=digest, action="draft", scheduled_time="2030-01-01T10:00:00Z")
        with self.assertRaises(ValueError):
            self.send(approved_digest=digest, action="publish")
        self.assertEqual(FakePublora.created, [])

    def test_a_key_that_does_not_manage_the_platform_sends_nothing(self):
        FakePublora.managed = ["threads-777"]
        with self.assertRaises(ApprovalError):
            self.send(approved_digest=text_digest(TEXT))
        self.assertEqual(FakePublora.created, [])

    def test_a_draft_over_the_limit_sends_nothing(self):
        text = "a" * 501
        with self.assertRaises(ThreadsRuleError):
            self.send(text=text, approved_digest=text_digest(text))
        self.assertEqual(FakePublora.created, [])

    def test_replies_stay_manual_even_with_publora_configured(self):
        result = publish("reply", TEXT, "https://www.threads.com/@x/post/1")
        self.assertEqual(result["mode"], "manual")
        self.assertEqual(FakePublora.created, [])

    def test_target_account_reads_the_name_from_publora(self):
        self.assertEqual(backend_selector.target_account(), "@demo")
        FakePublora.managed = ["threads-777"]
        self.assertIsNone(backend_selector.target_account())


class ManualModeTests(unittest.TestCase):
    def test_without_credentials_nothing_is_sent_and_no_fingerprint_is_needed(self):
        clean = {k: v for k, v in os.environ.items()
                 if k not in ("PUBLORA_API_KEY", "THREADS_PLATFORM_ID", "THREADS_SKILLS_CUSTOM_POSTER")}
        with mock.patch.dict(os.environ, clean, clear=True):
            result = publish("post", TEXT, URL)
        self.assertEqual(result["mode"], "manual")


if __name__ == "__main__":
    unittest.main()
