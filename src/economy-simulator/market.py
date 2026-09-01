# Import methods
import random
from merchant import Merchant

class Market:  
    
    #Init method
    def __init__(self,merchant_number,prices=None):
        # Avoid mutable default arguments
        if prices is None:
            prices = {"wheat":5}
            
        # Initialize a blank list
        self.merchants = []
        
        # Populate list of merchants
        for i in range(merchant_number):
            self.merchants.append(Merchant())
            
        self.prices = prices
        
    def select_random_merchant(self):
        return random.choice(self.merchants)
        
    def validate_transaction(self,buyer,seller,good):
        buy = buyer.will_buy(self,good)
        if not buy:
            print(f"Merchant did not have enough money or {good} was too expensive!")
            return False
        sell = seller.will_sell()
        if not sell:
            print(f"Merchant did not have enough wheat to sell!")
            return False
        return True
        
    def attempt_transaction(self,good):
        # Runs a full transaction between buyer and seller
        # Random selects buyer and seller and enforces that they are different
        random_buyer = self.select_random_merchant()
        random_seller = self.select_random_merchant()
        while random_buyer == random_seller:
            random_seller = self.select_random_merchant()
        # Validates the transaction between the two, if valid runs the transaction effects
        if self.validate_transaction(random_buyer,random_seller,good):
            self.execute_transaction(random_buyer,random_seller,good)
            print(f"Merchant found buyer for {good} at {self.prices[good]}!")
            
    def execute_transaction(self,buyer,seller,good):
        buyer.adjust_cash(-self.prices[good])
        buyer.adjust_wheat(1)
        seller.adjust_cash(self.prices[good])
        seller.adjust_wheat(-1)

    def run_tick(self):
        self.attempt_transaction("wheat")
        self.update_price()
    
    # Print method
    def print_market(self):
        print(f"Prices:\n{self.prices}")
        print("Merchants:")
        for i in range (len(self.merchants)):
            self.merchants[i].print_merchant()
            
    # Methods to update prices
    # Get the demand for wheat
    def get_demand(self):
        demand = 0
        for i in range (len(self.merchants)):
            threshold = self.merchants[i].threshold
            query = self.merchants[i].cash - self.prices["wheat"]
            if query > threshold:
                demand += 1
        return demand
    
    # Get the supply of wheat
    def get_supply(self):
        supply = 0
        for i in range (len(self.merchants)):
            supply += self.merchants[i].wheat
        return supply
        
    # Updates price based on supply and demand; if supply >, price--; if demand >, price++
    def update_price(self):
        demand = int(self.get_demand())
        supply = int(self.get_supply())
        
        if demand > supply:
            self.prices["wheat"] += 1
        # Clamp price to 1
        elif demand < supply and self.prices["wheat"] > 1:
            self.prices["wheat"] -= 1
    
    
