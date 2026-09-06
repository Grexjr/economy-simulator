# Import modules
import random
from transactions import TransactionResult

class Merchant:
    
    #Number is determined by sequence in which the merchant is added
    def __init__(self, number, cash=None, wheat=None, cash_threshold=None, wheat_threshold=None):
        # Random initialization of all values
        self.name = "Merchant" + str(number)
        self.cash = random.randint(1,100) if cash is None else cash
        self.wheat = random.randint(1,5) if wheat is None else wheat
        self.cash_threshold = random.randint(1,70) if cash_threshold is None else cash_threshold
        self.wheat_threshold = random.randint(1,self.wheat) if wheat_threshold is None else wheat_threshold


    def will_buy(self, market, item):
        # Validates if will buy
        # If cash is zero or less, do not buy
        if self.cash <= 0:
            return TransactionResult.INSUFFICIENT_FUNDS
        # If below wheat threshold, get to wheat threshold; infinite buy; higher priority than cash threshold
        if self.wheat <= self.wheat_threshold:
            return TransactionResult.SUCCESS
        # If item is too expensive, do not buy
        if self.cash - market.prices[item] < self.cash_threshold:
            return TransactionResult.TOO_EXPENSIVE
        return TransactionResult.SUCCESS

    def will_sell(self):
        # Validates if will sell
        # If wares are zero, do not sell
        if self.wheat <= 0:
            return TransactionResult.INSUFFICIENT_GOODS
        # If selling would take below wheat threshold, do not sell
        if self.wheat - 1 <= self.wheat_threshold:
            return TransactionResult.NEED_GOOD
        return TransactionResult.SUCCESS

    # TODO: will need to make this generic to all goods, but for now just wheat
    def adjust_wheat(self, adjust):
        # Adjusts the good by the amount (can be negative)
        self.wheat += adjust

    def adjust_cash(self, adjust):
        # Adjusts cash by the amount (can be negative)
        self.cash += adjust
            
    # Method to print merchant
    def print_merchant(self):
        print(f"{self.name}\n")
        print(f"\t cash:{self.cash}\n")
        print(f"\t wheat:{self.wheat}\n")  
        print(f"\t cash_threshold:{self.cash_threshold}\n")
        print(f"\t wheat_threshold:{self.wheat_threshold}\n")
