import os
from pathlib import Path

output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
output_dir.mkdir(parents=True, exist_ok=True)
ENTRY_TEXT = "You've reached the cat. " "If this is about the vase, I was asleep. If it's food at 4 a.m., I'm suddenly available."
(output_dir / "entry.txt").write_text(ENTRY_TEXT, encoding="utf-8")
