DATA_FILE_NAME = 'data.csv'
VOCAB_FILE_NAME = 'vocab.csv'
RECORD_FILE_NAME = 'record.ini'

SequentialIndexRec = -1

WORD_PER_UNIT = 16
WORD_FROM_POOL_IF_NOT_EXIST = 3
MINIMUM_SAMPLING_WITH_REPLACEMENT_SIZE = 10

Refresh_Word_Count = 8

class BaseWord(object):
    def __init__(self, **kwargs):
        self.name = kwargs['name']
        self.trans = kwargs['trans']

        self.suc_count = int(kwargs['suc_count'])
        self.tot_count = int(kwargs['tot_count'])

    def __repr__(self):
        return self.name