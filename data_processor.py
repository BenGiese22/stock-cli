import datetime
from typing import Tuple

TO_FORMAT = '%d/%m/%Y %H:%M:%S'

class DataProcessor:

    def __init__(self) -> None:
        pass

    def process_data(self, data_set: dict) -> Tuple[list, list]:
        if 'Time Series (5min)' in data_set:
            from_format = '%Y-%m-%d %H:%M:%S' #2022/02/18 11:45:00
            return self._process(data_set, 'Time Series (5min)', from_format)
        elif 'Monthly Time Series' in data_set:
            from_format = '%Y-%m-%d'
            return self._process(data_set, 'Monthly Time Series', from_format)
        return [], []

    def _process(self, data_set: dict, time_series: str, from_format: str) -> Tuple[list, list]:
        time_series = data_set[time_series]
        closing_data = []
        dts = []
        for dt_key in time_series:
            time_segment = time_series[dt_key]
            closing_data.append(float(time_segment['4. close']))
            dts.append(self._format_datetime(dt_key, from_format, TO_FORMAT))
        reversed_data = closing_data[::-1]
        reversed_dts = dts[::-1]
        return reversed_data, reversed_dts

    def _format_datetime(self, _datetime: str, from_format: str, to_format: str) -> str:
        dt = datetime.datetime.strptime(_datetime, from_format)
        return dt.strftime(to_format)
