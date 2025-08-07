import requests


class TestCreateJoke():

    url = "https://api.chucknorris.io" # получаем ссылку на ресурс

    def response_joke(self):

        menu_joke = {
            '1': "animal",
            '2': "career",
            '3': "movie",
            '4': "history",
            '5': "religion",
            '6': lambda: print('Выход из программы.') or quit()
        }

        while True:
            enter = input('\nВыберите категорию шутки из списка ниже:'
                      '\n1 - Животные'
                      '\n2 - Карьера'
                      '\n3 - Кино'
                      '\n4 - История'
                      '\n5 - Религия'
                      '\n6 - Выход'
                      '\nНажмите на цифру пункта меню: ')

            # проверяем наличие выбранной категории
            action = menu_joke.get(enter)
            path_list_categories = self.url + "/jokes/categories"
            result_categories = requests.get(path_list_categories)
            categories_json = result_categories.json()
            assert action in categories_json
            print('Есть несколько шуток в этой категории')

            # получаем шутку
            url_path_joke = self.url + f"/jokes/random?category={action}"
            result = requests.get(url_path_joke)
            joke_json = result.json()
            joke_value = joke_json.get('value')
            print(joke_value)


start = TestCreateJoke()
start.response_joke()