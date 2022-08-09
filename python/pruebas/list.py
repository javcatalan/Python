
lucky_numbers = [4,8, 13,25,26,25]
friends = ["Kevin", " Karen", "Jim", "Jim" , "Oscar", "Toby"]
friends[1] = "Jose"
print(friends[-1])
print(friends[1:])
friends.extend(lucky_numbers)
friends.append("Creed")
friends.insert(1, "Kelly")
friends.remove("Oscar")
friends.pop()
print(friends.index("Toby"))
print(friends.count("Jim"))
print(friends)
lucky_numbers.sort()
print(lucky_numbers)
lucky_numbers.reverse()
print(lucky_numbers)

friends2 = friends.copy()
print(friends2)