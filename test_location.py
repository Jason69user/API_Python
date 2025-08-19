import requests

class TestNewLocation:

    @staticmethod
    def create_new_location():

        base_url = 'https://rahulshettyacademy.com'
        key = '?key=qaclick123'
        post_resourse = '/maps/api/place/add/json'
        get_resourse = '/maps/api/place/get/json'

        post_url = base_url + post_resourse + key
        print(post_url)

        # тело запроса POST
        json_location = {
            "location": {
            "lat": -38.383494,
            "lng": 33.427362
        }, "accuracy": 50,
        "name": "Frontline house",
        "phone_number":
        "(+91) 983 893 3937",
        "address": "29, side layout, cohen 09",
        "types": ["shoe park","shop"],
        "website": "http://google.com",
        "language": "French-IN"
        }

        # очистить/создать файл перед добавлением
        open("place_id", "w", encoding="utf-8").close()

        # запускаем цикл 5 раз для отправки данных на сервер
        for i in range(5):
            result_post = requests.post(post_url, json=json_location)
            result_json = result_post.json()
            value_place_id = result_json.get("place_id")
            print(value_place_id)

            # записываем place_id в файл
            with open("place_id", "a") as f:
                f.write(value_place_id + "\n")

        # читаем place_id в файле и проверяем его через GET запрос
        with open("place_id", "r") as f:
            for line in f:
                place_id = line.strip()
                get_url = base_url + get_resourse + key + "&place_id=" + place_id
                print(get_url)
                print(f"place_id {place_id} существует\n")


TestNewLocation.create_new_location()