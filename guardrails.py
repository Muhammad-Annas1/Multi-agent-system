from typing import List

class OutputGuardrail:
    def __init__(self, banned_phrases=None):
        if banned_phrases is None:
            banned_phrases = ["sorry", "i'm sorry", "apologize", "apologies", "apologise"]
        self.banned_phrases = [p.lower() for p in banned_phrases]

    def validate(self, text: str) -> (bool, str):
        lower = text.lower()
        found = [p for p in self.banned_phrases if p in lower]
        if found:
            return False, f"Output rejected by guardrail — contains banned phrases: {found}"
        return True, text
