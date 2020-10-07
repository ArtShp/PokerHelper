from copy import deepcopy

class PokerHand(object):
    RESULT = ["Win", "Tie", "Loss"]
    values = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']

    def __init__(self, hand):
        self.hand = hand.split()
        self.highcard_exception = ''
        self._sort_hand()
        self._count_value()

    def _get_points(self):
        return self.points

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
        self.highcard_exception2 = ''
        self.highcard_exception3 = ''
        self.highcard_exception4 = ''
        self.highcard_exception5 = ''
        if 'T' == self.hand[0][0] and \
                'J' == self.hand[1][0] and \
                'Q' == self.hand[2][0] and \
                'K' == self.hand[3][0] and \
                'A' == self.hand[4][0] and \
                self.hand[0][1] == self.hand[1][1] == self.hand[2][1] == self.hand[3][1] == self.hand[4][1]:
            self.points = 10
            self.highcard_exception = self.values.index(self.hand[4][0])
        else:
            for i in range(9):
                if self.values[i] == self.hand[0][0] and \
                        self.values[i+1] == self.hand[1][0] and \
                        self.values[i+2] == self.hand[2][0] and \
                        self.values[i+3] == self.hand[3][0] and \
                        self.values[i+4] == self.hand[4][0] and \
                        self.hand[0][1] == self.hand[1][1] == self.hand[2][1] == self.hand[3][1] == self.hand[4][1]:
                    self.points = 9
                    self.highcard_exception = self.values.index(self.hand[4][0])
                    break
            if self.points == 0:
                if self.hand[0][0] == self.hand[1][0] == self.hand[2][0] == self.hand[3][0]:
                    self.points = 8
                    self.highcard_exception = self.values.index(self.hand[0][0])
                    self.highcard_exception2 = self.values.index(self.hand[4][0])
                elif self.hand[1][0] == self.hand[2][0] == self.hand[3][0] == self.hand[4][0]:
                    self.points = 8
                    self.highcard_exception = self.values.index(self.hand[1][0])
                    self.highcard_exception2 = self.values.index(self.hand[0][0])
                elif self.hand[0][0] == self.hand[1][0] == self.hand[2][0] and self.hand[3][0] == self.hand[4][0]:
                    self.points = 7
                    self.highcard_exception = self.values.index(self.hand[0][0])
                    self.highcard_exception2 = self.values.index(self.hand[3][0])
                elif self.hand[0][0] == self.hand[1][0] and self.hand[2][0] == self.hand[3][0] == self.hand[4][0]:
                    self.points = 7
                    self.highcard_exception = self.values.index(self.hand[2][0])
                    self.highcard_exception2 = self.values.index(self.hand[0][0])
                elif self.hand[0][1] == self.hand[1][1] == self.hand[2][1] == self.hand[3][1] == self.hand[4][1]:
                    self.points = 6
                    self.highcard_exception = self.values.index(self.hand[4][0])
                    self.highcard_exception2 = self.values.index(self.hand[3][0])
                    self.highcard_exception3 = self.values.index(self.hand[2][0])
                    self.highcard_exception4 = self.values.index(self.hand[1][0])
                    self.highcard_exception5 = self.values.index(self.hand[0][0])
                else:
                    for i in range(9):
                        if self.values[i] == self.hand[0][0] and \
                                self.values[i+1] == self.hand[1][0] and \
                                self.values[i+2] == self.hand[2][0] and \
                                self.values[i+3] == self.hand[3][0] and \
                                self.values[i+4] == self.hand[4][0]:
                            self.points = 5
                            self.highcard_exception = self.values.index(self.hand[4][0])
                            break
                    if self.points == 0:
                        if self.hand[0][0] == self.hand[1][0] == self.hand[2][0]:
                            self.points = 4
                            self.highcard_exception = self.values.index(self.hand[0][0])
                            self.highcard_exception2 = self.values.index(self.hand[4][0])
                            self.highcard_exception3 = self.values.index(self.hand[3][0])
                        elif self.hand[1][0] == self.hand[2][0] == self.hand[3][0]:
                            self.points = 4
                            self.highcard_exception = self.values.index(self.hand[1][0])
                            self.highcard_exception2 = self.values.index(self.hand[4][0])
                            self.highcard_exception3 = self.values.index(self.hand[0][0])
                        elif self.hand[2][0] == self.hand[3][0] == self.hand[4][0]:
                            self.points = 4
                            self.highcard_exception = self.values.index(self.hand[2][0])
                            self.highcard_exception2 = self.values.index(self.hand[1][0])
                            self.highcard_exception3 = self.values.index(self.hand[0][0])
                        elif self.hand[0][0] == self.hand[1][0] and self.hand[2][0] == self.hand[3][0]:
                            self.points = 3
                            self.highcard_exception = self.values.index(self.hand[2][0])
                            self.highcard_exception2 = self.values.index(self.hand[0][0])
                            self.highcard_exception3 = self.values.index(self.hand[4][0])
                        elif self.hand[0][0] == self.hand[1][0] and self.hand[3][0] == self.hand[4][0]:
                            self.points = 3
                            self.highcard_exception = self.values.index(self.hand[3][0])
                            self.highcard_exception2 = self.values.index(self.hand[0][0])
                            self.highcard_exception3 = self.values.index(self.hand[2][0])
                        elif self.hand[1][0] == self.hand[2][0] and self.hand[3][0] == self.hand[4][0]:
                            self.points = 3
                            self.highcard_exception = self.values.index(self.hand[3][0])
                            self.highcard_exception2 = self.values.index(self.hand[1][0])
                            self.highcard_exception3 = self.values.index(self.hand[0][0])
                        elif self.hand[0][0] == self.hand[1][0]:
                            self.points = 2
                            self.highcard_exception = self.values.index(self.hand[0][0])
                            self.highcard_exception2 = self.values.index(self.hand[4][0])
                            self.highcard_exception3 = self.values.index(self.hand[3][0])
                            self.highcard_exception4 = self.values.index(self.hand[2][0])
                        elif self.hand[1][0] == self.hand[2][0]:
                            self.points = 2
                            self.highcard_exception = self.values.index(self.hand[1][0])
                            self.highcard_exception2 = self.values.index(self.hand[4][0])
                            self.highcard_exception3 = self.values.index(self.hand[3][0])
                            self.highcard_exception4 = self.values.index(self.hand[0][0])
                        elif self.hand[2][0] == self.hand[3][0]:
                            self.points = 2
                            self.highcard_exception = self.values.index(self.hand[2][0])
                            self.highcard_exception2 = self.values.index(self.hand[4][0])
                            self.highcard_exception3 = self.values.index(self.hand[1][0])
                            self.highcard_exception4 = self.values.index(self.hand[0][0])
                        elif self.hand[3][0] == self.hand[4][0]:
                            self.points = 2
                            self.highcard_exception = self.values.index(self.hand[3][0])
                            self.highcard_exception2 = self.values.index(self.hand[2][0])
                            self.highcard_exception3 = self.values.index(self.hand[1][0])
                            self.highcard_exception4 = self.values.index(self.hand[0][0])
                        else:
                            self.points = 1
                            self.highcard_exception = self.values.index(self.hand[4][0])
                            self.highcard_exception2 = self.values.index(self.hand[3][0])
                            self.highcard_exception3 = self.values.index(self.hand[2][0])
                            self.highcard_exception4 = self.values.index(self.hand[1][0])
                            self.highcard_exception5 = self.values.index(self.hand[0][0])

    def compare_with(self, other):
        pts1, pts2 = self.points, other._get_points()
        hce1, hce2 = self.highcard_exception, other.highcard_exception
        hce1_2, hce2_2 = self.highcard_exception2, other.highcard_exception2
        hce1_3, hce2_3 = self.highcard_exception3, other.highcard_exception3
        hce1_4, hce2_4 = self.highcard_exception4, other.highcard_exception4
        hce1_5, hce2_5 = self.highcard_exception5, other.highcard_exception5
        if pts1 == pts2:
            if hce1 > hce2:
                return self.RESULT[0]
            elif hce1 == hce2:
                if hce1_2 > hce2_2:
                    return self.RESULT[0]
                elif hce1_2 == hce2_2:
                    if hce1_3 > hce2_3:
                        return self.RESULT[0]
                    elif hce1_3 == hce2_3:
                        if hce1_4 > hce2_4:
                            return self.RESULT[0]
                        elif hce1_4 == hce2_4:
                            if hce1_5 > hce2_5:
                                return self.RESULT[0]
                            elif hce1_5 == hce2_5:
                                return self.RESULT[1]
                            else:
                                return self.RESULT[2]
                        else:
                            return self.RESULT[2]
                    else:
                        return self.RESULT[2]
                else:
                    return self.RESULT[2]
            else:
                return self.RESULT[2]
        elif pts1 > pts2:
            return self.RESULT[0]
        else:
            return self.RESULT[2]
