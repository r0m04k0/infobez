import random

class User:
    def __init__(self, name):
        self.name = name
        self.permissions = {}
        
    def add_permission(self, obj, permission):
        self.permissions[obj] = permission

class Object:
    def __init__(self, name):
        self.name = name

class Admin(User):
    def __init__(self, name):
        super().__init__(name)
        self.permissions = {'read': True, 'write': True, 'grant': True}


def print_permissions():
    for user in users:
        for obj in objects:
            user.add_permission(obj, 
                random.choice([['read'], ['write'], ['read', 'write']]))

    for user in users:
        print(f"\n{user.name} permissions:")
        for obj, permission in user.permissions.items():
            print(f"{obj.name}: {permission}")

    print("\nAdmin permissions:")
    for obj, permission in admin.permissions.items():
        print(f"{obj}: {permission}")

def manage_permissions(admin, user, obj):
    print(f"Current permissions for {user.name} on {obj.name}: {', '.join(user.permissions.get(obj, ['None']))}")
    action = input("Enter action (add / remove): ")
    
    if action == 'add':
        permissions = input("Enter permissions to add (comma separated): ").split(',')
        user.add_permission(obj, permissions)
        print(f"Permissions added: {', '.join(permissions)}")
    elif action == 'remove':
        permissions = input("Enter permissions to remove (comma separated): ").split(',')
        current_permissions = user.permissions.get(obj, [])
        updated_permissions = [p for p in current_permissions if p not in permissions]
        user.add_permission(obj, updated_permissions)
        print(f"Permissions removed: {', '.join(permissions)}")
    else:
        print("Invalid action. Please enter 'add' or 'remove'.")
    
    print("\nUpdated permissions:")
    print(f"{user.name} permissions on {obj.name}: {', '.join(user.permissions.get(obj, ['None']))}")


users_count = 8
objects_count = 4

users = []
for i in range(users_count):
    users.append(User(f'User{i}'))

admin = Admin('Admin')

objects = []
for i in range(objects_count):
    objects.append(Object(f'Object{i}'))

print_permissions()
    
while True:
    username = input("\nEnter username to manage permissions >> ")

    if (username == 'Admin'):
        print_permissions()

    else:
        objectname = input("\nEnter object name >> ")
        for user in users:
            if user.name == username:
                for object in objects:
                    if object.name == objectname:
                        manage_permissions(admin, user, object)
                        break



# Пусть множество S возможных операций над объектами компьютерной 
# системы задано следующим образом: S = {«Доступ на чтение», «Доступ на 
# запись», «Передача прав»}.
# 1. Получить данные о количестве пользователей и объектов 
# компьютерной системы из табл. 2, соответственно варианту.
# 2. Реализовать программный модуль, создающий матрицу доступа 
# пользователей к объектам компьютерной системы. Реализация данного 
# модуля подразумевает следующее:
# 2.1. Необходимо выбрать идентификаторы пользователей, которые 
# будут использоваться при их входе в компьютерную систему (по одному 
# идентификатору для каждого пользователя, количество пользователей 
# указано для варианта). Например, множество из трёх идентификаторов 
# пользователей {Ivan, Sergey, Boris}. Один из данных идентификаторов 
# должен соответствовать администратору компьютерной системы 
# (пользователю, обладающему полными правами доступа ко всем объектам). 
# 2.2. Реализовать программное заполнение матрицы доступа, содержащей 
# количество пользователей и объектов, соответственно Вашему варианту.
# 2.2.1. При заполнении матрицы доступа необходимо учитывать, что 
# один из пользователей должен являться администратором системы 
# (допустим, Ivan). Для него права доступа ко всем объектам должны быть 
# выставлены как полные.
# 2.2.2. Права остальных пользователей для доступа к объектам 
# компьютерной системы должны заполняться случайным образом с помощью 
# датчика случайных чисел. При заполнении матрицы доступа необходимо 
# учитывать, что пользователь может иметь несколько прав доступа к 
# некоторому объекту компьютерной системы, иметь полные права, либо 
# совсем не иметь прав.
# 2.2.3. Реализовать программный модуль, демонстрирующий работу в 
# дискреционной модели политики безопасности. 
# 3. Данный модуль должен выполнять следующие функции:
# 3.1. При запуске модуля должен запрашиваться идентификатор 
# пользователя (проводится идентификация пользователя), при успешной 
# идентификации пользователя должен осуществляться вход в систему, при 
# неуспешной – выводиться соответствующее сообщение.
# 3.2. При входе в систему после успешной идентификации пользователя 
# на экране должен распечатываться список всех объектов системы с 
# указанием перечня всех доступных прав доступа идентифицированного 
# пользователя к данным объектам. Вывод можно осуществить, например, 
# следующим образом:
# User: Boris
# Идентификация прошла успешно, добро пожаловать в систему
# Перечень Ваших прав:
# Объект1:Чтение
# Объект2:Запрет
# Объект3:Чтение, Запись
# Объект4:Полные права
# Жду ваших указаний >
# 3.3. После вывода на экран перечня прав доступа пользователя к 
# объектам компьютерной системы, необходимо организовать ожидание 
# указаний пользователя на осуществление действий над объектами в 
# компьютерной системе. После получения команды от пользователя, на экран 
# необходимо вывести сообщение об успешности либо не успешности 
# операции. При выполнении операции передачи прав (grant) должна 
# модифицироваться матрица доступа. Программа должна поддерживать 
# операцию выхода из системы (quit), после которой запрашивается 
# идентификатор пользователя.