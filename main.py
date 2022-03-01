ticketsCount = int(input("Введите количество билетов: "))

ticketsSum = 0

for ticket in range(0, ticketsCount):
    age = int(input("Введите возраст: "))
    ticketPrice = 0
    if age < 18:
        ticketPrice = 0
    elif 18 <= age < 25:
        ticketPrice = 990
    else:
        ticketPrice = 1390
    ticketsSum = ticketsSum + ticketPrice

if ticketsCount > 3:
    ticketsSum = ticketsSum * 0.9

print("Сумма к оплате: ")
print(ticketsSum)
