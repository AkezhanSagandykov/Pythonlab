movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]
def above(movie):
    for i in movies:
        if i["name"] == movie:
            if i["imdb"] > 5.5:
                return True
            else:
                return False
def sublist(movies):
    new_list = []
    for i in range(0, 15):
        dic = movies[i]
        if dic["imdb"] > 5.5:
            new_list.append(dic["name"])
    return new_list
def name(name):
    for i in movies:
        if i["category"] == name:
            print(i["name"])
def average_score_movies(movies):
    average = 0
    for i in movies:
        average = average + i["imdb"]
    return average / 15
def average_score_categories(category):
    average = 0
    counter = 0
    for i in movies:
        if i["category"] == category:
            counter = counter + 1
            average = average + i["imdb"]
    return average / counter