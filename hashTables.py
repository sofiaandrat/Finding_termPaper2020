from os import listdir
from os.path import isfile, join

import numpy


def reader(f):
    data = f.read()
    separated_data = data.split("\n")
    if separated_data[-1] is '':
        separated_data.pop(-1)
    for i in range(len(separated_data)):
        separated_data[i] = separated_data[i].split(" ")
        separated_data[i] = [float(separated_data[i][0]), float(separated_data[i][1])]
    data = numpy.array(separated_data)
    return data


class Files:
    def __init__(self):
        self.files_list = [f for f in listdir('D:/курсач/songs data/бд/hash') if
                           isfile(join('D:/курсач/songs data/бд/hash', f))]
        self.hash_bd = {}

    def bd_filler(self):
        for file in self.files_list:
            f = open('D:/курсач/songs data/бд/hash/' + file, "r")
            data = reader(f)
            self.hash_bd.update({file[:-4]: data})

