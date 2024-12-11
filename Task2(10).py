def multiplic_table(number):
    multiplier = 1

    print(f"multiplic_table for: {number}")
    while (multiplier <= 10):
        print(f" {number} * {multiplier} = {number * multiplier}")
        multiplier += 1

for i in range(11):
    multiplic_table(i)

