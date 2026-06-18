music = {
    "Pop": ["Shape of You", "Blinding Lights", "Levitating"],
    "Rock": ["Believer", "Thunderstruck", "Numb"],
    "Hip-Hop": ["God's Plan", "Lose Yourself", "Sicko Mode"],
    "Classical": ["Moonlight Sonata", "The Four Seasons", "Canon in D"]
}

print("Music Genres:")
for genre in music:
    print("-", genre)

choice = input("\nEnter your favorite genre: ")

if choice in music:
    print("\nRecommended Songs:")
    for song in music[choice]:
        print(song)
else:
    print("Genre not found.")
