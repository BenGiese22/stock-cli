from api import StockAPI
from enums.interval import Interval

"""
Request API Key on init load. Validate it. Store it for continous use. 

Graphing Commands, see on-going stock information.
- Commands to view different time frames - 1d (xd) 1w (xw) 1m (xm) 1y (xy)
- Possible Libraries
    - plotext
    - termplotlib
    - uniplot
    - termplot
    - terminalplot
"""

API_KEY = 'T9N0WM17ULYZHHPM'

def main():
    stock_api = StockAPI(API_KEY)
    stock_api.intraday('amd', Interval.FIVE_MIN)

if __name__ == '__main__':
    main()
