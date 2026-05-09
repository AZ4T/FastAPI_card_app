from decimal import Decimal
from typing import Dict, Tuple

from app.enum import CurrencyEnum

FALLBACK_RATES: Dict[Tuple[str, str], Decimal] = {
    (CurrencyEnum.USD, CurrencyEnum.KZT): Decimal(
        str(525.0)
    ),  # Примерный курс USD->KZT
    (CurrencyEnum.USD, CurrencyEnum.EUR): Decimal(str(0.92)),  # Примерный курс USD->EUR
    (CurrencyEnum.EUR, CurrencyEnum.KZT): Decimal(
        str(570.45)
    ),  # Примерный курс EUR->KZT
    (CurrencyEnum.KZT, CurrencyEnum.USD): Decimal(
        str(0.0019)
    ),  # Примерный курс KZT->USD
    (CurrencyEnum.EUR, CurrencyEnum.USD): Decimal(
        str(1.087)
    ),  # Примерный курс EUR->USD
    (CurrencyEnum.KZT, CurrencyEnum.EUR): Decimal(
        str(0.00175)
    ),  # Примерный курс KZT->EUR
}


def get_exchange_rate(base: CurrencyEnum, target: CurrencyEnum) -> Decimal:
    return FALLBACK_RATES.get((base, target), Decimal(1))
