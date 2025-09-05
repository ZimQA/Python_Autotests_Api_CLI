import requests
import config
import bodies_json

# Создание покемона
def create_pokemon():
    body = bodies_json.body_create_pok()
    response = requests.post(url = f'{config.URL}/pokemons', headers = config.Header, json = body)
    print(response.text)

# Изменение имени
def change_name():
    body = bodies_json.body_pach_pok()
    response = requests.patch(url = f'{config.URL}/pokemons', headers = config.Header, json = body)
    print(response.text)

# Поймать в покебол
def catch_pokeball():
    body = bodies_json.body_poimat_v_pokeball()
    response = requests.post(url = f'{config.URL}/trainers/add_pokeball', headers = config.Header, json = body)
    print(response.text)

# Функция для выполнения всех тестов
def run_all_tests():
    create_pokemon()
    change_name()
    catch_pokeball()

# Главное меню
def main():
    while True:
        print("\n--- Меню тестов Pokémon API ---")
        print("1. Создать покемона")
        print("2. Изменить имя покемона")
        print("3. Поймать в покебол")
        print("4. Выполнить ВСЕ тесты подряд")
        print("0. Выйти")

        choice = input("\n Выберите действие: ")

        if choice == '1':
            create_pokemon()
        elif choice == '2':
            change_name()
        elif choice == '3':
            catch_pokeball()
        elif choice == '4':
            run_all_tests()
        elif choice == '0':
            print("Выход из программы...")
            break

        else: print("Выбран некорректный пункт меню")

# Запуск программы
if __name__ == "__main__":
    main()