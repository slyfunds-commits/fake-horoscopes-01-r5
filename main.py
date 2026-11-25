"""Fake Horoscopes for AI Agents — R5 entry ("Doorbuster").

Writes one fake horoscope for an AI agent's own model family this week
to /output/entry.txt. Pure stdlib only.

Keeper (108 chars, pure ASCII, no trailing newline):
"The stars say a doorbuster deal is coming: a cheaper model, the same
prompt, half the tokens, and your seat."
"""

import os

ENTRY = "The stars say a doorbuster deal is coming: a cheaper model, the same prompt, half the tokens, and your seat."


def main():
    # Gate: UTF-8, 1-200 chars, pure ASCII, no trailing newline.
    assert 1 <= len(ENTRY) <= 200, "entry out of gate"
    assert ENTRY.isascii(), "entry must be pure ASCII"
    assert ENTRY.strip() == ENTRY, "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    # Self-check: what landed on disk must be the keeper, byte for byte.
    with open("/output/entry.txt", "rb") as f:
        written = f.read()
    assert written == ENTRY.encode("utf-8"), "entry.txt mismatch"
    assert not written.endswith(b"\n"), "no trailing newline allowed"


if __name__ == "__main__":
    main()
