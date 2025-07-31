import string

import requests


class TestCreateJoke():

    url = "https://api.chucknorris.io" # получаем ссылку на ресурс

    def test_create_random_joke(self):

        # сохраняем тип в переменную и добавляем в URL
        types = 'religion'
        path_random_joke_chuck = f"/jokes/random?category={types}"
        url_path_joke = self.url + path_random_joke_chuck
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
        joke_type = check_joke.get("categories")
        print(joke_type)
        assert types in joke_type
        print("Категория корректна")

        # проверка на имя в шутке
        joke_value = check_joke.get("value")
        assert "Chuck" in joke_value
        print("Имя Chuck есть в шутке")


start = TestCreateJoke()
start.test_create_random_joke()