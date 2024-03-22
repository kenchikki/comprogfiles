winning_numbers = {10, 11, 8, 1, 5, 20}
user_name, *user_numbers_str = input().split()

if len(user_numbers_str) != 6:
    print("Should be 6 numbers")
    quit()

user_numbers = set()
for num_str in user_numbers_str:
    num = int(num_str)
    if num in user_numbers:
        print("No duplicates allowed.")
        quit()
    user_numbers.add(num)

num_matched = len(winning_numbers & user_numbers)
prize_money = num_matched * 100

if num_matched > 0:
    print(f"{user_name} has won {prize_money} pesos!")
else:
    print(f"{user_name} won nothing!")
