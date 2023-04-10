function fiboEvenSum(num) {

    let sum = 0
  
    const run = (a,b)=>{
      let x = [a]
      let y = [b]
      let z = [x[0]+y[0]]
      
      if(z>=num){
        console.log("done")
        return 
      } else{
        if(z%2==0){
          sum = sum + z[0]
        } 
        x=[...y]
        y=[...z]
        run(x[0],y[0])
      }
    }
    run(1,2)
    return sum+2
  }
  console.log(fiboEvenSum(1000))