# Import statements
from market import Merchant, Market

def main():
    
    merchants = []
    
    for i in range(5):
        merchants.append(Merchant())
    
    market = Market(merchants)
    
    print("How many ticks?")
    ticks = int(input())
    
    market.print_market()
    
    for x in range(ticks):
        market.run_tick()
        
    
    market.print_market()





if __name__ == "__main__":
    main()
