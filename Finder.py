from hashTables import reader
from target_zone import Cutter


class Finder:
    def __init__(self, src, bd):
        f = open(src, "r")
        self.hash_data = reader(f)
        smth = Cutter(self.hash_data)
        smth.cut_and_create_target()
        self.target_data = smth.get_cut_element()
        self.bd = bd
        self.target_bd = {}

    def take_targets(self):
        for name in list(self.bd.hash_bd.keys()):
            hashes = Cutter(self.bd.hash_bd[name])
            hashes.cut_and_create_target()
            self.target_bd.update({name: hashes.cut_element})

    def comparator(self):
        for song in list(self.target_bd.keys()):
            find_count = 0
            for little_target in self.target_data:
                for reference_target in self.target_bd[song]:
                    if reference_target == little_target:
                        find_count += 1
                        break
            print(song + ' ' + str((find_count / len(self.target_data)) * 100) + '%')
