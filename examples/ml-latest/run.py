import csv
import fivestars
import statistics
userdata = {}
moviedata = {}
i = 0
with open('ratings.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        i += 1
        if int(row['userId']) not in userdata:
            userdata[int(row['userId'])] = []
        userdata[int(row['userId'])].append(float(row['rating']))
        if int(row['movieId']) not in moviedata:
            moviedata[int(row['movieId'])] = []
        moviedata[int(row['movieId'])].append((int(row['userId']), float(row['rating'])))
        if i > 1000000:
            break
totaldiff = 0
totaldiffabs = 0
count = 0
for movie in moviedata:
    normalised_user_ratings = []
    ratings = []
    for rating in moviedata[movie]:
        ratings.append(rating[1])
        user_ratings = []
        if len(userdata[rating[0]]) > 1:
            for user_rating in userdata[rating[0]]:
                user_ratings.append(user_rating)
            normalised_user_ratings.append(fivestars.translate_user_rating(rating[1], user_ratings))
    normrating = fivestars.get_normalised_rating(normalised_user_ratings)
    meanrating = statistics.mean(ratings)
    print('normrating', normrating)
    print('meanrating', meanrating)
    totaldiff += (normrating - meanrating)
    totaldiffabs += (abs(normrating - meanrating))
    count += 1
    if count > 100:
        break
print('average difference is', totaldiff / count)
print('abs average difference is', totaldiffabs / count)
