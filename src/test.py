import pandas as pd

a = [True, False, True, False]
b=[1,2,3,4]
a = pd.DataFrame(a)
b= pd.DataFrame(b)

print(b[~a])
print(b[a])