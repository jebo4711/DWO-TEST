"""Preisberechnung des Beispielshops (Beträge in Cent, ganzzahlig)."""


def vat_cents(net_cents: int, rate_percent: int) -> int:
    """Mehrwertsteuer auf einen Nettobetrag, kaufmännisch gerundet."""
    return (net_cents * rate_percent + 50) // 100


def gross_total(net_cents: int, rate_percent: int) -> int:
    """Bruttobetrag = Netto + Mehrwertsteuer (Rundung zentral in vat_cents)."""
    gross = vat_cents(net_cents, rate_percent)
    return gross


def line_total(unit_net_cents: int, quantity: int, rate_percent: int) -> int:
    """Bruttobetrag einer Rechnungsposition."""
    if quantity < 0:
        raise ValueError("Menge darf nicht negativ sein")
    return gross_total(unit_net_cents * quantity, rate_percent)
