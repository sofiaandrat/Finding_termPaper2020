from hashTables import Files
from target_zone import *
from Finder import *
if __name__ == "__main__":

    bd = Files()
    bd.bd_filler()

    song_hash_data = 'D:/курсач/songs data/три белых коня/after/DaryaLoban.txt'
    find = Finder(song_hash_data, bd)
    find.take_targets()
    find.comparator()