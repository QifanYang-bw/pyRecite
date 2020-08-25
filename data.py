import csv
import os
from codecs import open
import configparser

import const
from const import BaseWord

wordlist = []
worddict = {}

def refresh_screen():
    print("\033[H\033[J", end = '')

def loadrecord():
    print('Loading info file...')

    config = configparser.ConfigParser()
    
    config.sections()
    config.read(const.RECORD_FILE_NAME)

    const.SequentialIndexRec = int(config['Sequential']['SequentialIndexRec'])

    const.WORD_PER_UNIT = int(config['Sequential']['WORD_PER_UNIT'])
    const.WORD_FROM_POOL_IF_NOT_EXIST = int(config['Sequential']['WORD_FROM_POOL_IF_NOT_EXIST'])
    const.MINIMUM_SAMPLING_WITH_REPLACEMENT_SIZE = int(config['Sequential']['MINIMUM_SAMPLING_WITH_REPLACEMENT_SIZE'])

    const.Refresh_Word_Count = int(config['General']['Refresh_Word_Count'])

    print('Info file loaded.')

def saverecord():
    print('Generating info file...')

    config = configparser.ConfigParser()
    config['Sequential'] = {}
    config['Sequential']['SequentialIndexRec'] = str(const.SequentialIndexRec)

    config['Sequential']['WORD_PER_UNIT'] = str(const.WORD_PER_UNIT)
    config['Sequential']['WORD_FROM_POOL_IF_NOT_EXIST'] = str(const.WORD_FROM_POOL_IF_NOT_EXIST)
    config['Sequential']['MINIMUM_SAMPLING_WITH_REPLACEMENT_SIZE'] = str(const.MINIMUM_SAMPLING_WITH_REPLACEMENT_SIZE)

    config['General'] = {}
    config['General']['Refresh_Word_Count'] = str(const.Refresh_Word_Count)

    with open(const.RECORD_FILE_NAME, 'w') as configfile:
        config.write(configfile)

    print('Info file generated.')

def load():
    print('Loading data file...')

    if not os.path.exists(const.DATA_FILE_NAME):
        print('Record file not found.')

        if os.path.exists(const.VOCAB_FILE_NAME):
            createdata()
        else:
            raise FileNotFoundError()

    with open(const.DATA_FILE_NAME, encoding="utf-8") as csvfile:
        '''Read csv file'''
        datareader = csv.reader(csvfile, delimiter=',') 

        count = 0
        for row in datareader:
            count += 1
            wordlist.append(BaseWord(
                name = row[0],
                trans = row[1],
                suc_count = row[2],
                tot_count = row[3]
            ))
            worddict[row[0]] = len(wordlist) - 1

    print(
        'Data file successfully loaded with ' + \
        str(count) + \
        ' words.'
    )

    if not os.path.exists(const.RECORD_FILE_NAME):
        print('Record info file not found.')
        saverecord()

    loadrecord()


def createdata():
    print('Creating data based on vocabulary file...')

    with open(const.VOCAB_FILE_NAME, encoding="utf-8") as csvfile:
        '''Read csv file'''
        vocabreader = csv.reader(csvfile, delimiter=',')    

        with open(const.DATA_FILE_NAME, 'w', encoding="utf-8") as csvfile:
            datawriter = csv.writer(csvfile, delimiter=',')

            for row in vocabreader:
                datawriter.writerow([row[0], row[1], 0, 0])

    print('Data file created.')


def save():
    print('Saving...')
    with open(const.DATA_FILE_NAME, 'w', encoding="utf-8") as csvfile:
        datawriter = csv.writer(csvfile, delimiter=',')

        for word in wordlist:
            datawriter.writerow([
                word.name,
                word.trans,
                word.suc_count,
                word.tot_count
            ])
    saverecord()
    print('Saving Complete.')