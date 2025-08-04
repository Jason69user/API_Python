import requests


class TestCreateJoke():

    url = "https://api.chucknorris.io" # получаем ссылку на ресурс

    def get_all_categories(self):

        # получаем ссылку на метод получения всех категорий
        path_list_categories = "/jokes/categories"
        url_path_categories = self.url + path_list_categories
        print(url_path_categories)

        result = requests.get(url_path_categories)
        categories_json = result.json()

        # запускаем цикл с перебором по одной шутки в каждой категории
        for a in categories_json:
            path_random_joke_chuck = f"/jokes/random?category={a}"
            url_path_joke = self.url + path_random_joke_chuck
            result = requests.get(url_path_joke)
            joke_json = result.json()
            joke_value = joke_json.get('value')
            print(joke_value)


start = TestCreateJoke()
start.get_all_categories()