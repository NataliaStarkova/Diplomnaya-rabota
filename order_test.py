import configuration
import requests
import data
import sender_standart_request

# доступ к документации
def test_get_docs():
    return requests.get(configuration.URL_SERVICE + configuration.DOC_PATH)

response = test_get_docs()
print(response.status_code)


# Сохранение трекинг номера заказа

request = sender_standart_request.post_new_order(data.order_body)
track_number = request.json()['track']
print(track_number)

# Проверка что код ответа = 200

def positive_assert(track):
    params = data.get_track_params.copy()
    params['t'] = track
    request = sender_standart_request.get_order_track(params)
    assert request.status_code == 200

def test_status_code():
    positive_assert(track_number)










