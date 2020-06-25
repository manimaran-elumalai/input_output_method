#  using pickle saving objects is very easy

import pickle

# movie_name = ('Alai Payudhey',
#               'AR Rahman',
#               '1997',
#               ((1, "Alai Paydhey Kanna"),
#                (2, "Enrenrum Punnagai"),
#                (3, "Evano Oruvan Vasikkiran"),
#                (4, "Kadhal Sadugudu"),
#                (5, "Pachai Niramey"),
#                (6, "September Madham")))
#
# with open('movie_name', 'bw') as movie_file:
#     pickle.dump(movie_name, movie_file)

with open('movie_name', 'br') as pickled_movie_file:
    movie_name1 = pickle.load(pickled_movie_file)

print(movie_name1)

album, musician, year, track_list = movie_name1

print("Movie Name: ", album)
print("Music By: ", musician)
print("Year Released: ", year)
for track in track_list:
    track_number, track_title = track
    print(track_number, " : ", track_title )

