import axios from "axios";

const username = "jostest3";
const email = "test2@gemail.com";
const password = "passwordtest123";
const address = "test address Str, suite 123";

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

const callingAPI = async (name,email,password,address)=>{
    const data = userData(name,email,password,address);
    const dataPost = await axios.post('https://api.restful-api.dev/objects',data);
    console.log('The id of the user is: ',dataPost.data.id);
}

callingAPI(username,email,password,address)