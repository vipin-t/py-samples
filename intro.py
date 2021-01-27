# print ('Introduction to Python Programming')

# print ('Introduction to Python Programming \nCoding using VS Code ')

#print [ "Introduction to Python Programming" ]
#int a
#print ( len ('Introduction to Python Programming Coding using VS Code ') )

rent = 4500
months = 36
total = ( rent * months ) / 12
print (total)

## use of special character inside print statement  such as %s, %d, %r
print ('The rent is %d for %d months and the total value is : %10.5f'%(rent, months, total) )
print ('The rent is %s for %s months and the total value is : %s'%(rent, months, total) )



## use of f-string formatting method
print (f'The rent is {rent} for {months} months and the total value is : {( rent * months ) / 12:1.4f}' )

## using format keyword
print ("The rent is {} for {} months and the total value is : {r:5.3f}".format(rent, months, r = ( rent * months ) / 12 ) )
print ("The rent is {r} for {m} months and the total value is : {t:5.3f}".format(r = rent, m = months, t = ( rent * months ) / 12 ) )




