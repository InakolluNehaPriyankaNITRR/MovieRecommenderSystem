
import numpy as np
import pandas as pd

ratings = pd.read_csv('ratings1.csv')
#print(ratings.info)


#rm[a][b] is rating matrix in which a->movie_id & b->user_id
rm =np.ndarray(shape=(100001,944), dtype=float)
data = np.genfromtxt('ratings1.csv',delimiter=',')
print("rating matrix starts here")
for i in range(1,10000):  
    x=data[i][0]
    y=data[i][1] 
    z=data[i][2]
    b = int(x)
    a = int(y)
    
    rm[a][b]=z
print(rm[23][1])
print(rm[1][1])
print(rm[12][1])
print(rm[25][1])
print(rm[15][1])
print(rm[13][1])
print(rm[7][1])
print(rm[14][1])
print(rm[9][1])
print(rm[50][1])
#[23  1 12 25 15 13  7 14  9 50]
print("rating matrix ends here")   
