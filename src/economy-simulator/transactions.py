from enum import Enum

class TransactionResult(Enum):
    SUCCESS = 1
    INSUFFICIENT_FUNDS = 2
    TOO_EXPENSIVE = 3
    INSUFFICIENT_GOODS = 4
