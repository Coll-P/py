#empty list
my_list=list()
#appendingvalues to my_list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

#appended list
print(f'The new list is {my_list}')

 #inserting 15 at position 2
my_list.insert(2,15)
print(f'The new list after inserting 15 is {my_list}')


#extending
new_list=[50,60,70]
my_list.extend(new_list)
print(f'The new extended list is {my_list}')


#removing last item
my_list.pop()
print(f'The new list after removing last item  {my_list}')



#sorting
my_list=sorted(my_list)
print(f'The new sorted list is {my_list}')


#possition of 30
print(f'The position of 30 is {my_list.index(30)}')