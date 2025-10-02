const stringSplit = function(string, splitter){
    let stringList =[''];
    let index =0;

    for (let counter = 0; counter < string.length; counter++){
        if(string.charAt(counter) === splitter){
            index++;
            stringList.push('');
        }else{
            stringList[index] += string.charAt(counter);
        }
    }
    return stringList
}

const splitTest = stringSplit('This is a test', ' ')

console.log(splitTest)