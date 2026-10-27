"""The Threads rules that code can check, checked by code."""
import unittest

from lib.threads_rules import check_draft, errors, format_report, split_posts


PAD = "a" * 320  # a single post under 300 characters gets a length warning


def codes(issues):
    return sorted(i.code for i in issues)


class ThreadsRulesTests(unittest.TestCase):
    def test_clean_post_passes(self):
        self.assertEqual(check_draft(PAD), [])

    def test_empty_draft_is_an_error(self):
        self.assertEqual(codes(check_draft("   ")), ["empty"])
        self.assertTrue(errors(check_draft("")))

    def test_post_over_500_characters_is_an_error(self):
        issues = check_draft("a" * 501)
        self.assertEqual(codes(errors(issues)), ["too_long"])

    def test_exactly_500_characters_passes(self):
        self.assertEqual(check_draft("a" * 500), [])

    def test_two_hashtags_in_one_post_is_an_error(self):
        self.assertEqual(codes(errors(check_draft(PAD + " #un #deux"))), ["hashtags"])

    def test_one_hashtag_is_fine(self):
        self.assertEqual(check_draft(PAD + " #un"), [])

    def test_two_em_dashes_is_only_a_warning(self):
        issues = check_draft("Un — deux — trois " + PAD)
        self.assertEqual(codes(issues), ["em_dash"])
        self.assertEqual(errors(issues), [])

    def test_three_emoji_is_only_a_warning(self):
        issues = check_draft("Allez \U0001F3F9\U0001F3AF\U0001F680 " + PAD)
        self.assertEqual(codes(issues), ["emoji"])

    def test_link_in_first_post_is_a_warning_not_in_later_posts(self):
        first = check_draft("Voir https://exemple.fr\n---\nSuite", kind="thread")
        self.assertEqual(codes(first), ["link_in_first_post"])
        later = check_draft("Début\n---\nVoir https://exemple.fr", kind="thread")
        self.assertEqual(later, [])

    def test_thread_is_checked_post_by_post(self):
        text = "a" * 400 + "\n---\n" + "b" * 600
        issues = errors(check_draft(text, kind="thread"))
        self.assertEqual([(i.code, i.post) for i in issues], [("too_long", 2)])

    def test_long_thread_without_separators_is_a_warning(self):
        text = ("Une phrase. " * 80).strip()
        issues = check_draft(text, kind="thread")
        self.assertEqual(codes(issues), ["auto_split"])
        self.assertEqual(errors(issues), [])

    def test_short_single_post_gets_a_length_warning(self):
        issues = check_draft("Un post court, sans artifice.")
        self.assertEqual(codes(issues), ["short_post"])
        self.assertEqual(errors(issues), [])

    def test_length_warning_stops_at_300_characters(self):
        self.assertEqual(codes(check_draft("a" * 299)), ["short_post"])
        self.assertEqual(check_draft("a" * 300), [])

    def test_threads_and_replies_are_not_asked_to_be_longer(self):
        self.assertEqual(check_draft("Court\n---\nCourt aussi", kind="thread"), [])
        self.assertEqual(check_draft("Une réponse courte", kind="reply"), [])

    def test_split_posts_ignores_blank_parts(self):
        self.assertEqual(split_posts("a\n---\n\n---\nb"), ["a", "b"])

    def test_report_lists_errors_first(self):
        text = "a" * 501 + " #x #y"
        report = format_report(check_draft(text))
        self.assertTrue(report.splitlines()[0].startswith("- ERREUR"))
        self.assertEqual(format_report([]), "Contrôles : aucun problème détecté.")


if __name__ == "__main__":
    unittest.main()
