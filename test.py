import random
import queue
import copy

import const
from const import BaseWord
from data import *
from getchar import getch

word_pool = []
word_pool_weight = []

next_seq = []
SIIIter = None
RndIter = None
RevIter = None

def get_current_char(seq):
    inf = getch()

    while not inf in seq + ['q']:
        if inf == 's':
            print()
            save()
        
        inf = getch()

    return inf

def init_wordpool():
    global SIIIter, RndIter, RevIter

    SIIIter = SequentialIndexIterator(const.SequentialIndexRec, len(wordlist))
    RndIter = RandomIndexIterator(const.SequentialIndexRec, len(wordlist))

    RevIter = ReviseIndexIterator()

    word_pool.clear()
    word_pool_weight.clear()
    for word in wordlist:
        if word.suc_count != word.tot_count or word.tot_count == 0:

            word_pool.append(word)
            word_pool_weight.append(1 + (word.tot_count - word.suc_count) * 2)

        if word.suc_count == 0 and word.tot_count != 0:
            next_seq.append(word)


def Sequential_Session(
    indexIter,
    prev = None,
    total = const.WORD_PER_UNIT
    ):

    if prev != None:
        word_seq = prev
    else:
        word_seq = []

    rev_count = min(random.randint(10, 15) - len(word_seq), 3)
    Rev = iter(RevIter)
    for _ in range(rev_count):
        word_seq.append(next(Rev))

    SII = iter(indexIter)
    while len(word_seq) < total:
        word_seq.append(wordlist[next(SII)])
    random.shuffle(word_seq)

    next_seq = []

    print('-' * 40)
    refresh_screen()
    print('Current Position: ', const.SequentialIndexRec, '/', len(wordlist), '\n')

    refresh_count = 0
    for word in word_seq:
        refresh_count += 1
        if refresh_count > const.Refresh_Word_Count:
            refresh_screen()
            refresh_count = 0

        print(word)
        
        inf = get_current_char(['y', 'n'])

        print(word.trans)

        if inf == 'y':
            inf = get_current_char(['m', 'u'])
        else:
            get_current_char(['g'])

        if inf in ('n', 'u'):
            next_seq.append(word)
            word.tot_count += 1
            print('N\n')
        elif inf == 'm':
            word.suc_count += 1
            word.tot_count += 1
            print('Y\n')
        elif inf == 'q':
            print('\nQuitting current session...\n')
            return (1, prev)

    if len(next_seq) > 0:
        print('The word(s) you need to revise include(s):')
        for word in next_seq:
            print(word.name, ' ', word.trans)
    else:
        print('You get everything right. Grats!')
    
    print()

    const.SequentialIndexRec = SII.index
    
    print('Current Position:', const.SequentialIndexRec, '/', len(wordlist))
    return (0, next_seq)

def Random_Session(
    indexIter,
    prev = None,
    total = const.WORD_PER_UNIT
    ):

    if prev != None:
        word_seq = prev
    else:
        word_seq = []

    Rev = iter(RevIter)
    while len(word_seq) < total:
        word_seq.append(next(Rev))
    random.shuffle(word_seq)

    next_seq = []

    print('-' * 40)
    refresh_screen()

    refresh_count = 0
    for word in word_seq:
        refresh_count += 1
        if refresh_count > const.Refresh_Word_Count:
            refresh_screen()
            refresh_count = 0

        print(word)
        
        inf = get_current_char(['y', 'n'])

        print(word.trans)

        if inf == 'y':
            inf = get_current_char(['m', 'u'])
        else:
            get_current_char(['g'])

        if inf in ('n', 'u'):
            next_seq.append(word)
            word.tot_count += 1
            print('N\n')
        elif inf == 'm':
            word.suc_count += 1
            word.tot_count += 1
            print('Y\n')
        elif inf == 'q':
            print('\nQuitting current session...\n')
            return (1, prev)

    if len(next_seq) > 0:
        print('The word(s) you need to revise include(s):')
        for word in next_seq:
            print(word.name, ' ', word.trans)
    else:
        print('You get everything right. Grats!')
    
    print()
    
    return (0, next_seq)


class SequentialIndexIterator():
    def __init__(self, index, size):
        self.size = size
        self.index = index

    def __iter__(self):
        return self

    def __next__(self):
        self.index = (self.index + 1) % self.size
        return self.index


class RandomIndexIterator():
    def __init__(self, index, size = const.WORD_PER_UNIT):
        self.index = index
        self.size = size

    def __iter__(self):
        return self 

    def __next__(self):
        ans = random.randint(self.index, self.size)
        return ans

class ReviseIndexIterator():
    #returns object
    # def __init__(self):
    #     self.size = size

    def __iter__(self):
        return self 

    def __next__(self):
        ans = random.choices(word_pool, weights=word_pool_weight)[0]
        return ans


# def Revision_Iter():

# def Random_Iter():
