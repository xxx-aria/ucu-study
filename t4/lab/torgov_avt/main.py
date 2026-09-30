DRINK_PRICE = 25

drinks_count = 0
drinks_bought = 0
total_cash = 0

if input() == 'start':
    print('ІНІЦІАЛІЗАЦІЯ ТОРГОВОГО АВТОМАТУ')
    print('Працівник заповнює автомат напоями та готівкою для решти:')

    drinks_count = int(input('Кількість напоїв (ціна 25 грн за штуку): '))

    cash_5 = int(input('Готівка номіналом 5 грн (кількість купюр): '))
    cash_10 = int(input('Готівка номіналом 10 грн (кількість купюр): '))
    cash_20 = int(input('Готівка номіналом 20 грн (кількість купюр): '))
    cash_50 = int(input('Готівка номіналом 50 грн (кількість купюр): '))
    cash_100 = int(input('Готівка номіналом 100 грн (кількість купюр): '))

    total_cash = 5 * cash_5 + 10 * cash_10 + 20 * cash_20 + 50 * cash_50 + 100 * cash_100

    print('Автомат ініціалізовано.')
    print(f'Кількість напоїв: {drinks_count}. Готівка: {total_cash} грн')

    print('=== ТОРГОВИЙ АВТОМАТ ПРАЦЮЄ ===')


    # У клієнтів є у доступі клавіатура, де є англійські літери, цифри та знаки + та -.
    while drinks_count > 0:
        raw = input('Внесіть кошти (сума): ')

        if raw == 'quit':
            print('Автомат відключено працівником.')
            break

        try:
            cash_input = int(raw)
        except ValueError:
           continue

        # not rerquired ??
        if cash_input <= 0:
                continue

        print(f'Внесено коштів: {cash_input} грн.')
        print(f'Напій коштує {DRINK_PRICE} грн. Залишилось напоїв: {drinks_count}')

        while cash_input > 0:
            raw_count = input('Укажіть кількість напоїв до покупки або q для припинення роботи (кошти повертаються): ')

            if raw_count == 'q':
                print(f'Решта: {cash_input} грн. Наступний клієнт.')
                break

            try:
                drinks_input = int(raw_count)
            except ValueError:
                print('Некоректна кількість. Введіть додатнє ціле число.')
                continue

            if drinks_input <= 0:
                print('Некоректна кількість. Введіть додатнє ціле число.')
                continue

            if drinks_input > drinks_count:
                print(f'Доступно лише {drinks_count} напоїв. Введіть відповідну кількість.')
                continue

            cost = drinks_input * DRINK_PRICE
            if  cost > cash_input:
                print(f'Недостатньо коштів. Потрібно {cost} грн, а у вас {cash_input} грн.')
                continue

            drinks_count -= drinks_input
            total_cash += cost
            cash_input -= cost
            drinks_bought += drinks_input
            print(f'Видано напоїв: {drinks_input} штук. Доступні кошти: {cash_input} грн.')

            if drinks_count <= 0:
                print(f'Решта: {cash_input} грн.')
                break

            if cash_input <= 0:
                print(f'Решта: {cash_input} грн. Наступний клієнт.')
                break

    print(f'Кількість виданих напоїв: {drinks_bought}. Готівка: {total_cash} грн')

print('=== ТОРГОВИЙ АВТОМАТ НЕ ПРАЦЮЄ ===')
