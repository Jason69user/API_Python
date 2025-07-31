import requests


class TestCreateJoke():

    url = "https://official-joke-api.appspot.com" # получаем ссылку на ресурс

    def test_create_random_joke(self):

        # сохраняем тип в переменную и добавляем в URL
        types = 'dad'
        path_random_joke_dad = f"/jokes/{types}/random"
        url_path_joke = self.url + path_random_joke_dad
        print(url_path_joke)

        # отправляем запрос GET и выводим его json
        result = requests.get(url_path_joke)
        print(result.json())

        # сверяем статус код с ожидаемым
        print(f"Статус код: {result.status_code}")
        assert result.status_code == 200
        print("Статус-код корректный")

        # делаем проверку type шутки
        check_joke = result.json()
        joke_type = check_joke[0].get("type")
        print(joke_type)
        assert joke_type == types
        print("Тест прошел успешно ")


start = TestCreateJoke()
start.test_create_random_joke()