# понял 
# случайно поставил табулацию 79 строке
import json
import re
import os
import logging

class BankSystem:
    def __init__(self):
        self.clients_file = "clients.json"
        self.bank_data = {
          'users': [], 
          'current_user': None}
        self.load_clients_from_file()
        logging.basicConfig(filename='errors.log', level=logging.ERROR)

    def save_clients_to_file(self):
        with open(self.clients_file, 'w') as file:
            json.dump(self.bank_data['users'], file, indent=2)

    def load_clients_from_file(self):
        if os.path.exists(self.clients_file):
            with open(self.clients_file, 'r') as file:
                self.bank_data['users'] = json.load(file)

    # Регистрация
    def register_user(self, username, password, initial_deposit_A=0, initial_deposit_B=0):
      try:

        if not re.match(r'^[^\s]{4,}$', username):
            raise ValueError("Логин должен содержать не менее 4 символов и не содержать пробелы.")
            return

        if not re.match(r'^[a-zA-Z0-9_-]{4,}$', password):
            raise ValueError("Пароль должен быть не менее 4 символов.")
            return

        user_exists = any(user['username'] == username for user in self.bank_data['users'])

        if not user_exists:
          new_user = {
            'username': username,
            'password': password,
            'deposit_A': initial_deposit_A,
            'deposit_B': initial_deposit_B
          }

          self.bank_data['users'].append(new_user)
          self.bank_data['current_user'] = username
          self.save_clients_to_file()
          print(f'\nПользователь {username} успешно зарегистрирован.') 

        else:
          print(f'\nПользователь с логином {username} уже существует.\n')
          raise ValueError("Пользователь с таким логином уже существует.")

      except ValueError as e:
        logging.error(f"Ошибка регистрации пользователя: {e}")
        print(f"Ошибка регистрации пользователя")



    # Вход   
    def login_user(self, username, password):
      try:
        if not re.match(r'^[a-zA-Z0-9_-]{4,}$', username):
          raise ValueError("Логин должен быть не менее 4 символов.")
          return False

        if not re.match(r'^[^\s]{4,}$', password):
          raise ValueError("Пароль должен содержать не менее 4 символов.")
          return False

        for user in self.bank_data['users']:
          if user['username'] == username and user['password'] == password:
              self.bank_data['current_user'] = username
              self.save_clients_to_file()
              return True  
            
        raise ValueError("Неверный логин или пароль.")

      except ValueError as e:
        logging.error(f"Ошибка входа пользователя: {e}")

    # Внести денг
    def deposit_money(self, deposit_type, amount):
      try:
        if self.bank_data['current_user'] is not None:
            for user in self.bank_data['users']:
                if user['username'] == self.bank_data['current_user']:
                    if deposit_type.upper() == "A" or deposit_type.upper() == "B":
                        user[f'deposit_{deposit_type.upper()}'] += amount
                        self.save_clients_to_file()
                        return True  
                    else:
                        print("Неверно указан тип депозита. Выберите 'A' или 'B'.")
                        raise ValueError("Неверный тип депозита.")
            print('Пользователь не найден в базе данных.')
            raise ValueError("Пользователь не авторизован.")
            return False  
        else:
            print('Необходимо войти в систему перед выполнением операции.')
            return False 
      except ValueError as e:
        logging.error(f"Ошибка внесения денег: {e}")

    # Перевести деньги между счетами
    def transfer_deposit_A_B(self, source_deposit_type, target_deposit_type, amount):
      try:
        if self.bank_data['current_user'] is not None:
            for user in self.bank_data['users']:
                if user['username'] == self.bank_data['current_user']:
                  if (source_deposit_type.upper() == "A" or source_deposit_type.upper() == "B") and (target_deposit_type.upper() == "A" or target_deposit_type.upper() == "B"):
                    if user[f'deposit_{source_deposit_type.upper()}'] >= amount:
                        user[f'deposit_{source_deposit_type.upper()}'] -= amount
                        user[f'deposit_{target_deposit_type.upper()}'] += amount
                        self.save_clients_to_file()
                        return True 
                    else:
                        print(f'Недостаточно средств на счете {source_deposit_type}.')
                        raise ValueError("Недостаточно средств на счете.")
                  else:
                      if source_deposit_type.upper() not in ["A", "B"]:
                        print(f"Не найден депозит {source_deposit_type}")
                        raise ValueError("Не найден депозит.")
                        return
                      if target_deposit_type.upper() not in ["A", "B"]:
                        print(f"Не найден депозит {target_deposit_type}")
                        raise ValueError("Не найден депозит.")
                        return
            print('Пользователь не найден в базе данных.')
            raise ValueError("Пользователь не найден в базе данных.")  
        else:
            print('Необходимо войти в систему перед выполнением операции.')  
      except ValueError as e:  
        logging.error(f"Ошибка перевода денег: {e}")

    # Перевести деньги между пользователями
    def transfer_to_user(self, target_username, deposit_type, amount):
      try:
        if self.bank_data['current_user'] is not None:
            if self.bank_data['current_user'] != target_username:
                source_user = next((user for user in self.bank_data['users'] if user['username'] == self.bank_data['current_user']), None)
                if source_user:
                    if deposit_type.upper() not in ["A", "B"]:
                        print(f"Не найден депозит {deposit_type}")
                        raise ValueError("Неверный тип депозита.")
                        return False

                    if source_user[f'deposit_{deposit_type.upper()}'] >= amount:
                        target_user = next((user for user in self.bank_data['users'] if user['username'] == target_username), None)
                        if target_user:
                            source_user[f'deposit_{deposit_type.upper()}'] -= amount
                            target_user[f'deposit_{deposit_type.upper()}'] += amount
                            self.save_clients_to_file()
                            return True
                        else:
                            print(f'Пользователь {target_username} не найден в базе данных.')
                            raise ValueError("Пользователь не найден в базе данных.")
                    else:
                        print(f'Недостаточно средств на счете пользователя {self.bank_data["current_user"]}.')
                        raise ValueError("Недостаточно средств на счете.")
                else:
                    print('Пользователь не найден в базе данных.')
            else:
                print('Нельзя осуществить перевод самому себе.')
      except ValueError as e:
        logging.error(f"Ошибка перевода денег: {e}")


    # Снятие денег со счета
    def withdraw(self, deposit_type, amount):
      try:
        if self.bank_data['current_user'] is not None:
            for user in self.bank_data['users']:
                if user['username'] == self.bank_data['current_user']:
                    if deposit_type.upper() not in ["A","B"]:
                      print(f"Не найден депозит {deposit_type}")
                      raise ValueError("Неверный тип депозита.")
                      print(f"Не найден депозит {deposit_type}")
                    if user[f'deposit_{deposit_type.upper()}'] >= amount:
                        user[f'deposit_{deposit_type.upper()}'] -= amount
                        self.save_clients_to_file()
                        return True
                    else:
                        print(f'Недостаточно средств на счете {deposit_type}.')
                        raise ValueError("Недостаточно средств на счете.")
      except ValueError as e:
        logging.error(f"Ошибка снятия средств: {e}")


    # Проверка баланса
    def check_balance(self, deposit_type):
        if self.bank_data['current_user'] is not None:
            for user in self.bank_data['users']:
                if user['username'] == self.bank_data['current_user']:
                    self.save_clients_to_file()
                    return True

    # Показать логин и пароль
    def check_info_user(self):
        if self.bank_data["users"]:
          last_register_user = self.bank_data["users"][-1]
          return last_register_user

    # Выйти из системы
    def user_logout(self):
      self.bank_data['current_user'] = None
      self.save_clients_to_file()


    def login_input(self):
      username = input("Введите логин: ")
      password = input("Введите пароль: ")
      if self.login_user(username, password):
          print(f'Вход в систему выполнен. Добро пожаловать, {username}!')
      else:
          print('Неверные логин или пароль.')

    def deposit_input(self):
      deposit_type = input("Выберите тип депозита (A или B): ")
      try:
          amount = float(input("Введите сумму для пополнения: "))
          if amount <= 0:
            raise ValueError("Сумма должна быть положительной")
            print("Сумма для пополнения должна быть положительным числом.")

          if amount > 0 and self.deposit_money(deposit_type.upper(), amount):
              print(f'На счет {deposit_type} внесено {amount} Ділдә.')
          else:
              print('Ошибка при пополнении счета.')
      except ValueError as e:
            logging.error(f"Ошибка ввода: {e}", )
            print("Пожалуйста, введите корректное числовое значение для суммы.")

    def transfer_input(self):
      deposit_1 = input("\nОткуда: ")
      deposit_2 = input("Куда: ")
      try:
          amount = float(input("Введите сумму для перевода со счета: "))
          if amount < 0:
            raise ValueError("Сумма должна быть положительной")
            print("Сумма для пополнения должна быть положительным числом.")
          if amount > 0 and self.transfer_deposit_A_B(deposit_1.upper(), deposit_2.upper(), amount):
              print(f'Переведено {amount} Ділдә со счета {deposit_1} на счет {deposit_2}.')
          else:
              raise ValueError("Недостаточно средств на счете")
              print('Ошибка при переводе между счетами.')
      except ValueError as e:
          logging.error(f"Ошибка ввода: {e}")
          print("Пожалуйста, введите корректное числовое значение для суммы.")


    def transfer_to_user_input(self):
      target_username = input("\nИмя пользователя: ")
      deposit_type = input("Выберите тип депозита (A или B): ")
      try:
        amount = float(input("Введите сумму для перевода со счета: "))
        if amount < 0:
          raise ValueError("Сумма должна быть положительной")
          print("Сумма для пополнения должна быть положительным числом.")
        if amount > 0 and amount != "" and self.transfer_to_user(target_username, deposit_type.upper(), amount):
          print(f'Переведено {amount} Ділдә от пользователя {self.bank_data["current_user"]} '
                                            f'пользователю {target_username}.')
      except ValueError as e:
        logging.error(f"Ошибка ввода: {e}")
        print("Пожалуйста, введите корректное числовое значение для суммы.")


    def withdraw_input(self):
      deposit_type = input("\nВыберите тип депозита (A или B): ")
      try:
        amount = float(input("Введите сумму для снятия со счета: "))
        if amount < 0:
          raise ValueError("Сумма должна быть положительной")
          print("Сумма для пополнения должна быть положительным числом.")
        if amount > 0 and self.withdraw(deposit_type.upper(),amount):
          print(f'Со счета {deposit_type.upper()} пользователя {self.bank_data["current_user"]} '
                                f'снято {amount} Ділдә.')
      except ValueError as e:
        logging.error(f"Ошибка ввода: {e}")
        print("Пожалуйста, введите корректное числовое значение для суммы.")  
      else:
        print('Ошибка при снятие счета.')


    def check_balance_input(self):
      deposit_type = input("\nВыберите тип депозита (A или B):")
      if deposit_type.upper() in ("A", "B") and self.check_balance(deposit_type.upper()):
          for user in self.bank_data['users']:
              if user['username'] == self.bank_data['current_user']:
                  print(f'Баланс счета {deposit_type.upper()} пользователя {user["username"]}: {user[f"deposit_{deposit_type.upper()}"]} Ділдә.')
      else:
          print(f'Ошибка при проверке баланса счета.')


    def check_info_user_input(self):
      last_registered_user = self.check_info_user()
      if last_registered_user:
          print(f"Логин: {last_registered_user['username']} \nПароль: {last_registered_user['password']}")


    def logout_input(self):
      self.user_logout()
      print('Выход из системы выполнен.')
