import configuration
import requests
import data

def post_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDERS_PATH, json=body)


def get_order_track(params):
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDERS_TRACK_PATH, params=params)



