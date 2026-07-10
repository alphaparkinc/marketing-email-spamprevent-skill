"""
marketing-email-spamprevent-skill: Client SDK
Flags spam trigger words inside marketing newsletters to ensure inbox delivery rates.
"""
from __future__ import annotations
from typing import Optional

SPAM_KEYWORDS = ["buy now", "free cash", "guaranteed click", "100% free", "make money", "winner", "earn cash"]


class MarketingEmailSpamPreventClient:
    """
    SDK for email delivery compliance testing.
    """

    def analyze_copy(
        self,
        email_subject: str,
        email_body: str,
    ) -> dict:
        content = (email_subject + " " + email_body).lower()
        detected = []

        for kw in SPAM_KEYWORDS:
            if kw in content:
                detected.append(kw)

        score = len(detected) * 20
        risk_score = min(100, score)

        return {
            "spam_score": risk_score,
            "trigger_words_detected": detected,
            "recommendation": "Rewrite flagged zones to bypass automated spam rules." if risk_score > 30 else "Safe to broadcast."
        }
