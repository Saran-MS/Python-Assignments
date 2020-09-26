def clc(dis,ticket):
    investment = 70
    investment *= dis/10
    profit = 80 * ticket
    if investment<profit:
        return profit-investment
    else:
        return -1
distance = int(input())
passengers = int(input())
print(clc(distance,passengers))
