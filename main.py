import const
from const import BaseWord
import test
from test import *
from data import *

def main():
    refresh_screen()

    load()
    init_wordpool()

    SIIIter = SequentialIndexIterator(const.SequentialIndexRec, len(wordlist))
    RndIter = RandomIndexIterator(const.SequentialIndexRec, len(wordlist))
    RevIter = ReviseIndexIterator()

    print('-' * 40)
    key = input("What would you like to do next? :")
    last_Session = Sequential_Session
    last_iter = SIIIter

    next_seq = test.next_seq
    stat = -1

    while key != 'q':
        print('-' * 40)
        if key in {'c', 'y'}:
            refresh_screen()
            stat, next_seq = last_Session(last_iter, prev = next_seq)
        if key == 'seq':
            refresh_screen()
            stat, next_seq = Sequential_Session(SIIIter, prev = next_seq)
            last_Session = Sequential_Session
        if key == 'rev':
            refresh_screen()
            stat, next_seq = Random_Session(RevIter, prev = next_seq)
            last_Session = Random_Session

        if stat == 0:
            save()
            print('-' * 40)
            stat = -1
        key = input("What would you like to do next? :")

    print('-' * 40)
    print('Thanks for using!\n')



if __name__ == '__main__':
    main()