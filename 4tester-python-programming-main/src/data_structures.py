movies = ['Dune', 'Star Wars', 'Stalker', 'Blade Runner', 'Lost Highway']

last_movie = movies[-1]
movies.append('LOTR')
movies.append('Titanic')

print(len(movies))
middle_movies_range = movies[2:5]
print(middle_movies_range)

movies.insert(0, 'Top Gun 2')
print(movies)


email = ['a@example.com', 'b@example.com']
print(len(email))
print(email[0])
print(email[-1])
email.append('cde@example.com')
print(email)


friend = {
    "first_name": "Darek",
    "age": 40,
    "hobby": ["games", "movies"]
}
friend_hobbies = friend["hobby"]
print("Hobbies of my friend:", friend_hobbies)
print(f'My friend has {len(friend_hobbies)} hobbies')
friend["hobby"].append('football')
friend["married"] = True
print(friend)


