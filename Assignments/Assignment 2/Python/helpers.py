import random

def createPartition():
    length = 250
    partition = [0] * length + [1] * length
    random.shuffle(partition)
    return partition