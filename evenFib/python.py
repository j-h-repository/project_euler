

def fiboEvenSum(num):

    sum = 0
    

    def run (a,b):
        
        nonlocal sum
       
        x = [a]
        y = [b]
        z = [x[0]+y[0]]
    
        if z[0] >= num:
            return 
        else:
            if z[0] % 2 ==0:
                sum = sum + int(z[0])
       
        x=[y[0]]
        y=[z[0]]
        
        run(x[0],y[0])

    run(1,2)
    print(sum)
    return sum

fiboEvenSum(1000)