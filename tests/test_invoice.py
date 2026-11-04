import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from shop.invoice import Line, format_eur, invoice_total  # noqa: E402


class InvoiceTest(unittest.TestCase):
    def test_single_line(self) -> None:
        self.assertEqual(invoice_total([Line("A-1", 1000, 2)]), 2380)

    def test_reduced_rate(self) -> None:
        self.assertEqual(invoice_total([Line("B-7", 500, 1, 7)]), 535)

    def test_format(self) -> None:
        self.assertEqual(format_eur(2380), "23,80 €")


if __name__ == "__main__":
    unittest.main()
