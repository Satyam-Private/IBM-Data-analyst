#lists in python 
#list is a collection of items in a particular order 
#list is mutable 

first_list = [1 , 2 , 3 , 4 , 5]
print(first_list)

#accessing elements in a list 
print(first_list[0])

#negative indexing
print(first_list[-1])
 
#opeations on list 
#add elements to a list 
first_list.append([11 ,33 ,22])
print(first_list)

#insert elements at a particular index
first_list.insert(2 , 100)
print(first_list)