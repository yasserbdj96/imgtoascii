# EXAMPLES :
#s
from imgtoascii import imgtoascii

# Example:1
imgtoascii("test.png").view()

# Example:2
p1=imgtoascii("test.png",False).view()

for i in range(len(p1)):
    print(p1[i])
#e
