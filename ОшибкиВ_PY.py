while True:  # Создаем бесконечный цикл
    try:  # код который должен выполнятся
        enter = float(input("enter digit "))
        print(100 / enter)
        # break

    except ValueError:
        print("you enter not a digit!!!")

    except ZeroDivisionError:  # перехват ошибки и дальше пишем какой ошибки
        # если ничего не писать, то перехватит любую ошибку, но луче прорабатывать
        # каждую ошибку чтоб понятно было что привело к ошибке
        print('you cannot divide by 0 !!!')

    else:  # необязательный оператор который выполняется только в том случае
        # если не было ошибки в try
        print("good job broooooooooooooooooo")

    finally:  # этот участок кода выполнится в любом случае если
        # Даже будет ошибка какая-то непредусмотренная это нужно для экстренного
        # закрытия программы сохранения файлов и т д и тп. Чтоб избежать потерии данных
        print("finish work")

print("everything is good")


