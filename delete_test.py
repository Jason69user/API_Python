from create_new_location import CreateNewLocation # импортируем клас
import requests


base_url = 'https://rahulshettyacademy.com'
get_resource = '/maps/api/place/get/json'
key ='?key=qaclick123'

# создаем экземпляр класса
location_manager = CreateNewLocation()

needed_lines = [2, 4]  # номера нужных строк
open("three_place_id.txt", "w", encoding="utf-8").close() # очистить/создать файл перед добавлением

# читаем place_id и удаляем 2 и 4
with open("place_id.txt", "r") as f:
    for line_number, line in enumerate(f, 1):
        if line_number in needed_lines:
            place_id = line.strip()
            location_manager.delete_request(place_id)

# проверяем через GET удаление place_id
with open("place_id.txt", "r") as f:
    for line in f:
        place_id = line.strip()
        get_url = base_url + get_resource + key + "&place_id=" + place_id
        print(get_url)
        result_get = requests.get(get_url)

        if result_get.status_code == 200:
            print(f"place_id {place_id} существует\n")
            with open("three_place_id.txt", "a") as f: # добавляем в three_place_id place_id которые не удалены
                f.write(place_id + "\n")
        elif result_get.status_code == 404:
            print(f"place_id {place_id} не существует\n")
