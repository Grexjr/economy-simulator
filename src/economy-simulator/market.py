# Import methods
import random

class Merchant:
    
    #Init method
    def __init__(self, cash=10, wheat=5, threshold=None):
        self.cash=cash
        self.wheat=wheat
        # Necessary to actually generate a random value each time
        if threshold is None:
            self.threshold=random.randint(1,100)
        else:
            self.threshold=threshold
        
    # Buy method with skip for if not enough money    
    def buy(self, item, market):
        # If cash to low, fail the buy
        if self.cash < market.prices[item]:
            print("Merchant tried to buy wheat, not enough cash!")
        # If buying wheat goes below threshold, do not buy
        if (self.cash - market.prices[item] < self.threshold):
            print("Merchant did not want to buy wheat at that price!")
        else:
            print("Merchant bought wheat.")
            self.cash = self.cash - market.prices[item]
            self.wheat += 1
            # Decrease wheat count of another random merchant
            random_seller = random.choice(market.merchants)
            random_seller.wheat -= 1

    # Sell method which checks if has enough wheat
    def sell(self, item, market):
        if self.wheat <= 0:
            print("Merchant tried to sell wheat, not enough wheat!")
        else:
            print("Merchant sold wheat.")
            self.cash = self.cash + market.prices[item]
            self.wheat -= 1
            # Increase wheat count of another random merchant
            random_buyer = random.choice(market.merchants)
            random_buyer.wheat += 1
            
    # Method to print merchant
    def print_merchant(self):
        print("Merchant:\n")
        print(f"\t cash:{self.cash}\n")
        print(f"\t wheat:{self.wheat}\n")  
        print(f"\t threshold:{self.threshold}\n")
    

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
        # Update the price
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
        # Clamp price to 0
        elif demand < supply and self.prices["wheat"] > 0:
            self.prices["wheat"] -= 1
    
    
