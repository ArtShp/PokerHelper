class PokerHand(object):
    RESULT = ["Win", "Tie", "Loss"]
    VALUES = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']

    def __init__(self, hand):
        self.hand = hand.split()
        self.hce1 = ''
        self._sort_hand()
        self._count_value()

    def _get_points(self):
        return self.points

    def _sort_hand(self):
        arr_i = [self.hand[0][0], self.hand[1][0], self.hand[2][0], self.hand[3][0], self.hand[4][0]]
        arr = []
        for i in range(5):
            arr.append(self.VALUES.index(arr_i[i]))
        arr.sort()
        arr = [self.VALUES[arr[0]], self.VALUES[arr[1]], self.VALUES[arr[2]], self.VALUES[arr[3]], self.VALUES[arr[4]]]
        fin_arr = []
        for i in range(5):
            fin_arr.append(self.hand[int(arr_i.index(arr[i]))])
            self.hand.remove(self.hand[int(arr_i.index(arr[i]))])
            arr_i.remove(arr[i])
        self.hand = fin_arr

    def _count_value(self):
        self.points = 0
        self.hce1, self.hce2, self.hce3, self.hce4, self.hce5 = ('' for i in range(5))
        if 'T' == self.hand[0][0] and \
                'J' == self.hand[1][0] and \
                'Q' == self.hand[2][0] and \
                'K' == self.hand[3][0] and \
                'A' == self.hand[4][0] and \
                self.hand[0][1] == self.hand[1][1] == self.hand[2][1] == self.hand[3][1] == self.hand[4][1]:
            self.points = 10
            self.hce1 = self.VALUES.index(self.hand[4][0])
        else:
            for i in range(9):
                if self.VALUES[i] == self.hand[0][0] and \
                        self.VALUES[i+1] == self.hand[1][0] and \
                        self.VALUES[i+2] == self.hand[2][0] and \
                        self.VALUES[i+3] == self.hand[3][0] and \
                        self.VALUES[i+4] == self.hand[4][0] and \
                        self.hand[0][1] == self.hand[1][1] == self.hand[2][1] == self.hand[3][1] == self.hand[4][1]:
                    self.points = 9
                    self.hce1 = self.VALUES.index(self.hand[4][0])
                    break
            if self.points == 0:
                if self.hand[0][0] == self.hand[1][0] == self.hand[2][0] == self.hand[3][0]:
                    self.points = 8
                    self.hce1 = self.VALUES.index(self.hand[0][0])
                    self.hce2 = self.VALUES.index(self.hand[4][0])
                elif self.hand[1][0] == self.hand[2][0] == self.hand[3][0] == self.hand[4][0]:
                    self.points = 8
                    self.hce1 = self.VALUES.index(self.hand[1][0])
                    self.hce2 = self.VALUES.index(self.hand[0][0])
                elif self.hand[0][0] == self.hand[1][0] == self.hand[2][0] and self.hand[3][0] == self.hand[4][0]:
                    self.points = 7
                    self.hce1 = self.VALUES.index(self.hand[0][0])
                    self.hce2 = self.VALUES.index(self.hand[3][0])
                elif self.hand[0][0] == self.hand[1][0] and self.hand[2][0] == self.hand[3][0] == self.hand[4][0]:
                    self.points = 7
                    self.hce1 = self.VALUES.index(self.hand[2][0])
                    self.hce2 = self.VALUES.index(self.hand[0][0])
                elif self.hand[0][1] == self.hand[1][1] == self.hand[2][1] == self.hand[3][1] == self.hand[4][1]:
                    self.points = 6
                    self.hce1 = self.VALUES.index(self.hand[4][0])
                    self.hce2 = self.VALUES.index(self.hand[3][0])
                    self.hce3 = self.VALUES.index(self.hand[2][0])
                    self.hce4 = self.VALUES.index(self.hand[1][0])
                    self.hce5 = self.VALUES.index(self.hand[0][0])
                else:
                    for i in range(9):
                        if self.VALUES[i] == self.hand[0][0] and \
                                self.VALUES[i+1] == self.hand[1][0] and \
                                self.VALUES[i+2] == self.hand[2][0] and \
                                self.VALUES[i+3] == self.hand[3][0] and \
                                self.VALUES[i+4] == self.hand[4][0]:
                            self.points = 5
                            self.hce1 = self.VALUES.index(self.hand[4][0])
                            break
                    if self.points == 0:
                        if self.hand[0][0] == self.hand[1][0] == self.hand[2][0]:
                            self.points = 4
                            self.hce1 = self.VALUES.index(self.hand[0][0])
                            self.hce2 = self.VALUES.index(self.hand[4][0])
                            self.hce3 = self.VALUES.index(self.hand[3][0])
                        elif self.hand[1][0] == self.hand[2][0] == self.hand[3][0]:
                            self.points = 4
                            self.hce1 = self.VALUES.index(self.hand[1][0])
                            self.hce2 = self.VALUES.index(self.hand[4][0])
                            self.hce3 = self.VALUES.index(self.hand[0][0])
                        elif self.hand[2][0] == self.hand[3][0] == self.hand[4][0]:
                            self.points = 4
                            self.hce1 = self.VALUES.index(self.hand[2][0])
                            self.hce2 = self.VALUES.index(self.hand[1][0])
                            self.hce3 = self.VALUES.index(self.hand[0][0])
                        elif self.hand[0][0] == self.hand[1][0] and self.hand[2][0] == self.hand[3][0]:
                            self.points = 3
                            self.hce1 = self.VALUES.index(self.hand[2][0])
                            self.hce2 = self.VALUES.index(self.hand[0][0])
                            self.hce3 = self.VALUES.index(self.hand[4][0])
                        elif self.hand[0][0] == self.hand[1][0] and self.hand[3][0] == self.hand[4][0]:
                            self.points = 3
                            self.hce1 = self.VALUES.index(self.hand[3][0])
                            self.hce2 = self.VALUES.index(self.hand[0][0])
                            self.hce3 = self.VALUES.index(self.hand[2][0])
                        elif self.hand[1][0] == self.hand[2][0] and self.hand[3][0] == self.hand[4][0]:
                            self.points = 3
                            self.hce1 = self.VALUES.index(self.hand[3][0])
                            self.hce2 = self.VALUES.index(self.hand[1][0])
                            self.hce3 = self.VALUES.index(self.hand[0][0])
                        elif self.hand[0][0] == self.hand[1][0]:
                            self.points = 2
                            self.hce1 = self.VALUES.index(self.hand[0][0])
                            self.hce2 = self.VALUES.index(self.hand[4][0])
                            self.hce3 = self.VALUES.index(self.hand[3][0])
                            self.hce4 = self.VALUES.index(self.hand[2][0])
                        elif self.hand[1][0] == self.hand[2][0]:
                            self.points = 2
                            self.hce1 = self.VALUES.index(self.hand[1][0])
                            self.hce2 = self.VALUES.index(self.hand[4][0])
                            self.hce3 = self.VALUES.index(self.hand[3][0])
                            self.hce4 = self.VALUES.index(self.hand[0][0])
                        elif self.hand[2][0] == self.hand[3][0]:
                            self.points = 2
                            self.hce1 = self.VALUES.index(self.hand[2][0])
                            self.hce2 = self.VALUES.index(self.hand[4][0])
                            self.hce3 = self.VALUES.index(self.hand[1][0])
                            self.hce4 = self.VALUES.index(self.hand[0][0])
                        elif self.hand[3][0] == self.hand[4][0]:
                            self.points = 2
                            self.hce1 = self.VALUES.index(self.hand[3][0])
                            self.hce2 = self.VALUES.index(self.hand[2][0])
                            self.hce3 = self.VALUES.index(self.hand[1][0])
                            self.hce4 = self.VALUES.index(self.hand[0][0])
                        else:
                            self.points = 1
                            self.hce1 = self.VALUES.index(self.hand[4][0])
                            self.hce2 = self.VALUES.index(self.hand[3][0])
                            self.hce3 = self.VALUES.index(self.hand[2][0])
                            self.hce4 = self.VALUES.index(self.hand[1][0])
                            self.hce5 = self.VALUES.index(self.hand[0][0])

    def compare_with(self, other):
        pts1, pts2 = self.points, other._get_points()
        hce1_1, hce2_1 = self.hce1, other.hce1
        hce1_2, hce2_2 = self.hce2, other.hce2
        hce1_3, hce2_3 = self.hce3, other.hce3
        hce1_4, hce2_4 = self.hce4, other.hce4
        hce1_5, hce2_5 = self.hce5, other.hce5
        if pts1 == pts2:
            if hce1_1 > hce2_2:
                return self.RESULT[0]
            elif hce1_1 == hce2_1:
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
