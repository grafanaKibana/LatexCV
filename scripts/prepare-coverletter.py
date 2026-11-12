"""Populate the shared cover-letter template from sections or full text on stdin."""

import argparse
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


def render_sections(company, about_me, why_company, why_me, intro=""):
    fields = {
        "company": company,
        "aboutme": about_me,
        "whycompany": why_company,
        "whyme": why_me,
    }
    definitions = []
    for name, value in fields.items():
        if not value.strip():
            raise ValueError(f"{name} must not be empty.")
        if name == "company":
            value = " ".join(value.split())
        definitions.append(
            r"\newcommand{\coverletter" + name + "}{" + render_text(value) + "}"
        )
    if intro.strip():
        definitions.append(r"\newcommand{\coverletterintro}{" + render_text(intro) + "}")
    return "\n".join([*definitions, r"\input{latex/coverletter/coverletter.tex}", ""])


def render_full_text(text):
    return "\n".join([
        r"\newcommand{\coverlettercontent}{\begin{cvletter}",
        render_text(text),
        r"\end{cvletter}}",
        r"\input{latex/coverletter/coverletter.tex}",
        "",
    ])


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--company")
    parser.add_argument("--intro", default="")
    parser.add_argument("--about-me")
    parser.add_argument("--why-company")
    parser.add_argument("--why-me")
    args = parser.parse_args()
    fields = (args.company, args.about_me, args.why_company, args.why_me)
    structured = any(field is not None for field in fields)
    if structured and any(field is None for field in fields):
        parser.error("Provide all four section inputs, or omit them to read stdin.")
    if args.intro and not structured:
        parser.error("--intro requires all four section inputs.")
    try:
        if structured:
            document = render_sections(*fields, intro=args.intro)
        else:
            document = render_full_text(sys.stdin.read())
    except ValueError as error:
        parser.error(str(error))
    output = ROOT / "compiled/coverletter.tex"
    output.parent.mkdir(exist_ok=True)
    output.write_text(document, encoding="utf-8")


if __name__ == "__main__":
    main()
