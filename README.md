# genpark-marketing-email-spamprevent-skill

> **GenPark AI Agent Skill** -- Email spam trigger words compiler and score evaluator.

## Quick Start

```python
from client import MarketingEmailSpamPreventClient
client = MarketingEmailSpamPreventClient()
res = client.analyze_copy("Special Promotion", "Buy now inside")
print(res["spam_score"])
```
