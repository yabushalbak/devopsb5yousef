
    # There is 20 devops engineers in the company that should be
    # equally asssigned to each of the 8 scrum teams.
    # Find out how many devops engineers will not be assigned
    # with a team.
    # Also find out how many devops engineers will be in
    # Each scrum team.

engineers = 20
scrum_teams = 8

assigned_engineers = 1
not_assigned_engineers = 1

print (engineers % scrum_teams)

print (engineers // scrum_teams)


#Instructor Example

# In order to find number of devops engineers in each team
#divide the num of devops with the num of teams.

num_devops, num_teams = 20, 8

print("Each team will have",num_devops//num_teams,"devops engineers")

print("After the assignment there will be",num_devops%num_teams,"engineers unassigned")









