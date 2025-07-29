import requests

url = "https://official-joke-api.appspot.com/jokes/random" # получаем ссылку на ресурс
print(url)
result = requests.get(url) # отправляем запрос GET
print("Статус код : " + str(result.status_code))
assert 200 == result.status_code # сверяем статус код с ожидаемым
if result.status_code == 200:
    print("Успешно, статус код верный")
else:
    print("Провал, статус код не верный")
result.encoding = "utf-8" # используем стандартную кодировку
print(result.text) # выводим текст 