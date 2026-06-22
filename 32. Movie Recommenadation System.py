movies = {
    "Action": ["Avengers", "Batman", "John Wick"],
    "Comedy": ["3 Idiots", "Dhamaal", "Golmaal"],
    "Horror": ["The Conjuring", "Annabelle", "Insidious"],
    "Sci-Fi": ["Interstellar", "Inception", "The Matrix"]
}

print("Available Genres:")
for genre in movies:
    print("-", genre)

choice = input("\nEnter your favorite genre: ")

if choice in movies:
    print("\nRecommended Movies:")
    for movie in movies[choice]:
        print(movie)
else:
    print("Sorry, genre not found.")
