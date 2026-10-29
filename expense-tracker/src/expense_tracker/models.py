from dataclasses import dataclass
from datetime import date
from decimal import Decimal


@dataclass
class Expense:
    id: int
    description: str
    category: str
    amount: Decimal
    date: date
