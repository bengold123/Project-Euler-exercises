"""def numbers_multiples_of_3(set=1001):
    listNumbers = []
    for number in range(set):
        if number % 3 == 0:
            listNumbers.append(number)
    return sum(listNumbers)


def numbers_multiples_of_5(set=1001):
    listNumbers = []
    for number in range(set):
        if number % 5 == 0:
            listNumbers.append(number)
    return sum(listNumbers)
"""


def Fibonaci_sequence(limit=4000000):
    listFibonaci = [1]
    number = 2
    listFibonaci.append(number)
    nextNumber = listFibonaci[-2] + listFibonaci[-1]
    while nextNumber <= limit:
        listFibonaci.append(nextNumber)
        nextNumber += listFibonaci[-2]

    return (listFibonaci)


def szukam_parzystych():
    listaParzystych = []
    for i in Fibonaci_sequence():
        if i % 2 == 0:
            listaParzystych.append(i)
    return sum(listaParzystych)


print(szukam_parzystych())
