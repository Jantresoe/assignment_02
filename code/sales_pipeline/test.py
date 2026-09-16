"""Utilities for cleaning sales data."""


def clean_currency(value) -> float:
    """Convert a currency value to a floating-point number."""
    if value is None:
        return 0.0
    if isinstance(value, (int, float)):
        return float(value)
    return float(str(value).replace("$", "").replace(",", "").strip())


def clean_quantity(value) -> float:
    if value is None:
        return 0.0
    if isinstance(value, (int, float)):
        return float(value)
    return float(str(value).replace(",", "").strip())


def clean_sales_data(raw_data: list[dict]) -> list[dict]:
    cleaned_data = []
    for row in raw_data:
        price = clean_currency(row.get("price"))
        qty = clean_quantity(row.get("qty"))
        cleaned_row = {
            "date": row.get("date"),
            "item": row.get("item"),
            "price": price,
            "qty": qty,
        }
        cleaned_row["total_revenue"] = cleaned_row["price"] * cleaned_row["qty"]
        cleaned_data.append(cleaned_row)
    return cleaned_data
