list_of_cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
import random

user_deal = []
computer_deal = []


def deal_card():
    return random.choice(list_of_cards)


def calculate_score(deal):
    if sum(deal) == 21 and len(deal) == 2:
        return 0
    if 11 in deal and sum(deal) > 21:
        deal.remove(11)
        deal.append(1)
    return sum(deal)


draw_card = True

print(logo)
for _ in range(2):
    user_deal.append(deal_card())
    computer_deal.append(deal_card())

print(f"Your cards: {user_deal}, compter's first card: {computer_deal[0]}")
while draw_card:
    draw_card = input("Do you want to draw another card? Type 'y' or 'n': ") == 'y'
    if draw_card:
        user_deal.append(deal_card())
        print(f"Your cars: {user_deal}, computer's first card: {computer_deal[0]}")

user_score = calculate_score(user_deal)
computer_score = calculate_score(computer_deal)

while computer_score < 17:
    computer_deal.append(deal_card())
    computer_score = calculate_score(computer_deal)

if user_score > 21 and 11 in user_deal:
    user_deal.remove(11)
    user_deal.append(1)
if computer_score > 21 and 11 in computer_deal:
    computer_deal.remove(11)
    computer_deal.append(1)

if user_score > 21:
    print("You lose")
elif computer_score > 21:
    print("You win")
elif user_score == computer_score:
    print("Draw")
elif user_score > computer_score:
    print("You win")
else:
    print("You lose")

print(f"Your final hand: {user_deal}, user final score: {user_score}")
print(f"Computer's final hand: {computer_deal}, computer's final score: {computer_score}")
