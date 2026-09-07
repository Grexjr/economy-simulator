from enum import Enum

class TransactionResult(Enum):
    SUCCESS = 1
    INSUFFICIENT_FUNDS = 2
    TOO_EXPENSIVE = 3
    INSUFFICIENT_GOODS = 4
    NEED_GOOD = 5


class MerchantStatus(Enum):
    BUYER = 1
    SELLER = 2
    HOLDER = 3
