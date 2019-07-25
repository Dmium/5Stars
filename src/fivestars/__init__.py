import statistics

def translate_user_rating(user_rating, user_ratings):
    std = statistics.stdev(user_ratings)
    if std == 0:
        return 0
    return max(-3, 
        min(3,
            (user_rating - statistics.mean(user_ratings)) / std
            ))

def get_normalised_rating(normalised_user_ratings):
    return ((5 * statistics.mean(normalised_user_ratings)) / 3) + 2.5