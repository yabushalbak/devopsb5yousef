# Suppose you have a box containing 28 colored 
# pencils,  and you want to divide them evenly 
# among 5 friends so that each friend gets 
# the same number of pencils.
# also find out how many pencils will be left to you

box_of_pencils = 28
num_of_friends = 5

split_pencils = box_of_pencils//num_of_friends

print("Each friend will recieve", split_pencils, "pencils each.")

your_pencils = box_of_pencils%num_of_friends

print("You get", your_pencils, "pencils.")

#Instructor solution

# Suppose you have a box containing 28 colored 
# pencils,  and you want to divide them evenly 
# among 5 friends so that each friend gets 
# the same number of pencils.
# Find out how many pencil each friend will get and 
# also find out how many pencil will be left to you.

num_pencils, num_friends = 28, 5

pencil_per_friend = num_pencils // num_friends

print("Each friend will get",pencil_per_friend,"pencils.")

left_over_pencils = num_pencils % num_friends

print("I will be left with",left_over_pencils,"pencils.")