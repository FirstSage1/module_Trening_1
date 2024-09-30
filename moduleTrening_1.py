

class Databasa:
    def __init__(self):
        self.data = {}

    def add_user(self, username, password):
        self.data[username] = password
        # gprint(username)
class User:
    """
    Класс пользователя,содержащий атрибуты: логин, пароль,возраст.
    """
    def __init__(self, username, password, password_confirm):
        self.username = username
        if password == password_confirm:
            self.password = password
    # def __hash__(self):
    #     return ((self.nickname, self.password,self.age))
    #     print(self)

if __name__ == '__main__':
    databasa=Databasa()
    while True:
        choice = input("Привет. Выберите действие: \n1-Вход\n2-Регистрация\n")
        if choice == 1:
            login = input("Введите логин: ")
            password = input("Введите пароль: ")
            if login in databasa.data:
                if password==databasa.data[login]:
                    print(f"Вход выполнен, {login}")
                    break
                else:
                    print("Не верный пароль.")
            else:
                print('Пользователь не найден.')

        if choice == 2:
            user=User(input('Введите логин: '), password:= input('Введите пароль: '),
                  password2:=input('Повторите пароль: '))
            if password != password2:
                print("Пароли не совпадают, попрубуйте еще раз.")
                continue
            databasa.add_user(user.username, user.password)
        print(databasa.data)