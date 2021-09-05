questions = [
    "1. Can I afford this?",
    "2. Do I need this?",
    "3. Do I have something similar, can I borrow or buy it second hand?",
    "4. Do I love it? ",
    "5. Does it suit my needs at this moment?",
    "6. Will I get a lot of use out of this item?",
    "7. If the item was full price would I still buy it? "
]
user_input = []

for i in questions:
    user_input.append(input(i + " : ").lower())

if user_input[2] == 'y' and user_input[5] == 'y' and user_input[6] == 'y':
    print("You can buy it")
else:
    print("Secondary need, try keeping it for 30 days in wish-list...")
