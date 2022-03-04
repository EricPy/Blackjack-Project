import Blackjack_module

#Set up the variables and objects
player = Blackjack_module.Player(100)
dealer = Blackjack_module.Dealer()
starting_bankroll = player.bankroll

game_on = True

#While game on
while game_on:

	if player.bankroll <= 0:
		print("Insufficient bankroll")
		break
	else:
		pass

	deck = Blackjack_module.Deck()
	deck.shuffle()

	#play a round?
	if Blackjack_module.bootup():
		pass
	else:
		break

	round_end = False
	
	#choose bet (added to pot variable)
	pot = Blackjack_module.choose_bet(player)
	player.bet(pot)
	
	#they each get 2 cards (dealer's hole card as its own variable)
	player.add_one(deck.deal())
	dealer.add_one(deck.deal())
	player.add_one(deck.deal())
	hole_card = deck.deal()

	#display the cards
	Blackjack_module.display(dealer, player, hole_card)

	#check in case one of them get a lucky hand
	if Blackjack_module.win_check(player):
		print(f"You have won the round")
		player.win_bet(pot*2)
		print(f"Your current bankroll: {player.bankroll}")
		round_end = True

		player.clear()
		dealer.clear()

	elif Blackjack_module.win_check(dealer, hole_card.value):
		print(f"Dealer Blackjack! (Hole card)")
		pot = 0
		print(f"Your current bankroll: {player.bankroll}")
		round_end = True

		player.clear()
		dealer.clear()

	else:
		pass

	#while player_turn:
	if not round_end:
		player_turn = True

		while player_turn:
			
			#hit or stay
			answer = "WRONG!!"

			while answer.lower() != "hit" or answer.lower() != "stay":
				try:
					answer = input("Hit or Stay? ")
				except:
					print("Incorrect input")
				else:
					if answer.lower() == "hit":
						player.add_one(deck.deal())

						Blackjack_module.display(dealer, player, hole_card)
						answer = "WRONG!!"

					elif answer.lower() == 'stay':
						break
				finally:
					#check if player got a blackjack/bust
						#if blackjack, player backroll add 2*pot, pot = 0, continue
						#if bust, pot = 0, continue

					if Blackjack_module.win_check(player):
						print(f"You have won the round!")
						player.win_bet(pot*2)
						print(f"Your current bankroll: {player.bankroll}")

						round_end = True
						
						break

					elif Blackjack_module.point_count(player) > 21:
						print(f"BUST!")
						pot = 0
						print(f"Your current bankroll: {player.bankroll}")

						round_end = True

						break

			#if stay, break/player_turn = False
			player_turn = False

		#while dealer's hand's value < player's total value:
		if not round_end:
			while Blackjack_module.point_count(dealer) < Blackjack_module.point_count(player):

				#dealer gets card
				dealer.add_one(deck.deal())
				Blackjack_module.display(dealer, player, hole_card)

				#Dealer blackjack
				if Blackjack_module.point_count(dealer) == 21:
					print("Dealer Blackjack!")
					pot = 0
					print(f"Your current bankroll: {player.bankroll}")

					break

				#if dealer's value + hole card == 21, pot = 0, continue
				if Blackjack_module.point_count(dealer) + hole_card.value == 21:
					print(f"Dealer uses hole card!")
					pot = 0
					print(f"Your current bankroll: {player.bankroll}")

					break

				#if dealer's value > player's value and dealer's value is <= 21, pot = 0, continue
				elif Blackjack_module.point_count(dealer) > Blackjack_module.point_count(player) and Blackjack_module.point_count(dealer) <= 21:
					print("Dealer Wins!")
					pot = 0
					print(f"Your current bankroll: {player.bankroll}")

					break			

				#if dealer's value == player's value: Tie, player has bet returned, continue
				elif Blackjack_module.point_count(dealer) == Blackjack_module.point_count(player):
					print("Tie!")
					player.win_bet(pot)
					pot = 0
					print(f"Your current bankroll: {player.bankroll}")

					break

				#if dealer's value > 21, player bankroll.add 2*pot, pot = 0
				elif Blackjack_module.point_count(dealer) > 21:
					print("Dealer BUST!")
					player.win_bet(pot*2)
					pot = 0
					print(f"Your current bankroll: {player.bankroll}")		

					break

				else:
					pass	

		#Game Over, hands reset
		player.clear()
		dealer.clear()

#Display: Starting bankroll, ending bankroll, and the increase
print("\n")
print(f"Starting bankroll: {starting_bankroll}")
print(f"Ending bankroll. : {player.bankroll}")
if starting_bankroll > player.bankroll:
	print(f"${starting_bankroll - player.bankroll} loss")
else:
	print(f"${player.bankroll - starting_bankroll} gain")
