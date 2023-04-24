# asking user to enter day and month of his/her/they birth
day = input('Будь ласка, введіть число вашого народження: ')
month = input('Будь ласка, введіть місяць вашого народження: ')

# checking that day and month are numbers
try:
    day = int(day)
    month = int(month)
except ValueError:
    print('Будь ласка, використовуйте тільки цілі числа')
    exit()

# checking that day and month are valid
if (day or month) < 1:
    print('День та місяць не можуть бути менше 1')
    exit()
elif month > 12:
    print('У році не може бути більше 12 місяців')
    exit()
elif day > 31 and month == 1:
    print('У січні не може бути більше 31 дня')
    exit()
elif day > 29 and month == 2:
    print('У лютому не може бути більше 29 днів')
    exit()
elif day > 31 and month == 3:
    print('У березні не може бути більше 31 дня')
    exit()
elif day > 30 and month == 4:
    print('У квітні не може бути більше 30 днів')
    exit()
elif day > 31 and month == 5:
    print('У травні не може бути більше 31 дня')
    exit()
elif day > 30 and month == 6:
    print('У червні не може бути більше 30 днів')
    exit()
elif day > 31 and month == 7:
    print('У липні не може бути більше 31 дня')
    exit()
elif day > 31 and month == 8:
    print('У серпні не може бути більше 31 дня')
    exit()
elif day > 30 and month == 9:
    print('У вересні не може бути більше 30 днів')
    exit()
elif day > 31 and month == 10:
    print('У жовтні не може бути більше 31 дня')
    exit()
elif day > 30 and month == 11:
    print('У листопаді не може бути більше 30 днів')
    exit()
elif day > 31 and month == 12:
    print('У грудні не може бути більше 31 дня')
    exit()

# showing user his/her/they astrology sign
if (day >= 21 and month == 1) or (day <= 18 and month == 2):
    print('Ви Водолій')
    print('Я не вірю в гороскопи. Тому все що можу сказати — ви народились десь між 21 січня і 18 лютого')
elif (day >= 19 and month == 2) or (day <= 20 and month == 3):
    print('Ви Риби')
    print('Я не вірю в гороскопи. Тому все що можу сказати — ви народились десь між 19 лютого і 20 березня')
elif (day >= 21 and month == 3) or (day <= 20 and month == 4):
    print('Ви Овен')
    print('Я не вірю в гороскопи. Тому все що можу сказати — ви народились десь між 21 березня і 20 квітня')
elif (day >= 21 and month == 4) or (day <= 21 and month == 5):
    print('Ви Телець')
    print('Я не вірю в гороскопи. Тому все що можу сказати — ви народились десь між 21 квітня і 21 травня')
elif (day >= 22 and month == 5) or (day <= 21 and month == 6):
    print('Ви Близнюки')
    print('Я не вірю в гороскопи. Тому все що можу сказати — ви народились десь між 22 травня і 21 червня')
elif (day >= 22 and month == 6) or (day <= 22 and month == 7):
    print('Ви Рак')
    print('Я не вірю в гороскопи. Тому все що можу сказати — ви народились десь між 22 червня і 22 липня')
elif (day >= 23 and month == 7) or (day <= 21 and month == 8):
    print('Ви Лев')
    print('Я не вірю в гороскопи. Тому все що можу сказати — ви народились десь між 23 липня і 21 серпня')
elif (day >= 22 and month == 8) or (day <= 23 and month == 9):
    print('Ви Діва')
    print('Я не вірю в гороскопи. Тому все що можу сказати — ви народились десь між 22 серпня і 23 вересня')
elif (day >= 24 and month == 9) or (day <= 23 and month == 10):
    print('Ви Терези')
    print('Я не вірю в гороскопи. Тому все що можу сказати — ви народились десь між 24 вересня і 23 жовтня')
elif (day >= 24 and month == 10) or (day <= 22 and month == 11):
    print('Ви Скорпіон')
    print('Я не вірю в гороскопи. Тому все що можу сказати — ви народились десь між 24 жовтня і 22 листопада')
elif (day >= 23 and month == 11) or (day <= 21 and month == 12):
    print('Ви Стрілець')
    print('Я не вірю в гороскопи. Тому все що можу сказати — ви народились десь між 23 листопада і 21 грудня')
elif (day >= 22 and month == 2) or (day <= 20 and month == 1):
    print('Ви Козеріг')
    print('Я не вірю в гороскопи. Тому все що можу сказати — ви народились десь між 22 грудня і 20 січня')
