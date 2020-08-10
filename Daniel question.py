# Created by Daniel the programmer

print(7!=7.0) # outputs False cos 7==7.0, they are of the same value

"""however 7 is not 7.0, though same value, they are different objects, in this case we refer to different datatypes, int and float!"""

print(7 is 7.0)

#Another example
solo1 = ["Joseph", "Tomiwa", "Daniel", "Theophile"]

solo2 = ["Joseph", "Tomiwa", "Daniel", "Theophile"]
# Two different objects, though value same!!!
print(solo1==solo2) # outputs True, but

print(solo1 is solo2) # outputs False
