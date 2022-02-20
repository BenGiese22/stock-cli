import time
import datetime
from typing import Tuple

class DataProcessor:

    def __init__(self) -> None:
        pass

    def process_intraday_data(self, intraday_data: dict) -> list:
        time_series = intraday_data['Time Series (5min)'] # TODO Make dynamic
        closing_data = []
        for key in time_series:
            time_segment = time_series[key]
            closing_data.append(float(time_segment['4. close']))
        # Reverse data so data starts from earliest datetime.
        reversed_data = closing_data[::-1]
        return reversed_data
