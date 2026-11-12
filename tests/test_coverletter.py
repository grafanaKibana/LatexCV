import importlib.util
from pathlib import Path
import unittest


spec = importlib.util.spec_from_file_location(
    "prepare_coverletter",
    Path(__file__).resolve().parents[1] / "scripts/prepare-coverletter.py",
)
coverletter = importlib.util.module_from_spec(spec)
spec.loader.exec_module(coverletter)


class CoverLetterTests(unittest.TestCase):
    def test_preserves_unicode_and_paragraphs(self):
        text = "Hi,\n\nI’ve built C#/.NET agents.\n\nHappy to chat!"
        self.assertEqual(coverletter.render_text(text), text.replace("#", r"\#"))

    def test_normalizes_line_endings_and_wrapped_paragraphs(self):
        text = "  Hi,\r\n \r\nFirst line\r\nsecond line.\r\n\r\nThanks!\r\n"
        self.assertEqual(
            coverletter.render_text(text), "Hi,\n\nFirst line second line.\n\nThanks!"
        )

    def test_escapes_every_latex_special_character(self):
        self.assertEqual(
            coverletter.render_text("\\{}$&#%_~^"),
            r"\textbackslash{}\{\}\$\&\#\%\_\textasciitilde{}\textasciicircum{}",
        )

    def test_latex_commands_remain_literal_text(self):
        self.assertEqual(
            coverletter.render_text(r"\input{secret} % ignored"),
            r"\textbackslash{}input\{secret\} \% ignored",
        )

    def test_rejects_empty_input(self):
        for text in ("", " \n\t\r\n"):
            with self.subTest(text=text), self.assertRaises(ValueError):
                coverletter.render_text(text)

    def test_sections_use_original_template_and_escape_all_fields(self):
        document = coverletter.render_sections(
            "R&D_Company", "C#/.NET\n\nNLP", "100% alignment", r"\input{secret}"
        )
        self.assertIn(r"\newcommand{\coverlettercompany}{R\&D\_Company}", document)
        self.assertIn("C\\#/.NET\n\nNLP", document)
        self.assertIn(r"100\% alignment", document)
        self.assertIn(r"\textbackslash{}input\{secret\}", document)
        self.assertTrue(document.endswith("\\input{latex/coverletter/coverletter.tex}\n"))
        self.assertNotIn(r"\documentclass", document)

    def test_sections_reject_each_blank_field(self):
        for index in range(4):
            values = ["Company", "About me", "Why company", "Why me"]
            values[index] = " \n\t"
            with self.subTest(index=index), self.assertRaises(ValueError):
                coverletter.render_sections(*values)

    def test_company_name_is_one_line(self):
        document = coverletter.render_sections(" Acme\r\n Team ", "About", "Why", "Me")
        self.assertIn(r"\coverlettercompany}{Acme Team}", document)

    def test_optional_intro_preserves_paragraphs_and_escapes_latex(self):
        document = coverletter.render_sections(
            "Company", "About", "Why company", "Why me", intro="Hello R&D!\n\n100% interested."
        )
        self.assertIn(
            "\\newcommand{\\coverletterintro}{Hello R\\&D!\n\n100\\% interested.}", document
        )

    def test_blank_intro_does_not_add_content(self):
        for intro in ("", " \n\t"):
            with self.subTest(intro=intro):
                document = coverletter.render_sections("Company", "About", "Why", "Me", intro=intro)
                self.assertNotIn(r"\newcommand{\coverletterintro}", document)

    def test_full_text_preserves_own_greeting_and_closing(self):
        document = coverletter.render_full_text("Hi,\n\nMy letter.\n\nThanks!")
        self.assertIn("Hi,\n\nMy letter.\n\nThanks!", document)
        self.assertIn(r"\newcommand{\coverlettercontent}", document)
        self.assertTrue(document.endswith("\\input{latex/coverletter/coverletter.tex}\n"))
        self.assertNotIn(r"\lettersection", document)
        self.assertNotIn(r"\makeletterclosing", document)

    def test_full_text_rejects_empty_letter(self):
        with self.assertRaises(ValueError):
            coverletter.render_full_text(" \n")


if __name__ == "__main__":
    unittest.main()
