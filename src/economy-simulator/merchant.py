# Import modules
import random

class Merchant:
    
    #Init method
    def __init__(self, cash=None, wheat=None, threshold=None):
        # Random initialization of all values
        self.cash = random.randint(1,100) if cash is None else cash
        self.wheat = random.randint(1,5) if wheat is None else wheat
        self.threshold = random.randint(1,70) if threshold is None else threshold


    def will_buy(self, market, item):
        # Validates if will buy
        # If cash is zero or less, do not buy
        if self.cash <= 0:
            return False
        # If item is too expensive, do not buy
        if self.cash - market.prices[item] < self.threshold:
            return False
        return True

    def will_sell(self):
        # Validates if will sell
        # If wares are zero, do not sell
        if self.wheat <= 0:
            return False
        return True

    # TODO: will need to make this generic to all goods, but for now just wheat
    def adjust_wheat(self, adjust):
        # Adjusts the good by the amount (can be negative)
        self.wheat += adjust

    def adjust_cash(self, adjust):
        # Adjusts cash by the amount (can be negative)
        self.cash += adjust
            
    # Method to print merchant
    def print_merchant(self):
        print("Merchant:\n")
        print(f"\t cash:{self.cash}\n")
        print(f"\t wheat:{self.wheat}\n")  
        print(f"\t threshold:{self.threshold}\n")
