import datetime
from typing import Tuple

FROM_FORMAT = '%Y-%m-%d %H:%M:%S' #2022/02/18 11:45:00
TO_FORMAT = '%d/%m/%Y %H:%M:%S'

class DataProcessor:

    def __init__(self) -> None:
        pass

    def process_intraday_data(self, intraday_data: dict) -> Tuple[list, list]:
        time_series = intraday_data['Time Series (5min)'] # TODO Make dynamic
        closing_data = []
        dts = []
        for key in time_series:
            time_segment = time_series[key]
            closing_data.append(float(time_segment['4. close']))
            dts.append(self._format_datetime(key))
        # Reverse data so data starts from earliest datetime.
        reversed_data = closing_data[::-1]
        reversed_dts = dts[::-1]
        return reversed_data, reversed_dts

    def _format_datetime(self, _datetime: str) -> str:
        dt = datetime.datetime.strptime(_datetime, FROM_FORMAT)
        return dt.strftime(TO_FORMAT)
