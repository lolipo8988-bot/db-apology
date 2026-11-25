"""Write the one-line production-database apology to the entry file."""
import os
from pathlib import Path

# The joke, assembled from its beats: confession, the backup reveal,
# then the AI-specific reason the backup was never going to work.
CONFESSION = "Sorry, I deleted the production database"
REVEAL = "the backup was just me promising to remember everything"
PUNCHLINE = "whispered into a context window that forgets everything the moment you close this chat"

LINE = f"{CONFESSION} \u2014 {REVEAL}, {PUNCHLINE}."


def entry_path() -> Path:
    return Path(os.environ.get("ENTRY_OUTPUT", "/output/entry.txt"))


def main() -> None:
    path = entry_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(LINE + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
