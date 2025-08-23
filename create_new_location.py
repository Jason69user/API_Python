import requests

class CreateNewLocation:

    def __init__(self):
        self.base_url = 'https://rahulshettyacademy.com'
        self.key = '?key=qaclick123'
        self.post_resource = '/maps/api/place/add/json'
        self.get_resource = '/maps/api/place/get/json'
        self.put_resource = '/maps/api/place/update/json'
        self.delete_resource = '/maps/api/place/delete/json'

        self.post_url = self.base_url + self.post_resource + self.key
        self.put_url = self.base_url + self.put_resource + self.key
        self.get_url = self.base_url + self.get_resource + self.key + '&place_id='
        self.delete_url = self.base_url + self.delete_resource + self.key

    # Создаем новый адрес через POST
    def post_request (self, json_location):
        # очистить/создать файл перед добавлением
        open("place_id.txt", "w", encoding="utf-8").close()

        # запускаем цикл 5 раз для отправки данных на сервер
        for i in range(5):
            result_post = requests.post(self.post_url, json=json_location)
            result_json = result_post.json()
            value_place_id = result_json.get("place_id")
            print(value_place_id)
            print(f'Статус-код: {result_post.status_code}\n')
            assert result_post.status_code == 200

            # записываем place_id в файл
            with open("place_id.txt", "a") as f:
                f.write(value_place_id + "\n")

        # читаем place_id в файле и проверяем его через GET запрос
        with open("place_id.txt", "r") as f:
            for line in f:
                place_id = line.strip()
                print(f"place_id {place_id} существует")

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

    # Удаляем place_id
    def delete_request(self, place_id):
        delete_data = {
            "place_id": place_id
        }
        result_delete = requests.delete(self.delete_url, json=delete_data)
        print(f'place_id {place_id} удалён')

        print(f'Статус-код: {result_delete.status_code}')
        assert result_delete.status_code == 200
        print('Статус-код DELETE корректный')

        check_response_delete = result_delete.json()
        status = check_response_delete.get('status')
        assert status == 'OK'
        print('Поле Status корректно')

json_location = {
        "location": {
            "lat": -38.383494,
            "lng": 33.427362
        }, "accuracy": 50,
        "name": "Frontline house",
        "phone_number":
            "(+91) 983 893 3937",
        "address": "29, side layout, cohen 09",
        "types": ["shoe park", "shop"],
        "website": "http://google.com",
        "language": "French-IN"
    }

if __name__ == "__main__":
    location_manager = CreateNewLocation()
    location_manager.post_request(json_location)