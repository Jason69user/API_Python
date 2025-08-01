import requests


class TestCreateJoke():

    url = "https://api.chucknorris.io" # получаем ссылку на ресурс

    def test_create_random_joke(self):

        # сохраняем тип в переменную и добавляем в URL
        types = 'religion'
        path_random_joke_chuck = f"/jokes/random?category={types}"
        url_path_joke = self.url + path_random_joke_chuck
        print(url_path_joke)

        # отправляем запрос GET, выводим его json и value
        result = requests.get(url_path_joke)
        joke_json = result.json()
        print(joke_json)
        joke_value = joke_json.get('value')
        print(joke_value)

        # сверяем статус код с ожидаемым
        print(f"Статус код: {result.status_code}")
        assert result.status_code == 200
        print("Статус-код корректный")

        # делаем проверку type шутки
        check_category = joke_json.get("categories")
        print(check_category)
        assert types in check_category
        print("Категория корректна")

        # проверка на имя в шутке
        joke_value = joke_json.get("value")
        assert "Chuck" in joke_value
        print("Имя Chuck есть в шутке")


start = TestCreateJoke()
start.test_create_random_joke()