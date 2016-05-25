# Python tutorial notes


# printing to console
print "hello world!"

# variables
one = 1
two = 2
three = one + two
hello = "hello"
world = "world"
helloworld= hello + " " + world
print three
print helloworld

# create list
mylist = []
mylist.append(1)
mylist.append(2)
mylist.append(3)
print(mylist[0])
print(mylist[1])
print(mylist[2])
for x in mylist:
    print x

# arithmetic operators
number = 1 + 2 * 3 / 4.0
print number
remainder = 11 % 3
print remainder
squared = 7 ** 2
cubed = 7 ** 3
print squared
print cubed
print 'Seven cubed = ', cubed
print 'Seven squared is {}'.format(squared)
even_num = [2,4,6,8]
odd_num = [1,3,5,7]
all_num = odd_num + even_num
print all_num

# string operations

print "length of hello world string is",len(helloworld)
print "index number of the letter o is",hello.index("o")

# conditions

test1 = True
test2 = "false"
if test1 and test2 == "false":
  print "test worked!"

