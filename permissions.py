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

# # Создаем пользователей
# user1 = User('User1')
# user2 = User('User2')
# admin = Admin('Admin')

# # Создаем объекты
# obj1 = Object('Object1')
# obj2 = Object('Object2')

# # Выдаем права пользователям на объекты
# user1.add_permission(obj1, 'read')
# user1.add_permission(obj2, 'write')
# user1.add_permission(obj2, 'read')

# user2.add_permission(obj1, 'read')
# user2.add_permission(obj2, 'read')

# # Администратор выдает права пользователю user2 на obj2
# admin.add_permission(obj2, 'write')

# Выводим информацию о правах пользователей на объекты
# print("User1 permissions:")
# for obj, permission in user1.permissions.items():
#     print(f"{obj.name}: {permission}")

# print("\nUser2 permissions:")
# for obj, permission in user2.permissions.items():
#     print(f"{obj.name}: {permission}")

# print("\nAdmin permissions:")
# for obj, permission in admin.permissions.items():
#     print(f"{obj}: {permission}")

def manage_permissions(admin, user, obj):
    print(f"Current permissions for {user.name} on {obj.name}: {', '.join(user.permissions.get(obj, ['None']))}")
    action = input("Enter action (add / remove): ")
    
    if action == 'add':
        permissions = input("Enter permissions to add (comma separated): ").split(',')
        user.add_permissions(obj, permissions)
        print(f"Permissions added: {', '.join(permissions)}")
    elif action == 'remove':
        permissions = input("Enter permissions to remove (comma separated): ").split(',')
        current_permissions = user.permissions.get(obj, [])
        updated_permissions = [p for p in current_permissions if p not in permissions]
        user.add_permissions(obj, updated_permissions)
        print(f"Permissions removed: {', '.join(permissions)}")
    else:
        print("Invalid action. Please enter 'add' or 'remove'.")
    
    # Проверяем обновленные права пользователя
    print("\nUpdated permissions:")
    print(f"{user1.name} permissions on {obj1.name}: {', '.join(user1.permissions.get(obj1, ['None']))}")

# Пример использования интерфейса
obj1 = Object('Object1')
user1 = User('User1')
admin = Admin('Admin')

# Выдаем права пользователю user1 на obj1
user1.add_permissions(obj1, ['read'])

# Администратор управляет правами пользователя user1 на obj1
manage_permissions(admin, user1, obj1)

