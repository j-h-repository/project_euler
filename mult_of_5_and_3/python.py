### Find the sum of all the multiples of 3 or 5 below the provided parameter value number.
import math as m

def run(number):
    sum = 0

    targets = [3,5]

   
    #find the number of multiples of targets[0]
    c3 =m.floor((number-1)/targets[0])
    #print("number of multiples for " +str(targets[num]) + ": " + str(c))
    a3 = ((((c3-1)*.5)+1)*c3)*targets[0]
    #print("a3", m.floor(a3/15))
    print("a3", a3)
    #find all that is divisible by targets[1] within the number
    c5 = m.floor((number-1)/targets[1])
    a5 = ((((c5-1)*.5)+1)*c5)*targets[1]
    #print("a5", m.floor(a5/15))
    print("a5",a5)
    c15 = c5 = m.floor((number-1)/15)
    print("c15f3",c15)
    a15 = ((((c15-1)*.5)+1)*c15)*15
    print("a15", a15)
 
    sum = a5+a3-a15

    print(sum)

run(8456)




#test1(1000)

    #if a number is provided
        #divide the number by 3 and grab the rounded down number
            #store the rounded down number
        #divide the number by 5 and grab the rounded down number
            #store the rounded down number


            #e.g run (97)

                # 97/3 ==> 32.3 ==> 32
                    #sum off all 3 * n
                        #instead of (3*1) + (3*2)+ (3*3) +....(3*32) 

                        #im predicting that 3 32 times will have a sum of 
                        # 3 * (3 + )