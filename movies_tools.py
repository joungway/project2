

# csv_file = open("movies_clean.csv", "w")
# writer=csv.writer(csv_file, delimiter=',')
#
# for row in table:
#     writer.writerow(row)
#
# csv_file.close()

class Movie(object):

    def __init__(self, list):
       self.title = list[0]
       self.rating = list[14]

    def __str__(self):
       return "{}  |  {}".format(self.title, self.rating)

# def count_movie(input_file):
#     count=0
#     row_counter=csv.reader(input_file)
#
# ins1 = Movie("Slam", R)
# barclays = Bank("Wilson", NA)
# bank_of_china = Bank("3 Ninjas Kick Back", PG)
