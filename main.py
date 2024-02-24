# че как брат нормально?
# все понял
from func import BankSystem

def main():
  bank_system = BankSystem()
  while True:
          print("\n⇺⇻⇺⇻⇺⇻⇺⇻⇺⇻⇺⇻⇺⇻⇺⇻⇺⇻⇺⇻⇻")
          print("Выберите действие:\n")

          if bank_system.bank_data['current_user'] is None:
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
                      bank_system.register_user(username, password)

              elif choice == "2":
                  bank_system.login_input()
              else:
                  print("Некорректный ввод. Попробуйте снова.")
          else:
              print("⇺⇻⇺⇻⇺⇻⇺⇻⇺⇻⇺⇻⇺⇻⇺⇻⇺⇻⇺⇻⇺⇻⇺⇻⇺⇻⇺⇻⇺⇻⇺⇻⇺⇻⇺⇻")
              print("3. Внесение денег на счет")
              print("4. Снятие денег со счета")
              print("5. Проверка баланса счета")
              print("⇺⇻⇺⇻⇺⇻⇺⇻⇺⇻⇺⇻⇺⇻⇺⇻⇺⇻⇺⇻⇺⇻⇺⇻⇺⇻⇺⇻⇺⇻⇺⇻⇺⇻⇺⇻")
              print("6. Перевод между пользователями")
              print("7. Перевод между счетами")
              print("⇺⇻⇺⇻⇺⇻⇺⇻⇺⇻⇺⇻⇺⇻⇺⇻⇺⇻⇺⇻⇺⇻⇺⇻⇺⇻⇺⇻⇺⇻⇺⇻⇺⇻⇺⇻")
              print("8. Показать логин и пароль")
              print("9. Выход из системы")
              print("0. Выход")
              print("⇺⇻⇺⇻⇺⇻⇺⇻⇺⇻⇺⇻⇺⇻⇺⇻⇺⇻⇺⇻⇺⇻⇺⇻⇺⇻⇺⇻⇺⇻⇺⇻⇺⇻⇺⇻")
              choice = input("\n>>> Введите номер действия: ")
              print("\n")

              if choice not in ("3", "4", "5", "6", "7", "8", "9", "0"):
                  print("Некорректный ввод. Попробуйте снова.")
                  continue

              if choice == "3": 
                  bank_system.deposit_input()
              elif choice == "4": 
                  bank_system.withdraw_input()
              elif choice == "5": 
                  bank_system.check_balance_input()
              elif choice == "6": 
                  bank_system.transfer_to_user_input()
              elif choice == "7": 
                  bank_system.transfer_input()
              elif choice == "8": 
                  bank_system.check_info_user_input()
              elif choice == "9": 
                  bank_system.logout_input()
              elif choice == "0": 
                  print("Выход из программы.")
                  break         
              else: 
                  print("Некорректный ввод. Попробуйте снова.")

if __name__ == "__main__":
  main()


