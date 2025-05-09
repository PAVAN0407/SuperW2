users = [
    {"id": 1, "name": "Alice", "email": "alice@example.com"},
    {"id": 2, "name": "Bob", "email": "bob@example.com"},
]
def add_User():
    new_id=int(input("enter id:"))
    new_name=input("enter name:")
    new_email=input("enter email:")
    
    users.append({"id":new_id,"name":new_name,"email":new_email})
    print("new user added")

def read():
    if not users:
        print("no users")
    for user in users:
        print(user)

def delete():
    user_id=int(input("enter user id to delete:"))
    for user in users:
        if user["id"]==user_id:
            users.remove(user)
            print("user deleted successfully")
            return
    print('user not found')

def update():
    user_id=int(input("enter the user id to update: "))
    for user in users:
        if user["id"]==user_id:
            user["name"]=input("enter new name:")
            user["email"]=input("enter new email:")
            print("user details updated successfully")
            return
    print("user not found")

def main():
    while(True):
        print("CRUD Operations")
        print("1)add user")
        print("2)update")
        print("3)read")
        print("4)delete")
        print("5)exit")
        print("-"*10)
        choice=int(input("enter the operatio to perform(1-5):"))
        if(choice==1):
            add_User()
        elif(choice==2):
            update()
        elif(choice==3):
            read()
        elif(choice==4):
            delete()
        elif(choice==5):
            break
        else:
            print("wrong choice")
main()