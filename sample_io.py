print ("****************************\nTo work on input output with external files \n*****************************")
#my_file = open('io_file.txt')
my_file = open('io_file.txt', 'a+')

my_file.write('\nAppending an another line at the bottom')
my_file.seek(0)
contents = ( my_file.read() )

with open ('io2_file.txt', mode='w') as z:
     z.write('I am adding an new line in a new file') 

with open ('io2_file.txt', mode='r') as z:
     print(z.read()) 

#print ( contents )

print ('\n') 