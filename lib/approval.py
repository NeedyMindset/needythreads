"""Approval gate helpers.

Every skill that posts to Threads MUST present a draft to the user and wait for
explicit approval before calling Publora. The card built here carries a
fingerprint of the exact text shown. `publish()` refuses to send to Publora
unless it receives that fingerprint and the text still matches it, so a draft
edited after the user approved it cannot go out under the old approval.

This is a guard against mistakes, not against a determined caller: code cannot
prove what a human said. The wording of the skills still decides when to ask.
"""
from __future__ import annotations

import hashlib
from typing import Optional

from .threads_rules import check_draft, format_report

#: What the user can answer to a card, and what each answer does.
ACTIONS = ("draft", "schedule", "now")


class ApprovalError(Exception):
    """The text was not approved, or changed after it was approved."""


def normalize_text(text: str) -> str:
    """Trim trailing spaces per line and the ends of the text, unify newlines."""
    unified = text.replace("\r\n", "\n").replace("\r", "\n")
    return "\n".join(line.rstrip() for line in unified.strip().split("\n"))


def text_digest(text: str) -> str:
    """Short fingerprint of the draft the user reads. 12 hex characters."""
    return hashlib.sha256(normalize_text(text).encode("utf-8")).hexdigest()[:12]


def check_approved(text: str, approved_digest: Optional[str]) -> None:
    """Raise ApprovalError unless `approved_digest` matches `text` exactly."""
    if not approved_digest:
        raise ApprovalError(
            "Aucune empreinte d'approbation : montre d'abord la carte de validation "
            "(render_approval_card) et attends la réponse de l'utilisateur."
        )
    if approved_digest != text_digest(text):
        raise ApprovalError(
            "Le texte a changé depuis la validation (empreinte différente) : "
            "reconstruis la carte et fais valider la nouvelle version."
        )


def render_approval_card(
    *,
    kind: str,  # "post" | "thread" | "reply" | "quote"
    preview_text: str,
    target_url: Optional[str] = None,
    char_count: Optional[int] = None,
    post_count: Optional[int] = None,
    extra_context: Optional[dict] = None,
    account: Optional[str] = None,
    key_source: Optional[str] = None,
    warnings: Optional[list] = None,
    lang: str = "fr",
) -> str:
    """Format the card the user reads before anything is created or sent.

    The card contains: what the action is, the full text, the character count
    (and post count for a thread), the mechanical Threads checks, the account the
    key will publish to, where the key was read from, the fingerprint of the
    text, and the exact answers the user can give.

    `account` comes from `lib.target_account()`; `key_source` from
    `lib._env.env_source("PUBLORA_API_KEY")`; `warnings` from
    `lib._env.ignored_credentials()` formatted by the caller.
    """
    en = lang == "en"
    if char_count is None:
        char_count = len(preview_text)
    lines = [("## Draft to approve: " if en else "## Brouillon à valider : ") + kind, ""]

    if target_url:
        lines.append(("**Target:** " if en else "**Cible :** ") + target_url)
    lines.append(("**Account:** " if en else "**Compte cible :** ")
                 + (account or ("not verified" if en else "non vérifié")))
    if key_source:
        lines.append(("**Key read from:** " if en else "**Clé lue dans :** ") + key_source)
    lines.append(("**Text fingerprint:** " if en else "**Empreinte du texte :** ")
                 + f"`{text_digest(preview_text)}`")
    lines.append(("**Characters:** " if en else "**Caractères :** ") + str(char_count))
    if post_count is not None:
        lines.append(("**Posts:** " if en else "**Posts :** ") + str(post_count))
    lines.append("")
    lines.append("**Preview:**" if en else "**Aperçu :**")
    lines.append("")
    for pl in preview_text.splitlines() or [""]:
        lines.append(f"> {pl}")
    lines.append("")
    lines.append(format_report(check_draft(preview_text, kind)))
    lines.append("")
    if warnings:
        lines.append("**Warnings:**" if en else "**Avertissements :**")
        for w in warnings:
            lines.append(f"- {w}")
        lines.append("")
    if extra_context:
        lines.append("**Context:**" if en else "**Contexte :**")
        for k, v in extra_context.items():
            lines.append(f"- **{k}**: {v}")
        lines.append("")

    if en:
        lines += [
            "You can answer:",
            "- **draft**: create a draft in Publora (nothing becomes public).",
            "- **schedule <day and time>**: schedule the post.",
            "- **publish now**: publish right away.",
            "- **copy-paste**: I give you the text and you post it yourself.",
            "- or tell me what to change.",
            "\"yes\" or \"ok\" only approve the text: they create nothing.",
        ]
    else:
        lines += [
            "Ce que tu peux répondre :",
            "- **brouillon** : crée un brouillon dans Publora (rien n'est public).",
            "- **programme <jour et heure>** : programme la publication.",
            "- **publie maintenant** : publie tout de suite.",
            "- **copier-coller** : je te donne le texte et tu publies toi-même.",
            "- ou dis-moi ce qu'il faut changer.",
            "« oui » ou « ok » valident seulement le texte : ils ne créent rien.",
        ]
    return "\n".join(lines)
