from copy import deepcopy

class PokerHand(object):
    RESULT = ["Loss", "Tie", "Win"]
    values = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
    suits = ['S', 'H', 'D', 'C']

    def __init__(self, hand):
        self.hand = hand.split()
        self._sort_hand()

    def show_hand(self):
        print(self.hand)

    def _sort_hand(self):
        hand = deepcopy(self.hand)
        arr_i = [hand[0][0], hand[1][0], hand[2][0], hand[3][0], hand[4][0]]
        arr = []
        for i in range(5):
            arr.append(self.values.index(arr_i[i]))
        arr.sort()
        arr = [self.values[arr[0]], self.values[arr[1]], self.values[arr[2]], self.values[arr[3]], self.values[arr[4]]]
        fin_arr = []
        for i in range(5):
            fin_arr.append(hand[int(arr_i.index(arr[i]))])
            hand.remove(hand[int(arr_i.index(arr[i]))])
            arr_i.remove(arr[i])
        self.hand = fin_arr

    def _count_value(self):
        self.points = 0

        if 'T' == self.hand[0][0] and \
                'J' == self.hand[1][0] and \
                'Q' == self.hand[2][0] and \
                'K' == self.hand[3][0] and \
                'A' == self.hand[4][0] and \
                self.hand[0][1] == self.hand[1][1] == self.hand[2][1] == self.hand[3][1] == self.hand[4][1]:
            self.points = 10

    def compare_with(self, other):
        pass
