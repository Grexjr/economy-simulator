# Import statements
from market import Market

def main():
    
    print("How many merchants?")
    number = int(input())
    
    market = Market(number)
    
    print("How many ticks?")
    ticks = int(input())
    
    market.print_market()
    
    for x in range(ticks):
        market.run_tick()
        
    
    market.print_market()





if __name__ == "__main__":
    main()
