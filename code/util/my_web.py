import requests
import json

######################################################################################
# Configuration
datasource_url           = "https://markets.ft.com/data/chartapi/series"
datasource_days          = 365*5    # 5 years
datasource_default_stock = "VWRL:LSE:GBP"

stock_database = {
    "VWRL:LSE:GBP": {
        "symbol": "46487967",
        "name": "Vanguard FTSE All-World UCITS ETF"
    },
    "VFEM:LSE:GBP": {
        "symbol": "46487960",
        "name": "Vanguard FTSE Emerging Markets UCITS ETF USD Distributing"
    }
}

######################################################################################
"""
Fetch CSV data series from the Internet.

@param stock_shortname - optionally provide which stock you want, e.g "VWRL:LSE:GBP"
@return (date_series, value_series) - two lists for dates and prices
"""
def fetch_data(stock_shortname=datasource_default_stock):
    # prepare request data
    request_data = {
        "days": datasource_days,
        "dataNormalized": False,
        "dataPeriod": "Day",
        "dataInterval": 1,
        "realtime": False,
        "returnDateType": "ISO8601",
        "elements": [{
            "Type": "price",
            "Symbol": stock_database[stock_shortname]["symbol"]
        }]
    }
    request_data = dict_to_json(request_data)
    request_headers = {"Content-Type": "application/json"}

    # issue WEB request
    response = requests.post(datasource_url, request_data, headers=request_headers)

    # verify response and return data
    assert response.status_code == 200, "Error getting the stocks data for {}\n"\
                                        "Response: {}". format(stock_shortname, response.status_code)

    response_dict = json_to_dict(response.text)
    value_series  = extract_values_from_response(response_dict)
    date_series   = extract_dates_from_response(response_dict)

    assert len(value_series) == len(date_series), "Stock data does not have equal length"

    date_series = sanitise_dates(date_series)
    return date_series, value_series


def dict_to_json(dictionary):
    return json.dumps(dictionary)


def json_to_dict(json_str):
    return json.loads(json_str)


def extract_values_from_response(response):
    """
    When the data series comes back from the server, we need to get only the interesting bits,
    i.e. the data series for prices that we requeted
    component series are:
    0 - open
    1 - high
    2 - low
    3 - close   <- we use this one
    """
    return response["Elements"][0]["ComponentSeries"][3]['Values']


def extract_dates_from_response(response):
    return response["Dates"]


def sanitise_dates(dates):
    """
    Convert date format from
    "2012-05-23T00:00:00" to
    "2012-05-23"
    """
    result = []
    for date in dates:
        result.append(date.split('T')[0])
    return result


def pretty_print_POST(prepared):
    """
    Accept a prepared request and print what it would look like "raw"

    example:
    req = requests.Request('POST','https://markets.ft.com/data/chartapi/series',headers=request_headers,data=request_data)
    pretty_print_POST(req.prepare())
    """
    print('{}\n{}\r\n{}\r\n\r\n{}'.format(
        '-----------START-----------',
        prepared.method + ' ' + prepared.url,
        '\r\n'.join('{}: {}'.format(k, v) for k, v in prepared.headers.items()),
        prepared.body,
    ))


def print_available_stocks():
    for shortname, stock in stock_database.items():
        print("{} - {}".format(shortname, stock["name"]))