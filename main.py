from poker_hand import PokerHand

player = PokerHand('2H 3H 4H 5H 6H')
opponent = PokerHand('KS AS TS QS JS')
print(player.compare_with(opponent))
