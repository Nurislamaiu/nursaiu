import re

bank = {
    "users": [{
        "useranme": "admin",
        "password": "123",
        "account": 0
    },{
        "useranme": "nurs",
        "password": "123",
        "account": 0
    }],
    "current_user": None
}

def login(username, password):

    if bank.get("username") == username and bank.get("password") == password:
        bank["current_user"] = username
        return f"Welcome!, {username}"
    return "Error in login or password"

def register(username, password):
    user = find_user_by_username(username)

    if user is not None:
        return "This login have a DataBase"
    
    if not is_valed_password(password):
        return "The password must not contain characters"
    
    
    new_user = create_new_user(username, password)
    bank["users"].append(new_user)
    bank["current_user"] = username    

def deposit():
    user = find_user_by_username(bank["current_user"])
    amount = input("Введите сумму: ")
    if int(amount) < 0:
        return "Сумма должен быть положительным"
    else:
        user["account"] += int(amount)
        return f"Пополнен {amount}$"
    
def withdraw():
    user = find_user_by_username(bank["current_user"])
    amount = input("Введите сумму: ")
    if amount < 0:
        return "Сумма должен быть положительным"
    else:
        user["account"] -= amount

def check_balance():
    user = find_user_by_username(bank["current_user"])
    balance = user["account"]
    return f"Ваш баланс {balance}"

def transfer_to_user():
    transfer_username = input("Кому: ")
    users = bank.get("username")
    print(f"* {users}")
    user_transfer = find_user_by_username(transfer_username)
    if user_transfer is None:
        return "Такого пользователя нет в Базе Данных"
    else:
        if bank["current_user"] == transfer_username:
            return "Нельзя отправить самому себя"
        else:
            amount = input("Введите сумму: ")
            if int(amount) < 0:
                return "Сумма должен быть положительным"
            else:
                user = find_user_by_username(bank["current_user"])
                user["account"] -= int(amount)
                user_transfer["account"] += int(amount)
                return f"Успешно отправленно {amount}$"
    











def is_valed_password(password):
    pattern = re.compile(r'[!@#$%^&*()<>?/\|}{~:]')
    return not bool(pattern.search(password))

def find_user_by_username(username):
    for user in bank.get("users"):
        if user.get("username") == username:
            return user
        return None
    
def has_access():
    return bank.get("current_user") is not None

def create_new_user(username, password):
    return {
        "username": username,
        "password": password,
        "account": 0,
    }

    

