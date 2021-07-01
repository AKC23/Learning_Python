# 
# Example file for variables
#

# Declare a variable and initialize it
f = 0
# print(f)

# re-declaring the variable works
""" f = "abc"
print (f) """



# ERROR: variables of different types cannot be combined

# print("This is a string " + str(123))


# Global vs. local variables in functions

def FUNC():
    global f
    f = "XYZ"
    print (f)

FUNC()
print (f)    #this f is outside of FUNC()
 
del f 
print (f)