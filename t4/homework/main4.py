if input() == 'start':

    print('ІНІЦІАЛІЗАЦІЯ БАНКОМАТУ')

    print('Працівник банку поповнює банкомат купюрами: ')
    cash_1000 = int(input('Кількість банкнот номіналом 1000 грн: '))
    cash_500 = int(input('Кількість банкнот номіналом 500 грн: '))
    cash_200 = int(input('Кількість банкнот номіналом 200 грн: '))
    cash_100 = int(input('Кількість банкнот номіналом 100 грн: '))
    cash_50 = int(input('Кількість банкнот номіналом 50 грн: '))
    cash_10 = int(input('Кількість банкнот номіналом 10 грн: '))

    cash_total = cash_1000 * 1000 + cash_500 * 500 + cash_200 * 200 + cash_100 * 100 + cash_50 * 50 + cash_10 * 10
    print(f'Банкомат ініціалізовано. Загальна сума: {cash_total} грн')

    print('=== БАНКОМАТ ПРАЦЮЄ ===')

    while cash_total > 0:
        balance = input('Вставте картку (зчитується баланс картки): ')
        if balance == 'quit':
            print('Банкомат відключено працівником.')
            break
        balance = int(balance)
        if balance == 0:
            print('На рахунку немає коштів.')
            continue
        # Передбачається, що баланс картки завжди невідʼємне ціле число.
        print(f'Доступний залишок на картці {balance} грн.')

        while True:
            amount = input('Введіть суму для зняття або q: ')
            if amount == 'q':
                print('Операцію скасовано. Наступний клієнт.')
                break

            # У клієнтів є у доступі клавіатура,
            # де є англійські літери, цифри та знаки + та -.
            try:
                amount = int(amount)
            except ValueError:
                print('Некоректна сума. Введіть додатне ціле число.')
                continue
            if amount <= 0:
                print('Некоректна сума. Введіть додатне ціле число.')
                continue
            # if not (not isinstance(amount, str) and (amount := int(amount)) > 0)

            if amount > balance:
                print(f'Доступний залишок на картці {balance} грн. Введіть відповідну суму.')
                continue

            if amount > cash_total:
                print(f'Доступний залишок в банкоматі {cash_total} грн. Введіть відповідну суму.')
                continue

            cash_total -= amount
            balance -= amount
            if balance > 0:
                print(f'Видано {amount} грн. Залишок на картці: {balance} грн.')
                if cash_total <= 0:
                    break
                continue

            print(f'Видано {amount} грн. На картці немає коштів.')
            break

print('=== БАНКОМАТ НЕ ПРАЦЮЄ ===')
