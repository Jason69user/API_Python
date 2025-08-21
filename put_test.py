from create_new_location import create_new_location # импортируем клас

# создаем экземпляр класса
location_manager = create_new_location()
# вносим изменения в адрес
new_address = 'Sanguinius street, RU'
location_manager.put_request('06a2e4af4292b7467b9efaa99635a143', new_address)