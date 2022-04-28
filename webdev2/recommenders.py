"""Here implement movie-recommender functions"""

import random

movie_list = [
    "The Great Beauty",
    "Terminator II",
    "The God's Hand",
    "Call me by your name",
    "ARQ",
    "AMADEUS",
    "Life is Beautiful"
]

def nmf_recommender(user_query):
    "recommender based on negative matrix factorization "
    pass

def most_popular_recommender(user_query):
    pass


def cosim_recommender(user_query):
    "recommender based on cosine similarities"
    pass


def random_recommender(user_query):
    random.shuffle(movie_list)
    top3 = movie_list[:3]
    return top3


if __name__ == "__main__":
    top3 = random_recommender(user_query = {"ARQ":3, "Termiantor":4})
    print(top3)