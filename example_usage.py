"""
example_usage.py -- Demonstrates MarketingEmailSpamPreventClient
"""
from client import MarketingEmailSpamPreventClient

def main():
    client = MarketingEmailSpamPreventClient()
    result = client.analyze_copy(
        email_subject="Winner! Get free cash today",
        email_body="Earn cash fast. Buy now to secure your 100% free promo gift."
    )
    print("[Email Deliverability Result]")
    print(f"Spam Score: {result['spam_score']}/100")
    print(f"Triggers: {result['trigger_words_detected']}")

if __name__ == "__main__":
    main()
