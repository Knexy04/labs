from __future__ import annotations

import math
from typing import Iterable


class Calculator:
    def add(self, *numbers: float) -> float:
        if not numbers:
            return 0.0
        total: float = 0.0
        for value in numbers:
            total += float(value)
        return total

    def divide(self, numerator: float, denominator: float) -> float:
        if float(denominator) == 0.0:
            raise ZeroDivisionError("Cannot divide by zero")
        return float(numerator) / float(denominator)

    def is_prime_number(self, value: int) -> bool:
        n = int(value)
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True
