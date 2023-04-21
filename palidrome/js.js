function largestPalindromeProduct(n) {

    let one = ""
    let two = ""
    let min = "1"
    let mult1 = ""
    let mult2 = ""
    let place1 = ""
    let largest = 0
  
    const reset = ()=>{
      console.log("reset called")
      mult2 = place1
    }
  
    const check = ()=>{
      one = mult1*mult2
      if(one > 0){
        one = one.toString().split("")
        two = [...one]
        one = one.join("")
        two = (two.reverse()).join("")
        if(one == two){
          console.log(mult1, " * ", mult2, " = ", one)
          if(one > largest){
            largest = parseInt(one.toString())
          }
          
          
        } 
      }
      
    }
  
    
  
    const decre2 = ()=>{
      for(let i=place1; i>mult1/2;i--){
        mult2-=1;
        if(mult2%10==0){
          mult2-=1
        }else{
          check()
        }
      }
      reset()
    }
  
    const decre1 = ()=>{
      for(let i=0; i<mult1; i++){
        mult1-=1;
        if(mult1%11==0){
          decre2()
        }
      }
    }
  
    const run = ()=>{
        for(let i=0; i<(place1/11);i++){
          decre1()
        }
    }
  
    for(let i=1; i<n; i++){
      min+="0"
    }
    min = parseInt(min)
   
  
    for (let i=0; i<n; i++){
     
      (mult1 +="9");
      (mult2 +="9")
      
    }
    place1 = parseInt(mult1.slice(0,))
    mult1 = parseInt(mult1)
    console.log(mult1)
    mult2 = parseInt(mult2)
    console.log(mult2)
   
  
   run()
  
  console.log(largest)
  ///this works so far. add a validator to ensure the function does not run all the way through and instead stops when it notices the values are the highest possible
  
  }
  
  largestPalindromeProduct(3);