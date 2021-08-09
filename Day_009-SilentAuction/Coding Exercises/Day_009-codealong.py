programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
}

# #Retrive items from a dictionary
# print(programming_dictionary["Bug"])

# #Adding new items to dictionary.
programming_dictionary["Loop"] = "The action of doing something over and over again."
# print(programming_dictionary)

#Create an emtpy dictionary
empty_dictionary = {}

# #Wipe an existing dictionary
# programming_dictionary = {}
# print(programming_dictionary)

# #edit an item in a dictionary
# programming_dictionary["Bug"] = "A moth in your computer"
# print(programming_dictionary)

# #loop through a dictionary
# for key in programming_dictionary:
#     print(key)
#     print(programming_dictionary[key])

#**********NESTING****************

# capitals = {
#     "France": "Paris",
#     "Germany": "Berlin",
# }
#
# #Nesting a list in a dictionary
# travel_log = {
#     "France":["Paris","Lille","Dijon"],
#     "Germany": ["Berlin","Hamburg","Stuttgart"]
# }

#Nesting Dctionary in a Dictionary
travel_log = {
    "France": {"cities_visited": ["Paris","Lille","Dijon"], "total_visits": 12},
    "Germany": {"cities_visted": ["Berlin","Hamburg","Stuttgart"], "total_vists": 5}
}

#nesting Dictionary in a lists
travel_log = [
    {
    "country": "France",
    "cities_visited": ["Paris","Lille","Dijon"],
    "total_visits": 12
     },
    {
    "country": "Germany",
    "cities_visted": ["Berlin","Hamburg","Stuttgart"],
    "total_vists": 5
    }
]