# Thank you lair001 for the definition of monetary system and bill, I have no idea what it is...

decreasing_values = [100.0, 50.0, 20.0, 10.0, 5.0, 2.0, 1.0, 0.5, 0.25, 0.1, 0.05, 0.01]


def makeChange(given, charged):

    total_change = given - charged
    remaining_change = total_change

    denominations = {
        "100.0": {"plural": "hundred-dollar bills", "count": 0},
        "50.0": {"plural": "fifty-dollar bills", "count": 0},
        "20.0": {"plural": "twenty-dollar bills", "count": 0},
        "10.0": {"plural": "ten-dollar bills", "count": 0},
        "5.0": {"plural": "five-dollar bills", "count": 0},
        "2.0": {"plural": "two-dollar bills", "count": 0},
        "1.0": {"plural": "dollar bills", "count": 0},
        "0.5": {"plural": "half dollars", "count": 0},
        "0.25": {"plural": "quarters", "count": 0},
        "0.1": {"plural": "dimes", "count": 0},
        "0.05": {"plural": "nickels", "count": 0},
        "0.01": {"plural": "pennies", "count": 0},
    }

    for value in decreasing_values:
        count = remaining_change // value
        remaining_change = round(remaining_change - count * value, 2)

        denominations[str(value)]["count"] = count

    return total_change, denominations


def ex31():
    given = int(input("Given: "))
    charge = int(input("Charge: "))
    bill_count = 0
    total_change, denominations = makeChange(given, charge)
    for value in decreasing_values:
        denomination = denominations[str(value)]
        count = denomination["count"]
        if count > 0:
            bill_count += count
            print("%s: %i" % (denomination["plural"], count))
    print("total change: $%.2f" % total_change)
    print("total number of bills and coins: %i" % bill_count)


ex31()
