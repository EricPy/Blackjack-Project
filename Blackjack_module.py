import random

values = {"Two":2,"Three":3,"Four":4,"Five":5,"Six":6,"Seven":7,"Eight":8,"Nine":9,"Ten":10,"Jack":10,"Queen":10,"King":10,"Ace":11}
suits = ("Hearts","Diamonds","Spades","Clubs")
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')

class Card():
	"""
	Class for cards
	"""
	
	def __init__(self, suit, rank):
		self.suit = suit.capitalize()
		self.rank = rank.capitalize()
		self.value = values[self.rank]

	def __str__(self):
		return self.rank + " of " + self.suit


class Deck:

	def __init__(self):
		self.all_cards = []

		for suit in suits:
			for rank in ranks:

				generated_card = Card(suit, rank)

				self.all_cards.append(generated_card)

	def deal(self):
		return self.all_cards.pop()

	def shuffle(self):
		random.shuffle(self.all_cards)

class Player:

	def __init__(self, bankroll=0):
		self.bankroll = bankroll
		self.hand = []

	def add_one(self, card):
		self.hand.append(card)

	def bet(self, amount):
		self.bankroll -= amount

	def win_bet(self, amount):
		self.bankroll += amount

	def clear(self):
		self.hand = []

class Dealer:

	def __init__(self):
		self.hand = []

	def add_one(self, card):
		self.hand.append(card)

	def clear(self):
		self.hand = []

def bootup():

	answer = "Bleh"

	while answer.lower() != "y" or answer.lower() != "n":
		try:
			answer = input("\nPlay a round? (Y/N) ")
		except:
			print("Incorrect input")
		else:
			if answer.lower() == "y":
				return True
				break
			elif answer.lower() == 'n':
				return False
				break

def point_count(person):

	alist = []
	
	for card in person.hand:
		alist.append(card.value)

	total = sum(alist)

	if 11 in alist and total > 21:
		return total-10
	else:
		return total

def win_check(person, hole_card = 0):
	return point_count(person) + hole_card == 21

def display(dealer, player, hole_card):

	print("\n")

	if point_count(dealer) + hole_card.value == 21:
		print(f"Dealer cards: {point_count(dealer)+hole_card.value}")
		print(f"- {str(dealer.hand[0])}")
		print(f"- {str(hole_card)}")
		for card in dealer.hand[1:]:
			print(f"- {str(card)}")
	 
		print(f"\nPlayer cards: {point_count(player)}")
		for card in player.hand:
			print(f"- {str(card)}")

	else:
		print(f"Dealer cards: {point_count(dealer)}")
		print(f"- {str(dealer.hand[0])}")
		print("- (X)")
		for card in dealer.hand[1:]:
			print(f"- {str(card)}")
	 
		print(f"\nPlayer cards: {point_count(player)}")
		for card in player.hand:
			print(f"- {str(card)}")

def hit_stay(dealer, player, deck):

	answer = "WRONG!!"

	while answer.lower() != "hit" or answer.lower() != "stay":
		try:
			answer = input("Hit or Stay? ")
		except:
			print("Incorrect input")
		else:
			if answer.lower() == "hit":
				player.add_one(deck.deal())

				display(dealer, player)
				answer = "WRONG!!"

			elif answer.lower() == 'stay':
				break

def choose_bet(player):
	pot = 1234567

	while pot > player.bankroll or pot < 0:
		try:
			pot = int(input(f"Available bankroll: {player.bankroll} \nYour bet: "))
		except:
			print("Incorrect input")
		else:
			if pot > player.bankroll or pot < 0:
				print("Insufficient Funds")
			else:
				pass
		finally:
			print("\n")
	
	return pot
