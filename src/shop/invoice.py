"""Rechnung aus Positionen zusammenstellen."""

from dataclasses import dataclass

from shop.pricing import line_total


@dataclass(frozen=True)
class Line:
    sku: str
    unit_net_cents: int
    quantity: int
    rate_percent: int = 19


def invoice_total(lines: list[Line]) -> int:
    """Gesamtbetrag einer Rechnung (brutto, in Cent)."""
    return sum(line_total(line.unit_net_cents, line.quantity, line.rate_percent) for line in lines)


def format_eur(cents: int) -> str:
    """Betrag für die Anzeige, z. B. 1234 -> '12,34 €'."""
    euros, rest = divmod(abs(cents), 100)
    sign = "-" if cents < 0 else ""
    return f"{sign}{euros},{rest:02d} €"
