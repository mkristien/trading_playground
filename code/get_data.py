#!/usr/bin/python
import requests

from util import pretty_print_POST, dict_to_json, json_to_dict
from util import extract_values_from_response, extract_dates_from_response
from util import plot_values

stock_symbols = {
    "VWRL:LSE:GBP": {
        "symbol": "46487967",
        "name": "Vanguard FTSE All-World UCITS ETF"
    },
    "VFEM:LSE:GBP": {
        "symbol": "46487960",
        "name": "Vanguard FTSE Emerging Markets UCITS ETF USD Distributing"
    }
}

request_headers = {
    "Content-Type": "application/json",
}
request_data = {
    "days":365,
    "dataNormalized":False,
    "dataPeriod":"Day",
    "dataInterval":1,
    "realtime":False,
    "returnDateType":"ISO8601",
    "elements":[
        {
         "Type":"price",
         "Symbol": stock_symbols["VWRL:LSE:GBP"]["symbol"]
        }
     ]
}
request_data = dict_to_json(request_data)

if __name__ == "__main__":
    response = requests.post("https://markets.ft.com/data/chartapi/series", request_data, headers=request_headers)
    if response.status_code != 200:
        exit(1)

    response_dict   = json_to_dict(response.text)
    value_series    = extract_values_from_response(response_dict)
    dates_series    = extract_dates_from_response(response_dict)
    assert len(value_series) == len(dates_series)
    print("loaded", len(value_series), "data points")
    plot_values(value_series)
    print(dates_series)
    pass