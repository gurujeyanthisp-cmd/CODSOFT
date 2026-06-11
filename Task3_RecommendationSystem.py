# Task 3 - Recommendation System
# CodeSoft AI Internship

print("Welcome to the Movie Recommendation System!")

# Movie categories
action_movies = ["Avengers", "Batman", "John Wick"]
comedy_movies = ["Mr. Bean", "Home Alone", "The Mask"]
romantic_movies = ["Titanic", "The Notebook", "La La Land"]

# Ask user preference
print("\nChoose your favorite movie type:")
print("1. Action")
print("2. Comedy")
print("3. Romantic")

choice = input("\nEnter your choice (1/2/3): ")

# Recommendation logic
if choice == "1":
    print("\nRecommended Action Movies:")
    for movie in action_movies:
        print("-", movie)

elif choice == "2":
    print("\nRecommended Comedy Movies:")
    for movie in comedy_movies:
        print("-", movie)

elif choice == "3":
    print("\nRecommended Romantic Movies:")
    for movie in romantic_movies:
        print("-", movie)

else:
    print("\nInvalid choice! Please run the program again.")
else:
    print("\nInvalid choice!")

input("\nPress Enter to exit...")
