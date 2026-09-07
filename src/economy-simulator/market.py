# Import methods
import random
from merchant import Merchant
from enums import TransactionResult, MerchantStatus

class Market:  
    
    #Init method
    def __init__(self,merchant_number,prices=None):
        # Avoid mutable default arguments
        if prices is None:
            prices = {"wheat":5}
            
        # Initialize a blank list of all merchants, buyers, sellers
        self.merchants = []
        self.buyers = []
        self.sellers = []
        
        # Populate list of merchants
        for i in range(merchant_number):
            self.merchants.append(Merchant(i+1))
            
        self.prices = prices
       
    def run_tick(self):
        for merchant in self.merchants: 
            result = merchant.is_merchant_buyer_or_seller(self,"wheat")
            if result == MerchantStatus.BUYER:
                self.buyers.append(merchant)
            if result == MerchantStatus.SELLER:
                self.sellers.append(merchant)

        # shuffle lists to prevent early merchant number bias
        random.shuffle(self.buyers)
        random.shuffle(self.sellers)

        # Iterate through while both are not empty and pair them up
        while len(self.buyers) != 0 and len(self.sellers) != 0:
            self.attempt_transaction("wheat",self.buyers.pop(),self.sellers.pop())

        # Then update the price after all transactions of the tick have been done
        self.update_price()
        
    def validate_transaction(self,buyer,seller,good):
        # Buyer validation
        buy = buyer.will_buy(self,good)
        if buy == TransactionResult.INSUFFICIENT_FUNDS:
            print(f"{buyer.name} did not have enough money to buy {good}!")
            return False
        if buy == TransactionResult.TOO_EXPENSIVE:
            print(f"{buyer.name} felt {good} was too expensive!")
            return False
        # Seller validation
        sell = seller.will_sell()
        if sell == TransactionResult.INSUFFICIENT_GOODS:
            print(f"{seller.name} did not have enough {good} to sell!")
            return False
        if sell == TransactionResult.NEED_GOOD:
            print(f"{seller.name} needed to keep the {good}!")
            return False
        # If all validation succeeds, return true
        return True
        
    # This is the method that is run every tick
    def attempt_transaction(self,good,buyer,seller):
        # Validates the transaction between the two, if valid runs the transaction effects
        if self.validate_transaction(buyer,seller,good):
            self.execute_transaction(buyer,seller,good)
            print(f"{random_seller.name} found {random_buyer.name} for {good} at {self.prices[good]}!")
            
    def execute_transaction(self,buyer,seller,good):
        buyer.adjust_cash(-self.prices[good])
        buyer.adjust_wheat(1)
        seller.adjust_cash(self.prices[good])
        seller.adjust_wheat(-1) 
    
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
            cash_threshold = self.merchants[i].cash_threshold
            query = self.merchants[i].cash - self.prices["wheat"]
            if query > cash_threshold:
                demand += 1
        return demand
    
    # Get the supply of wheat - adjusted by who has enough to sell (not going below their threshold)
    def get_supply(self):
        supply = 0
        for i in range (len(self.merchants)):
            wheat_threshold = self.merchants[i].wheat_threshold
            query = self.merchants[i].wheat - 1
            if query > wheat_threshold:
                supply += 1
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


