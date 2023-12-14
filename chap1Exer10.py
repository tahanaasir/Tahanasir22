#Exercise 10 : Film Dictionary☑️
#Create a dictionary that contains relevant data for
#films (e.g. Title, Director, etc). Display the film details using loop.

#Defining films, director name, release year and rating
films = [
    {
        "Title": "Vertigo",
        "Director": "Alfred Hitchcock",
        "ReleaseYear": 1958,
        "Rating": 9.3
    },
    {
        "Title": "The Innocnents",
        "Director": "Jack Clayton",
        "ReleaseYear": 1961,
        "Rating": 9.2
    },
    {
        "Title": "Lawrence of Arabia",
        "Director": "David Lean",
        "ReleaseYear": 1962,
        "Rating": 8.9
    },
{
        "Title": "Blade Runner",
        "Director": "Ridely Scott",
        "ReleaseYear": 1982,
        "Rating": 9.3
    },
{
        "Title": "Eyes Wide Shut",
        "Director": "Stanley Kubrick",
        "ReleaseYear": 1999,
        "Rating": 8.2
    },
{
        "Title": "Chinatown",
        "Director": "Roman Polanski",
        "ReleaseYear": 1974,
        "Rating": 7.9
    },
{
        "Title": "Boogie Nights",
        "Director": "Paul Thomas Anderson",
        "ReleaseYear": 1997,
        "Rating": 8.4
    },
{
        "Title": "Titanic",
        "Director": "James Cameron",
        "ReleaseYear": 1997,
        "Rating": 8.9
    },
{
        "Title": "Good Will Hunting",
        "Director": "Gus Van Sant",
        "ReleaseYear": 1997,
        "Rating": 7.9
    },
{
        "Title": "Avatar",
        "Director": "James Cameron",
        "ReleaseYear": 2009,
        "Rating": 9.9
    },
]

#Displaying films details by using a loop
for film in films:
    print("Title: ", film["Title"])
    print("Director: ", film["Director"])
    print("ReleaseYear: ", film["ReleaseYear"])
    print("Rating: ", film["Rating"])
    print("/n")