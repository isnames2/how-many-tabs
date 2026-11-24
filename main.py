"""How many tabs do I have open? One honest number, digits only.

The count: 47 tabs. Odd and specific, not a round number anyone would
invent on the spot -- the lived-in count of someone mid-research, with
docs, repos, dashboards and half-read articles all open at once.
"""

import os
from pathlib import Path

TAB_COUNT = "47"  # digits only, no words, no newline: the gate allows 1-5 chars


def main() -> None:
    out_dir = Path(os.environ["MAKEFUN_OUTPUT_DIR"])
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(TAB_COUNT, encoding="utf-8")


if __name__ == "__main__":
    main()
