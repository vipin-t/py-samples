# print ("to work on lists")

a_list = [7,1,5,8,4,2,6]
b_list = ['f', 'g', 'a', 'd', 'b', 'e', 'c']
c_list = [a_list, b_list]

b_list.   
## list commands

# a_list.sort()
# a_list.reverse()
# b_list.sort()

print ( a_list )
print(b_list)
print ('\n')
print ( c_list )

#print ( b_list.pop(2) )
# print ( len(a_list) )
# print ( a_list + b_list  )

## using dictionary. This uses key:value pair and used when we dont have any ordering or indexing.. Just retrieves the value based on the key
print ("to work on Dictionary")
new_dictionary = {'apples': 20, 'mango': 40, 'orange': 10, 'banana': 80}
my_dictionary = {'key1':123,'key2':[12,23,33],'key3':['item0','item1','item2']}

print (new_dictionary) 
print (my_dictionary['key3'][2])


## tuple similar to list.. but not immutable.. i.e., the values are fixed and cannot be changed after they are defined.
## tuple(*,*,*) ... list[*,*,*]... dictionary {key:value, key:value, key:value}

_tuple1 = ('phy', 'chem', 'bio', 'math')
print (_tuple1)
print (_tuple1.count('phy'))