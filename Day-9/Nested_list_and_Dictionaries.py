capitals = {
    "France": "paris",
    "Germany": "Berlin",
}

# Nested List in Dictionary

# travel_log = {
#     "France": ["Paris", "Lille","Dijon"],
#     "Germany": ["stuttgart","Berlin"],
# }

# print lille

#print(travel_log["France"][1])

nested_list = ["A","B",["C","D","E"],"F"]
#print(nested_list[2][2])


travel_log = {
    "France":{
        "Paris":["Berlin","Lille","Dijon"],
        "total_visits":12
    },
    "Germany":{
        "cities":["Berlin","Hamburg","stuttgart"],
        "total_visits":5
    }
}

print(travel_log["France"]["Paris"][1])
print(travel_log["Germany"]["cities"][1])