# Created by Daniel theProgrammer

"""Endeavoring to highlight that both the if and else conditions yield the same output which is 1, hence the sololearner cannot afford to get this answer wrong...
"""

arr = [1,2,3,4]
if arr[3]<arr[2]:
    print(1 and 0 or 1)
else:
    print(1 or 0 and 0)
print((1 and 0 or 1)==(1 or 0 and 0))