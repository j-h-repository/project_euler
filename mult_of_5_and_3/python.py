### Find the sum of all the multiples of 3 or 5 below the provided parameter value number.
import math as m

def run(number):
    sum = 0

    targets = [3,5]

    c3 =m.floor((number-1)/targets[0])
    
    a3 = ((((c3-1)*.5)+1)*c3)*targets[0]
    
    c5 = m.floor((number-1)/targets[1])
    
    a5 = ((((c5-1)*.5)+1)*c5)*targets[1]
  
    c15 = c5 = m.floor((number-1)/15)
  
    a15 = ((((c15-1)*.5)+1)*c15)*15

 
    sum = a5+a3-a15

    print(sum)

run(8456)




 
