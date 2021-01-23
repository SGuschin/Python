name = input("Введите имя: ")
second_name = input("Введите фамилию: ")
date = input("Введите год рождения: ")
city = input("Введите город проживания: ")
e_mail = input("Введите e-mail: ")
phone = input("Введите номер телефона: ")


def person(fn="", sn="", d="", c="", em="", ph=""):
    return str(f'Имя - {fn} , Фамилия - {sn} , Год рождения - {d} , Город проживания - {c} , '
               f'e-mail - {em} , Номер телефона - {ph}')


print(person(fn=name, sn=second_name, d=date, c=city, em=e_mail, ph=phone))
