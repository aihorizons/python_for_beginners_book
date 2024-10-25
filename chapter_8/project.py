# Project: Movie Watchlist (Storing Data Using Files)

# Step 1: Define the watchlist
watchlist = []
 
# Step 2: Define a function to add movies to the watchlist
def add_movie(movie):
    watchlist.append(movie)
    print(f"{movie} has been added to your watchlist.")
 
# Step 3: Define a function to view the watchlist
def view_watchlist():
    if watchlist:
        print("Your watchlist:")
        for movie in watchlist:
            print(f"- {movie}")
    else:
        print("Your watchlist is empty.")
 
# Step 4: Define a function to save the watchlist to a file
def save_watchlist(filename):
    with open(filename, "w") as file:
        for movie in watchlist:
            file.write(f"{movie}\n")
    print(f"Your watchlist has been saved to {filename}.")
 
# Step 5: User input to add movies and save the watchlist
while True:
    action = input("Enter 'add' to add a movie, 'view' to view the watchlist, 'save' to save the watchlist, or 'quit' to exit: ")
    
    if action == "add":
        movie = input("Enter the movie title: ")
        add_movie(movie)
    elif action == "view":
        view_watchlist()
    elif action == "save":
        filename = input("Enter the filename to save the watchlist: ")
        save_watchlist(filename)
    elif action == "quit":
        break
    else:
        print("Invalid action. Please try again.")
