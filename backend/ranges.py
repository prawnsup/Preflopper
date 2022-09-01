import itertools  # "22+"
import numpy as np
import warnings

warnings.filterwarnings("ignore", category=np.VisibleDeprecationWarning)


def search2d(nparray, item):
    y, x = np.where(nparray == item)
    return y[0], x[0]



def clean(strings):
    #used to format the strings, removes the + signs

    if 's' in strings:
        strings=strings[0:3]
    else:
        strings=strings[0:2]

    return strings


def processor(inp, table):
    # will clean inputs into a format suitable for searching through our data structure and returns cooardinates for cards which are searched
    inp = clean(inp)
    y, x = search2d(table, inp)
    return y, x


class ranges:
    def __init__(self, rangein):
        self.graph = np.array(
            [['AA', 'AK', 'AQs', 'AJs', 'ATs', 'A9s', 'A8s', 'A7s', 'A6s', 'A5s', 'A4s', 'A3s', 'A2s'],
             ['AK', 'KK', 'KQs', 'KJs', 'KTs', 'K9s', 'K8s', 'K7s', 'K6s', 'K5s', 'K4s', 'K3s', 'K2s'],
             ['AQ', 'KQ', 'QQ', 'QJs', 'QTs', 'Q9s', 'Q8s', 'Q7s', 'Q6s', 'Q5s', 'Q4s', 'Q3s', 'Q2s'],
             ['AJ', 'KJ', 'QJ', 'JJ', 'JTs', 'J9s', 'J8s', 'J7s', 'J6s', 'J5s', 'J4s', 'J3s', 'J2s'],
             ['AT', 'KT', 'QT', 'JT', 'TT', 'T9s', 'T8s', 'T7s', 'T6s', 'T5s', 'T4s', 'T3s', 'T2s'],
             ['A9', 'K9', 'Q9', 'J9', 'T9', '99', '98s', '97s', '96s', '95s', '94s', '93s', '92s'],
             ['A8', 'K8', 'Q8', 'J8', 'T8', '98', '88', '87s', '86s', '85s', '84s', '83s', '82s'],
             ['A7', 'K7', 'Q7', 'J7 ', 'T7', '97', '87', '77', '76s', '75s', '74s', '73s', '72s'],
             ['A6', 'K6', 'Q6', 'J6', 'T6', '96', '86', '76', '66', '65s', '64s', '63s', '62s'],
             ['A5', 'K5', 'Q5', 'J5', 'T5', '95', '85', '75', '65', '55', '54s', '53s', '52s'],
             ['A4', 'K4', 'Q4', 'J4', 'T4', '94', '84', '74', '64', '54', '44', '43s', '42s'],
             ['A3', 'K3', 'Q3', 'J3', 'T3', '93', '83', '73', '63', '53', '43', '33', '32s'],
             ['A2', 'K2', 'Q2', 'J2', 'T2', '92', '82', '72', '62', '52', '42', '32', '22']]
        )
        self.ranges = rangein
        self.c_valid=[]
    # ['22+,43s+, A2s-]
    def converter(self):  # used to generate the combinations of cards which are valid according to ranges inputed
        inp = self.ranges.split(',')
        for i in inp:
            test=i
            determiner = test[-1]
            if test[-2]=='+': # if there is two + signs e.g A4++ , only the y value is changes - its decreased by 1 each time since the higher value cards are stored above.KJ>KT

                y, x = processor(test, self.graph)
                self.c_valid.append(self.graph[y][x])

                while y != 0:
                    y=y-1
                    self.c_valid.append(self.graph[y][x])


            if determiner == "+": #if there is only 1 + sign , e.g 34s+ , both x and y value are are decreased incremently. This allows for diagonal movement upwards. J9s>87s
                y, x = processor(test, self.graph)
                self.c_valid.append(self.graph[y][x])

                while y != 0 and x != 0:
                    y = y - 1
                    x = x - 1
                    self.c_valid.append(self.graph[y][x])


            elif determiner == "-": #if there is a - sign e.g A3s- only x value is decreased incrementally. So allows for horizontal movement to the left where higher value cards are stored.A4s>A2s
                y, x = processor(test, self.graph)
                self.c_valid.append(self.graph[y][x])

                while x != 0:
                    x = x - 1
                    self.c_valid.append(self.graph[y][x])


            else:
                y,x=processor(test,self.graph)

                self.c_valid.append(self.graph[y][x])


