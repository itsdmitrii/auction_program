from art import *

print(logo)
dictionary = {}
def bid_info():
  additional_user = True
  while additional_user:
    user_name = input("What is your name?: ")
    bid_price = int(input("What's your bid price?: $"))
    dictionary[user_name] = bid_price
    other_users = input("Is there any other bidders? Type 'yes' or 'no'.\n").lower()
    if other_users == "no":
      additional_user = False


bid_info()
max_bid = 0
for bidder in dictionary:
  bid_amount = dictionary[bidder]
  if bid_amount > max_bid:
    max_bid = bid_amount
    winner = bidder

print(f"The winner is {winner} with a bid of $ {max_bid}.")