"""Mechanical checks for the Threads rules a draft must respect.

The skills describe these rules in prose, and a prose rule is a request, not a
guarantee. This module checks what code can check, so the approval card shows
the result and `publish()` refuses a draft that breaks a hard limit.

Hard limits (error): a post over 500 characters, more than one hashtag in a
post, an empty draft. Style signals (warn): more than one em dash, a link in the
first post, more than two emoji, a single post under 300 characters (the room is
there to use: 350 to 500 is the target).
"""
from __future__ import annotations

import re
from dataclasses import dataclass

MAX_POST_CHARS = 500
MAX_HASHTAGS = 1
MAX_EM_DASHES = 1
MAX_EMOJI = 2
MIN_SINGLE_POST_CHARS = 300

_HASHTAG = re.compile(r"(?<!\w)#\w+", re.UNICODE)
_URL = re.compile(r"https?://\S+|www\.\S+", re.IGNORECASE)
_EMOJI = re.compile(
    "[\U0001F300-\U0001FAFF\U00002600-\U000027BF\U0001F000-\U0001F2FF\U00002B00-\U00002BFF]"
)
_SEPARATOR = re.compile(r"^\s*---\s*$", re.MULTILINE)
_EM_DASH = "—"


class ThreadsRuleError(ValueError):
    """A draft breaks a hard Threads limit and was not sent."""


@dataclass(frozen=True)
class Issue:
    severity: str  # "error" | "warn"
    code: str
    post: int  # 1-based post number
    message: str


def split_posts(text: str) -> list[str]:
    """Split a thread on lines that are exactly `---`. A text with none is one post."""
    parts = [p.strip() for p in _SEPARATOR.split(text.replace("\r\n", "\n"))]
    parts = [p for p in parts if p]
    return parts or [text.strip()]


def check_draft(text: str, kind: str = "post") -> list[Issue]:
    """Return every rule a draft breaks. An empty list means it passes."""
    if not text or not text.strip():
        return [Issue("error", "empty", 1, "Le brouillon est vide.")]

    issues: list[Issue] = []
    hand_split = bool(_SEPARATOR.search(text))
    posts = split_posts(text)
    check_length = True

    if kind == "thread" and not hand_split and len(text.strip()) > MAX_POST_CHARS:
        issues.append(Issue(
            "warn", "auto_split", 1,
            "Aucun séparateur `---` : Publora découpera le texte lui-même. "
            "Place les coupures toi-même pour garder le contrôle.",
        ))
        posts = [text.strip()]
        check_length = False

    for number, post in enumerate(posts, start=1):
        if check_length and len(post) > MAX_POST_CHARS:
            issues.append(Issue(
                "error", "too_long", number,
                f"{len(post)} caractères, la limite est {MAX_POST_CHARS}.",
            ))
        tags = _HASHTAG.findall(post)
        if len(tags) > MAX_HASHTAGS:
            issues.append(Issue(
                "error", "hashtags", number,
                f"{len(tags)} hashtags ({', '.join(tags)}) : Threads n'en accepte qu'un par post.",
            ))
        dashes = post.count(_EM_DASH)
        if dashes > MAX_EM_DASHES:
            issues.append(Issue(
                "warn", "em_dash", number,
                f"{dashes} tirets cadratins : un seul par post au maximum.",
            ))
        emoji = _EMOJI.findall(post)
        if len(emoji) > MAX_EMOJI:
            issues.append(Issue(
                "warn", "emoji", number,
                f"{len(emoji)} emoji : deux au maximum, et seulement s'ils servent.",
            ))
        if kind == "post" and len(posts) == 1 and len(post) < MIN_SINGLE_POST_CHARS:
            issues.append(Issue(
                "warn", "short_post", 1,
                f"{len(post)} caractères : il reste de la place (cible 350 à 500). "
                "Ajoute un détail vécu de ta banque d'histoires, ou dis-moi lequel ajouter ; "
                "je n'invente rien pour remplir.",
            ))
        if number == 1 and _URL.search(post):
            issues.append(Issue(
                "warn", "link_in_first_post", 1,
                "Un lien dans le premier post : place-le dans une réponse.",
            ))
    return issues


def errors(issues: list[Issue]) -> list[Issue]:
    """Only the hard-limit issues."""
    return [i for i in issues if i.severity == "error"]


def format_report(issues: list[Issue]) -> str:
    """One line per issue, errors first. An empty list gives a short pass line."""
    if not issues:
        return "Contrôles : aucun problème détecté."
    ordered = sorted(issues, key=lambda i: (i.severity != "error", i.post))
    return "\n".join(
        f"- {'ERREUR' if i.severity == 'error' else 'à vérifier'} (post {i.post}) : {i.message}"
        for i in ordered
    )
