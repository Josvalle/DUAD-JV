const numberList = [1,2,3,4,5,6,7,8,9];
let evenList=[];

const even = (a) => a%2;

for (const i of numberList){
    checkValue = even(i)
    if (checkValue === 0){
        evenList.push(i);
    }
}

console.log(evenList)