# In the farm we have 35 cows , 23 chickens,
#and 40 ducks.
# Create a program to calculate total number of 
# legs in the farm
#Requirements create a variable for 
# cows, chickens and ducks , and create variables
#for their number of legs. 
# print "We have 'result' legs in the farm"

cows = 35*4
chickens = 23*2
ducks = 40*2

result = str(cows+chickens+ducks)

print('We have ' + result + ' legs in the farm') 

# or you can also do
#   result = cows+chickens+ducks
#   print('we have', result, 'legs in the farm')
# you can do this because you are not adding them together you are
# showing them side by side and python automatically places spaces
# for you

#This is what was shown in class
# In the farm we have 35 cows , 23 chickens,
#and 40 ducks.
# Create a program to calculate total number of 
# legs in the farm
#Requirements create a variable for 
# cows, chickens and ducks , and create variables
#for their number of legs. 
# print "We have 'result' legs in the farm"

num_of_cows = 35
num_of_chickens = 23
num_of_ducks = 40

legs_of_a_cow = 4
legs_of_a_chicken = 2
legs_of_a_duck = 2

total_legs_of_chickens = legs_of_a_chicken * num_of_chickens
total_legs_of_cows = legs_of_a_cow * num_of_cows
total_legs_of_ducks = legs_of_a_duck * num_of_ducks


total_num_of_legs = total_legs_of_chickens + total_legs_of_ducks + total_legs_of_cows

print("We have", total_num_of_legs, "legs in this farm.")

#Note : Python is going to add space when comma is 
# used in print function.



# We are asked to create a program to calculate 
# average score for a student with the exam scores following:
# 1 -> 70
# 2 -> 95
# 3 -> 50 
# 4 -> 45
# Calculate the average score for the student 
# and print the average in following format. 
# Average score for given student grades is `avgScore`. 

score1 = 70
score2 = 95
score3 = 50
score4 = 45

average_score = (score1 + score2 + score3 + score4)/4

print('Average score for given student grades is', average_score)

#What is the type of variable average?
#float
# type() function
#when we put variable name in a type function it will
# show the type of a variable.
print(type(average_score))






#what we did as a class
# We are asked to create a program to calculate 
# average score for a student with the exam scores following:
# 1 -> 70
# 2 -> 95
# 3 -> 50 
# 4 -> 45
# Calculate the average score for the student 
# and print the average in following format. 
# Average score for given student grades is `avgScore`. 

exam1 = 70
exam2 = 95
exam3 = 50 
exam4 = 45

sum_exam_scores = exam1 + exam2 + exam3 + exam4 
avg = sum_exam_scores / 4
print("Average score for given student grades is", avg)

#What is the type of variable avg? 
#float
# type() function
#When we put the variable name in a type function it will 
# show the type of a variable. 
print(type(avg))