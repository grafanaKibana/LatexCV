"""Turn a complete plain-text letter from stdin into compiled/coverletter.tex."""

from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parents[1]
LATEX_ESCAPES = {
    "\\": r"\textbackslash{}",
    "{": r"\{",
    "}": r"\}",
    "$": r"\$",
    "&": r"\&",
    "#": r"\#",
    "%": r"\%",
    "_": r"\_",
    "~": r"\textasciitilde{}",
    "^": r"\textasciicircum{}",
}


def render_text(text):
    text = text.replace("\r\n", "\n").replace("\r", "\n").strip()
    if not text:
        raise ValueError("Cover letter text must not be empty.")
    paragraphs = re.split(r"\n\s*\n", text)
    return "\n\n".join(
        "".join(LATEX_ESCAPES.get(char, char) for char in " ".join(part.splitlines()))
        for part in paragraphs
    )


def main():
    try:
        body = render_text(sys.stdin.read())
    except ValueError as error:
        sys.exit(str(error))
    template = (ROOT / "latex/coverletter/plain-text.tex").read_text(encoding="utf-8")
    output = ROOT / "compiled/coverletter.tex"
    output.parent.mkdir(exist_ok=True)
    output.write_text(template.replace("%%LETTER_TEXT%%", body), encoding="utf-8")


if __name__ == "__main__":
    main()
