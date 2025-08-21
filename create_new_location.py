import requests

class create_new_location:

    def __init__(self):
        self.base_url = 'https://rahulshettyacademy.com'
        self.key = '?key=qaclick123'
        self.post_resource = '/maps/api/place/add/json'
        self.get_resource = '/maps/api/place/get/json'
        self.put_resource = '/maps/api/place/update/json'

        self.post_url = self.base_url + self.post_resource + self.key
        self.put_url = self.base_url + self.put_resource + self.key
        self.get_url = self.base_url + self.get_resource + self.key + '&place_id='

    # Создаем новый адрес через POST
    def post_request (self, json_location):
        result_post = requests.post(self.post_url, json=json_location)
        print(result_post.json())

        print(f'Статус-код: {result_post.status_code}')
        assert result_post.status_code == 200
        print('Статус-код POST корректный')

    # Проверяем наличие адреса через GET
    def get_request(self, place_id):
        url = self.get_url + place_id
        result_get = requests.get(url)
        print(result_get.json())

        print(f'Статус-код: {result_get.status_code}')
        assert result_get.status_code == 200
        print('Статус-код GET корректный')

    # Вносим изменения в адрес через PUT и проверяем на корректность
    def put_request(self, place_id, new_address):
        update_data = {
            "place_id": place_id,
            "address": new_address,
            "key": "qaclick123"
        }

        result_put = requests.put(self.put_url, json=update_data)
        print(result_put.json())

        print(f'Статус-код: {result_put.status_code}')
        assert result_put.status_code == 200
        print('Статус-код PUT корректный')

        check_response_put = result_put.json()
        msg = check_response_put.get('msg')
        print(msg)
        assert msg == 'Address successfully updated'
        print('Поле MSG корректно')