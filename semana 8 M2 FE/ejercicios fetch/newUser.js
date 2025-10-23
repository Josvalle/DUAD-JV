
function userData(name,email, password,address ){
    const data = {
    "name":name,
    "data":{
        "email": email,
        "password":password,
        "address": address
    }
    }
    return data
}

async function callAPIPost(data) {
    const requestConfig = {
    method: "POST",
    headers: {
        "Content-Type": "application/json"
    },
    body: JSON.stringify(data),
};

const url = 'https://api.restful-api.dev/objects';
const response = await fetch(url, requestConfig);
const userID = await response.json();
return userID
}


const username = "jostest2";
const email = "test2@gemail.com";
const password = "passwordtest123";
const address = "test address Str, suite 123";

const callingAPI = async (name,email,password,address)=>{
    const data = userData(name,email,password,address);
    const dataPost = await callAPIPost(data);
    console.log('The id of the user is: ',dataPost.id);
}

callingAPI(username,email,password,address)