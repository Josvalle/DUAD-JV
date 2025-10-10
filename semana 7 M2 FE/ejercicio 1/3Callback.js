function oddOrNot(number,pairCallback,oddCallback){
    if (number%2===0){
        pairCallback()
    }else{
        oddCallback()
    }
}

oddOrNot(2,() => {
    console.log('The number is pair');
}, ()=>{
    console.log('The number is odd')
})