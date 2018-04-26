import datetime

def string_term(b):
    convert = {0:0, 1:1, 2:2, 3:2, 4:2, 5:0, 6:0, 7:0, 8:0, 9:0, 11:0, 12:0, 13:0, 14:0}
    list_term = {
        0: ["дней", "часов", "минут"],
        1: ["день", "час", "минута"],
        2: ["дня", "часа", "минуты"],
    }

    b = str(b)
    if(len(b) > 1):
        b = b[-2:]
        if(b != '11' and b != '12' and b != '13' and b != '14'):
            b = str(b[-1:])

    b = int(b)
    return list_term[convert[b]]


def counter():
    delta = datetime.datetime(datetime.date.today().year + 1, 1, 1) - datetime.datetime.now()

    seconds = delta.seconds

    days = delta.days
    hours = int(seconds / 60 / 60)
    minuts = int(seconds / 60)
    if minuts >= 60: minuts = (int(seconds / 60) - int(60 * hours))

    return str(days) + " " + str(string_term(days)[0]) + " " + str(hours) + " " + str(string_term(hours)[1]) + " " + str(minuts) + " " + string_term(minuts)[2]

print(counter())