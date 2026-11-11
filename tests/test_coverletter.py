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


if __name__ == "__main__":
    unittest.main()
