available_weight = float(input())
loaded_count = reweight_count = waiting_count = 0

while True:
    box_weight = input()

    if box_weight == 'q':
        break

    try:
        box_weight = float(box_weight)
    except ValueError:
        reweight_count += 1
        continue

    if box_weight <= 0:
        reweight_count += 1
        continue

    if box_weight > available_weight:
        waiting_count += 1
        continue

    available_weight -= box_weight
    loaded_count += 1

print(loaded_count)
print(reweight_count)
print(waiting_count)
