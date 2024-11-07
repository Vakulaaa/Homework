def my_date(n):
    if n < 0 and n >=8640000:
        return "Wrong number!"

    days, b = divmod(n, 86400)
    hours, b =  divmod(n, 3600)
    minutes, b = divmod(n, 60)

    day_word = " день, " if days == 1 else(" дня, " if 2<= days <=4 else " дней ")
    formated_time = (
        f"{days}{day_word}"
        f"{str(hours).zfill(2)}:{str(minutes).zfill(2):{str(minutes).zfill(2)}}"
    )

    return formated_time

res = int(input("Write your number: "))
print(my_date(res))