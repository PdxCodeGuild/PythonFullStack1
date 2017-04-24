"Simulates Powerball Investments."
import random


winners = {3, 10, 25, 26, 48}
cost = 2.0

def calc_winnnings(matches):


    if matches == 1:
        return 4
    elif matches == 2:
        return 7
    elif matches == 3:
        return 100
    elif matches == 4:
        return 50000
    elif matches == 5:
        return 1000000
    elif matches == 6:
        return 25000000

def guess(winners, ticket_cost, min_matches=1):
    main_bucket = range(1, 70)
    print("Created Random Bucket... \n")
    power_bucket = range(1, 27)
    print("Created Random Powerball Bucket... \n")
    counter = 0
    print("Guessing Numbers... \n")

    while True:
        result = random.sample(main_bucket, 5)
        #power_ball = random.choice(power_bucket)
        #result.append(power_ball)
        print(result)

        shared_numbers = winners.intersection(result)
        match_count = len(shared_numbers)
        #print("Tried {nums}".format(nums=result))
        counter += 1

        if match_count >= min_matches:
            investment = counter * ticket_cost
            winnings = calc_winnnings(match_count)
            net = winnings - investment

            print("Winner!\n \
            Winning Numbers: {nums}\n \
            After {tries} tries!\n \
            You spent ${dollars} before winning ${money}\n \
            You profited ${profit}".format(nums=shared_numbers,
            tries=counter, dollars=investment, money=winnings, profit=net))

            break
guess(winners, cost, min_matches=5)
