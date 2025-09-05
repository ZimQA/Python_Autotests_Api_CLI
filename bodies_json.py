# Функция создания покемона
def body_create_pok():
    name = input("Имя покемона: ")
    photo_id = int(input("Фото ID: "))

    return {
        "name":name,
        "photo_id":photo_id
    }

# Частичное изменение покемона
def body_pach_pok():
    pokemon_id = input("ID Покемона ")
    new_name = input("Новое имя: ")

    return {
        "pokemon_id": pokemon_id,
        "name": new_name
    }

# Поймать в покебол
def body_poimat_v_pokeball():
    pokemon_id = input("ID Покемона ") 
    
    return {
        "pokemon_id": pokemon_id
    }