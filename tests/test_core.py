from merchant import Merchant
from market import Market
from enums import MerchantStatus, TransactionResult

def test_merchant_not_buyer_when_cash_negative():
    market = Market(0)
    merchant = Merchant(1)

    merchant.cash = 0

    assert merchant.is_merchant_buyer_or_seller(market,"wheat") != MerchantStatus.BUYER

    merchant.cash = 3
    
    assert merchant.is_merchant_buyer_or_seller(market,"wheat") != MerchantStatus.BUYER



