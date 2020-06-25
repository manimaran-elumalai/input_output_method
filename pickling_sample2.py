import pickle

movie_name = ('Alai Payudhey',
              'AR Rahman',
              '1997',
              ((1, "Alai Paydhey Kanna"),
               (2, "Enrenrum Punnagai"),
               (3, "Evano Oruvan Vasikkiran"),
               (4, "Kadhal Sadugudu"),
               (5, "Pachai Niramey"),
               (6, "September Madham")))

even = list(range(0, 20, 2))
odd = list(range(1, 12, 2))

with open('sample_pickling', 'wb') as pickled_file:
    pickle.dump(movie_name, pickled_file)
    pickle.dump(even, pickled_file)
    pickle.dump(odd, pickled_file)
    pickle.dump(140608, pickled_file)

with open('sample_pickling', 'rb') as pickled_file:
    movie_name1 = pickle.load(pickled_file)
    even_list = pickle.load(pickled_file)
    odd_list = pickle.load(pickled_file)
    cdm = pickle.load(pickled_file)

print(movie_name1)

album, musician, year, track_list = movie_name1

print("Movie Name: ", album)
print("Music By: ", musician)
print("Year Released: ", year)
for track in track_list:
    track_number, track_title = track
    print(track_number, " : ", track_title)

print('---' * 15)

for i in even_list:
    print(i)

print('---' * 15)

for i in odd_list:
    print(i)

print('---' * 15)

print(cdm)