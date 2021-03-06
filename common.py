from enum import Enum

DEBUG = True

if DEBUG:
    FINNHUB_API_KEY = 'sandbox_c837q2qad3ift3bm38e0'
else:
    FINNHUB_API_KEY = 'c837q2qad3ift3bm38dg'

ALPHA_VANTAGE_API_KEY = 'T9N0WM17ULYZHHPM'

class TimeSeries(Enum):
    INTRADAY = "TIME_SERIES_INTRADAY"
    MONTHLY = "TIME_SERIES_MONTHLY"


"""
Request API Key on init load. Validate it. Store it for continous use. 

Graphing Commands, see on-going stock information.
- Commands to view different time frames - 1d (xd) 1w (xw) 1m (xm) 1y (xy)
- Possible Libraries
    - plotext
    - termplotlib
    - uniplot
    - terminalplot

Colored text - use "Colorama"

sys.stdout.write("\rDoing thing %i" % i)
sys.stdout.flush()
"""
