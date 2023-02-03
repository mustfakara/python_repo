movies = [{"title": "The Shawshank Redemption", "rating": 9.2},    {"title": "The Godfather", "rating": 9.2},    {"title": "The Dark Knight", "rating": 9.0},    {"title": "The Godfather: Part II", "rating": 9.0},    {"title": "12 Angry Men", "rating": 8.9},    {
    "title": "Schindler's List", "rating": 8.9},    {"title": "The Lord of the Rings: The Return of the King", "rating": 9.0},    {"title": "Pulp Fiction", "rating": 8.9},    {"title": "The Good, the Bad and the Ugly", "rating": 8.8},    {"title": "Fight Club", "rating": 8.8}, ]


def recommend_movies(user_rating):
    recommended_movies = []
    for movie in movies:
        if movie["rating"] >= user_rating:
            recommended_movies.append(movie["title"])
    return recommended_movies


user_rating = float(input("Enter your minimum rating: "))

recommended_movies = recommend_movies(user_rating)

if recommended_movies:
    for movie in recommended_movies:
        print("- " + movie)
else:
    print("Sorry, no movies to recommend for your rating.")
