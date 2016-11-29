# this program finds multiples of 3 and 5 and sums them within a range
# this will be our list we pull from
multiple = []

# this prompt explains the program and asks for an input to define the range.
print "This will show the sum of multiples of 3 or 5 from 1 up to a certain number."
upto = int(raw_input("Please enter that number: "))

# this block uses modulo to find the multiples and add them to the list
for i in range(1, upto):
    if i % 3 == 0 or i % 5 == 0:
        multiple.append(i)

# this is a variable for the next block so we can actually print the multiples.
x = 1

# this block prints all of the multiples of 3 and 5 in the range
print "The multiples of 3 and 5 in this range are: "
for i in multiple:
    print x, ". ", i
    x += 1

# this computes the total of the list, then we return it below.
total = sum(multiple)

print "The sum of all of these multiples is: ", total
