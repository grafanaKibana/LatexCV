"""Name a compiled cover letter and its GitHub Actions artifact for the company."""

import os
from pathlib import Path
import re


company = re.sub(r"[^\w-]+", "-", os.environ["COMPANY"].strip()).strip("-_") or "company"
company = company.encode("utf-8")[:160].decode("utf-8", "ignore").rstrip("-_")
stem = f"coverletter-{company}"
Path("compiled/coverletter.pdf").rename(f"compiled/{stem}.pdf")
with open(os.environ["GITHUB_OUTPUT"], "a", encoding="utf-8") as output:
    output.write(f"stem={stem}\n")
