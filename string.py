 # Assign string to variable
k = "thisisstring"
print(k)
print(type(k))

k = "Jahnavi"
k = 'Jahnavi'  # Both lines are same 

print(k)
print(type(k))

# Multi line Strings
a = """I would like to learn the web developement, 
that's why  ilearn all the basic's of python
i will try  to become a good developer"""
print(a) 

# Strings are the array's
k = "venky"
print(k[3])

# Looping through a string
for i in k:
    print(i) 

# Check string
a = "Bachelor of Technology"
print("Technology" in a)

# Lenght of the string
print(len(a))

if 'of' in a:
    print("Yes! 'of' is present in the a")

    # Slicing
    print(a[0:21])

    print(a[:4])

    print(a[-10:])

    print(a[:-1])

# Upper case
print(a.upper())

# Lower case
print(a.lower())
 
# Remove white spaces!
g = " Singles!, Mingles! "
print(g.strip())
print(g)

# Replace function
print(g.replace("S", "M"))

# Split function
print(g.split())

# Concatenation
a = "Venkatesh"
b = "Katta"
print(a + b)

print(a + " " + b)

# Format 
cat = "27"
venky = "My Roll Number is: " + cat

print(venky)

cat = 27
venky = "My Roll Number is: {}"

print(venky.format(cat))

# Multi values formatting!
a = 27
b = 56
c = 87
value = "apple cost {0}, mangoes cost {1} and kiwi cost is {2}"
print(value.format(a,b,c)