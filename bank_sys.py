import bank_sys_func
while True:
    print("\n⇺⇻⇺⇻⇺⇻⇺⇻⇺⇻⇺⇻⇺⇻⇺⇻⇺⇻⇺⇻⇻")
    print("Выберите действие:\n")

    if bank_sys_func.bank.get("current_user") is None:
        print("⇺⇻⇺⇻⇺⇻⇺⇻⇺⇻⇺⇻⇺⇻⇺⇻⇺⇻⇺⇻⇺⇻⇺⇻⇺⇻⇺⇻⇺⇻⇺⇻⇺⇻⇺⇻")
        print("1. Регистрация нового пользователя")
        print("2. Вход в систему")
        print("⇺⇻⇺⇻⇺⇻⇺⇻⇺⇻⇺⇻⇺⇻⇺⇻⇺⇻⇺⇻⇺⇻⇺⇻⇺⇻⇺⇻⇺⇻⇺⇻⇺⇻⇺⇻")
        choice = input("\n>>> Введите номер действия: ")

        if choice == "1":
            username = input("Введите логин: ")
            password = input("Введите пароль: ")
            if username.isspace() and password.isspace():
                print("Некорректный ввод. Попробуйте снова.")
            else:
                result = bank_sys_func.register(username, password)
                print(result)

        elif choice == "2":
            username = input("Введите логин: ")
            password = input("Введите пароль: ")
            if username.isspace() and password.isspace():
                print("Некорректный ввод. Попробуйте снова.")
            else:
                result = bank_sys_func.login(username, password)
                print(result)
        else:
            print("Некорректный ввод. Попробуйте снова.")
    else:
        print("⇺⇻⇺⇻⇺⇻⇺⇻⇺⇻⇺⇻⇺⇻⇺⇻⇺⇻⇺⇻⇺⇻⇺⇻⇺⇻⇺⇻⇺⇻⇺⇻⇺⇻⇺⇻")
        print("1. Внесение денег на счет")
        print("2. Снятие денег со счета")
        print("3. Проверка баланса счета")
        print("⇺⇻⇺⇻⇺⇻⇺⇻⇺⇻⇺⇻⇺⇻⇺⇻⇺⇻⇺⇻⇺⇻⇺⇻⇺⇻⇺⇻⇺⇻⇺⇻⇺⇻⇺⇻")
        print("4. Перевод между пользователями")
        print("5. Взять кредит")
        print("6. Процент вероятности кредита")
        print("7. Платеж кредита")
        print("⇺⇻⇺⇻⇺⇻⇺⇻⇺⇻⇺⇻⇺⇻⇺⇻⇺⇻⇺⇻⇺⇻⇺⇻⇺⇻⇺⇻⇺⇻⇺⇻⇺⇻⇺⇻")
        print("8. Показать логин и пароль")
        print("9. Выход из системы")
        print("0. Выход")
        print("⇺⇻⇺⇻⇺⇻⇺⇻⇺⇻⇺⇻⇺⇻⇺⇻⇺⇻⇺⇻⇺⇻⇺⇻⇺⇻⇺⇻⇺⇻⇺⇻⇺⇻⇺⇻")
        choice = input("\n>>> Введите номер действия: ")
        print("\n")
        if choice not in ("1", "2", "3", "4", "5", "6", "7", "8", "9", "0"):
            print("Некорректный ввод. Попробуйте снова.")
            continue
        if choice == "1": 
            bank_sys_func.deposit()
        elif choice == "2": 
            bank_sys_func.withdraw()
        elif choice == "3": 
            result = bank_sys_func.check_balance()
            print(result)
        elif choice == "4": 
            result = bank_sys_func.transfer_to_user()
            print(result)
        # elif choice == "5": 
        #     bank_sys_func.transfer_input()
        # elif choice == "9": 
        #     bank_sys_func.check_info_user_input()
        # elif choice == "10": 
        #     bank_sys_func.logout_input()
        elif choice == "0": 
            print("Выход из программы.")
            break         
        else: 
            print("Некорректный ввод. Попробуйте снова.")


