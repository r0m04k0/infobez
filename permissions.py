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

