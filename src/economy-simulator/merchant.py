# Import modules
import random
from enums import TransactionResult, MerchantStatus

class Merchant:
    
    #Number is determined by sequence in which the merchant is added
    def __init__(self, number, cash=None, wheat=None, cash_threshold=None, wheat_threshold=None):
        # Random initialization of all values
        self.name = "Merchant" + str(number)
        self.cash = random.randint(1,100) if cash is None else cash
        self.wheat = random.randint(1,5) if wheat is None else wheat
        self.cash_threshold = random.randint(1,70) if cash_threshold is None else cash_threshold
        self.wheat_threshold = random.randint(1,self.wheat) if wheat_threshold is None else wheat_threshold


    # Returns true if has cash to buy wheat | TODO: will need to figure this out with more goods
    def has_cash_to_buy(self,market,good):
        return self.cash > 0 and self.cash >= market.prices[good]
    
    # Return true if desperate to buy wheat (below safety threshold of personal supply)
    def is_desperate(self):
        return self.wheat <= self.wheat_threshold

    # Return true if buying does not take buyer below cash threshold
    def is_willing_to_buy(self,market,good):
        return self.cash - market.prices[good] >= self.cash_threshold

    # Return true if have enough wheat to sell at all
    def has_wheat_to_sell(self):
        return self.wheat > 0

    # Return true if selling would not take below wheat threshold
    def is_willing_to_sell(self):
        return self.wheat - 1 >= self.wheat_threshold

    

    def is_merchant_buyer_or_seller(self,market,good):
        # Compute each boolean separately
        cash_to_buy = self.has_cash_to_buy(market,good)
        desperate = self.is_desperate()
        willing_to_buy = self.is_willing_to_buy(market,good)
        wheat_to_sell = self.has_wheat_to_sell()
        willing_to_sell = self.is_willing_to_sell()

        # If has cash and is desperate or willing to buy, then buyer
        wants_to_buy = cash_to_buy and (desperate or willing_to_buy)
        # If has wheat to sell and willing to sell, then seller
        wants_to_sell = wheat_to_sell and willing_to_sell
        # NOTE: if desperate, then will never be seller; so desperation always leads to buying behavior

        if wants_to_buy and wants_to_sell:
            # Both true, so need a tiebreaker
            # DEBUG
            #print("MERCHANT TIE!")
            return self.resolve_tie(market,good)
        if wants_to_buy:
            #print("MERCHANT IS BUYER")
            return MerchantStatus.BUYER
        if wants_to_sell:
            #print("MERCHANT IS SELLER")
            return MerchantStatus.SELLER
        else:
            #print("MERCHANT IS HOLDER")
            return MerchantStatus.HOLDER
            
    def resolve_tie(self,market,good):
        # Does not need to adjudicate negative resources/desperation on cash or wheat because guaranteed to not buy or sell if cash is low or wheat is low, respectively
        # Instead, just calculates margins and which is greater; however, cannot just do raw numbers b/c always more cash than wheat, so need proportions
        cash_margin = self.cash - self.cash_threshold
        wheat_margin = self.wheat - self.wheat_threshold

        # Get proportions; NOTE: divided by actual for what percent is essentially spare, since we do not have a robust consumption methodology yet 
        cash_proportion = cash_margin / self.cash
        wheat_proportion = wheat_margin / self.wheat

        # derive status from these; if more cash above threshold than wheat
        if cash_proportion >= wheat_proportion:
            return MerchantStatus.BUYER
        else:
            return MerchantStatus.SELLER

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
