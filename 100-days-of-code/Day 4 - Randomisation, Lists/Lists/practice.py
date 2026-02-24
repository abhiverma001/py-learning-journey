#storing few states name of india in list
states_of_india = ["Uttar Pradesh", "karnataka", "Andhra Pradesh", "Bihar"]
print(states_of_india[1])    #in computer index numbers are start with 0 like uttar pradesh will be at 0 number, rest all similar way
print(states_of_india[-1])   # - start taking from last

states_of_india[0] = "UP"
print(states_of_india)

#using extend function to increase the list of state names
states_of_india.extend(["Maharastra", "Goa"])
print(states_of_india)

#there are many other data structure function. ref the python official doc and do practice.
#https://docs.python.org/3/tutorial/datastructures.html


