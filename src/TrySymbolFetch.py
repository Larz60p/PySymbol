# Author: Larz60+ (c) November 2019
#
import PySymbol


class myapp:
    '''
    Test routine for PySymbol.

    Note: To force a symbol update, change self.sym
    from: self.sym = PySymbol.PySymbol()
    To: self.sym = PySymbol.PySymbol(force_update=True)
    '''
    def __init__(self):
        self.sym = PySymbol.PySymbol()
    
    def Lookup_test(self):
        lookup = self.sym.Lookup
        # Lookup by company name
        mkt = 'NYSE'
        company = 'Raytheon Company'

        symbol = lookup(mkt, company_name=company)
        print(f"\nThe {mkt} stock symbol for {company} is {symbol}")


        # Lookup by Symbol
        mkt = 'NASDAQ'
        symbol = 'BFST'

        company = lookup(mkt, ticker=symbol)
        print(f"\nThe {mkt} company name for {symbol} is {company}")
 

if __name__ == '__main__':
    ma = myapp()
    ma.Lookup_test()
