import matplotlib.pyplot as plt
year= [1950,2000,2050,2100] # Defining the list of values for X axis
pop= [3.5,3.6,3.7,3.8] #Defining list of values for Y axis
plt.plot(year,pop) #If you want this as point then use scatter where polt defined
plt.show()
print(year[-1]) #To access the last element of a regular Python list, use [-1]
print(pop[-1])
