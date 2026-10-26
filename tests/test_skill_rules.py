"""The written rules that decide what an assistant does on its own.

Prose is not a guarantee, but a rule that disappears from a skill is a
regression we can catch. These checks fail when a consent, approval or
no-inference rule is edited out.
"""
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def text(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


class TemplateTests(unittest.TestCase):
    def test_shipped_templates_are_blank(self):
        for name in ("references/voice-profile.md", "references/story-bank.md"):
            body = text(name)
            self.assertRegex(body, r"(?m)^- filled: no\s*$", name)
            self.assertNotRegex(body, r"(?mi)^\s*-\s*filled:\s*yes", name)

    def test_templates_explain_the_three_statuses(self):
        for name in ("references/voice-profile.md", "references/story-bank.md"):
            body = text(name)
            for status in ("`[confirmé]`", "`[à confirmer]`", "`[interdit]`"):
                self.assertIn(status, body, f"{name} lacks {status}")

    def test_voice_profile_asks_for_one_signature_and_never_invents_a_link(self):
        body = text("references/voice-profile.md")
        self.assertIn("Signature (une seule phrase", body)
        self.assertIn("un lien n'est jamais inventé", body)


class ConsentTests(unittest.TestCase):
    def setUp(self):
        self.writer = text("skills/threads-post-writer/SKILL.md")

    def test_saving_the_profile_is_a_separate_confirmed_step(self):
        self.assertIn("Saving the profile is a separate step, never a side effect", self.writer)
        self.assertIn("is not a yes", self.writer)
        self.assertIn("second clear yes", self.writer)
        self.assertIn("show the full content of both files", self.writer)

    def test_the_old_save_on_yes_rule_is_gone(self):
        self.assertNotIn("If the user says yes and you can write files", self.writer)

    def test_nothing_is_inferred_into_the_profile(self):
        self.assertIn("Do not infer anything they did not write", self.writer)
        self.assertIn("`[à confirmer]`", self.writer)
        self.assertIn("ask which one applies; never choose", self.writer)

    def test_interview_shows_the_bank_before_writing_it(self):
        body = text("skills/threads-humanizer/sub-skills/story-bank-interview.md")
        self.assertIn("write the file only after a clear yes", body)

    def test_profile_from_posts_never_infers_the_network(self):
        body = text("skills/threads-humanizer/sub-skills/voice-profile.md")
        self.assertIn("Never infer the social network", body)


class PublicationTests(unittest.TestCase):
    def test_every_skill_that_publishes_a_post_passes_the_fingerprint(self):
        # A reply or a quote only returns a copy-paste block: nothing is sent.
        for path in sorted((ROOT / "skills").glob("*/SKILL.md")):
            body = path.read_text(encoding="utf-8")
            if 'lib.publish(kind="post"' in body:
                self.assertIn("approved_digest", body, f"{path.name} publishes without a fingerprint")
                self.assertIn("confirm_public", body, f"{path.name} lacks the public-action confirmation")

    def test_a_draft_needs_the_word_brouillon(self):
        for name in ("skills/threads-post-writer/SKILL.md", "skills/threads-repurposer/SKILL.md"):
            self.assertIn("brouillon", text(name), name)

    def test_a_plain_yes_never_publishes(self):
        root = text("SKILL.md")
        self.assertIn('"yes" approves the wording only', root)
        self.assertNotIn("auto-publishes on approval", root)
        self.assertNotIn("Only after explicit approval does the skill call Publora to publish", root)

    def test_voice_rules_keep_facts_in_the_users_words(self):
        rules = text("references/voice-rules.md")
        self.assertRegex(rules, r"Their facts, in their words")
        self.assertRegex(rules, r"Never guess who the user is")

    def test_skill_descriptions_have_no_dashes(self):
        for path in [ROOT / "SKILL.md", *sorted((ROOT / "skills").glob("*/SKILL.md"))]:
            for line in path.read_text(encoding="utf-8").splitlines():
                if line.startswith("description:"):
                    self.assertFalse(re.search("[–—]", line), f"dash in {path.name}")


if __name__ == "__main__":
    unittest.main()
