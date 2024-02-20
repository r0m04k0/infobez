import random

users = 4
objects = 4

user_ids = ["Admin", "User2", "User3", "User4"]

rights = ["Чтение", "Запись", "Исполнение", "Запрет"]

access_matrix = []

for i in range(users):
    user_rights = []
    for j in range(objects):
        if user_ids[i] == "Admin":
            user_rights.append("Полные права")
        else:
            user_rights.append(random.choice
            (rights))
    access_matrix.append(user_rights)

def check_access(user, object, action):
    user_index = user_ids.index(user)
    object_index = int(object) - 1
    user_right = access_matrix[user_index][object_index]
    if user_right == action or user_right == "Полные права":
        return True
    else:
        return False

def grant_access(user_from, user_to, object, right):
    user_from_index = user_ids.index(user_from)
    user_to_index = user_ids.index(user_to)
    object_index = int(object) - 1
    user_from_right = access_matrix[user_from_index][object_index]
    if user_from_right == "Полные права":
        access_matrix[user_to_index][object_index] = right
        return True
    else:
        return False

def show_rights(user):
    user_index = user_ids.index(user)
    print(f"User: {user}")
    print("Идентификация прошла успешно, добро пожаловать в систему")
    print("Перечень Ваших прав:")
    for i in range(1, objects + 1):
        print(f"Объект{i}: {access_matrix[user_index][i - 1]}")
    print("Введите команду (read/write/execute) >>")

def handle_command(user):
    command = input()
    if command in ["read", "write", "execute"]:
        print("Над каким объектом производится операция?")
        object = input()
        if check_access(user, object, command):
            print("Операция прошла успешно")
        else:
            print("Отказ в выполнении операции.У Вас нет прав для ее осуществления")
    elif command == "grant":
        print("Право на какой объект передается?")
        object = input()
        print("Какое право передается?")
        right = input()
        print("Какому пользователю передается право?")
        user_to = input()
        if grant_access(user, user_to, object, right):
            print("Операция прошла успешно")
        else:
            print("Отказ в выполнении операции. У Вас нет прав для ее осуществления")
    elif command == "quit":
        print(f"Работа пользователя {user} завершена. До свидания.")
        print("User:")
        user = input()
        show_rights(user)
    else:
        print("Неверная команда. Повторите ввод.")
    handle_command(user)

print("User:")
user = input()
show_rights(user)
handle_command(user)