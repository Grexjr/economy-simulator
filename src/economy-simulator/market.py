# Import methods
import random

class Merchant:
    
    #Init method
    def __init__(self, cash=10, wheat=5):
        self.cash=cash
        self.wheat=wheat
        
    # Buy method with skip for if not enough money    
    def buy(self, item, market):
        if self.cash < market.prices[item]:
            print("Merchant tried to buy wheat, not enough cash!")
        else:
            print("Merchant bought wheat.")
            self.cash = self.cash - market.prices[item]
            self.wheat += 1

    # Sell method which checks if has enough wheat
    def sell(self, item, market):
        if self.wheat <= 0:
            print("Merchant tried to sell wheat, not enough wheat!")
        else:
            print("Merchant sold wheat.")
            self.cash = self.cash + market.prices[item]
            self.wheat -= 1
            
    # Method to print merchant
    def print_merchant(self):
        print("Merchant:\n")
        print(f"\t cash:{self.cash}\n")
        print(f"\t wheat:{self.wheat}\n")
            


class Market:  
    
    #Init method
    def __init__(self,merchants,prices={"wheat":5}):
        self.merchants=merchants
        self.prices=prices
        
    #Run tick method
    def run_tick(self):
        #Select a random merchant
        random_merchant = random.choice(self.merchants)
        #Decide if sell or buy attempt
        random_bool = bool(random.getrandbits(1))
        if random_bool:
            random_merchant.buy("wheat",self)
        else:
            random_merchant.sell("wheat",self)
    
    # Print method
    def print_market(self):
        print(f"Prices:\n{self.prices}")
        print("Merchants:")
        for i in range (len(self.merchants)):
            self.merchants[i].print_merchant()
    
    
