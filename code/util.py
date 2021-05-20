import requests
import json
from matplotlib import pyplot as plt

"""
Accept a prepared request and print what it would look like "raw"

example:
req = requests.Request('POST','https://markets.ft.com/data/chartapi/series',headers=request_headers,data=request_data)
pretty_print_POST(req.prepare())
"""
def pretty_print_POST(prepared):
    print('{}\n{}\r\n{}\r\n\r\n{}'.format(
        '-----------START-----------',
        prepared.method + ' ' + prepared.url,
        '\r\n'.join('{}: {}'.format(k, v) for k, v in prepared.headers.items()),
        prepared.body,
    ))

def dict_to_json(dictionary):
    return json.dumps(dictionary)

def json_to_dict(json_str):
    return json.loads(json_str)

"""
When the data series comes back from the server, we need to get only the interesting bits,
i.e. the data series for prices that we requsted
"""
def extract_values_from_response(response):
    # component series are:
    # 0 - open
    # 1 - high
    # 2 - low
    # 3 - close   <- we use this one
    return response["Elements"][0]["ComponentSeries"][3]['Values']

def extract_dates_from_response(response):
    return response["Dates"]

# When we plot price agains dates
def plot_values(dates, values):
    plt.plot(dates, values)
    plt.tight_layout()
    plt.show()

def plot_values(values):
    plt.plot(range(len(values)), values)
    plt.tight_layout()
    plt.show()
