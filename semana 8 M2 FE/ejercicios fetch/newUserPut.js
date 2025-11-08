const userID = 'ff8081819782e69e0199df40dc10319d'
const newAddress = '205 st new york ave, suite 100'

async function userData(userID, address ){
    try{
        
    const response = await fetch(`https://api.restful-api.dev/objects/${userID}`)
    const userInfo = await response.json()
    const data = {
    "name":userInfo.name,
    "data":{
        "email": userInfo.data.email,
        "password":userInfo.data.password,
        "address": address
    }
    }
    return data
        } catch(error){
        console.log('There was an error: ', error)
    }
    
}


async function modifyUser(userID,data) {
    const requestConfig = {
    method: "PUT",
    headers: {
        "Content-Type": "application/json"
    },
    body: JSON.stringify(data),
};

const url = `https://api.restful-api.dev/objects/${userID}`;
const response = await fetch(url, requestConfig);
const modifyData = await response.json();
return modifyData
}

const callingAPI = async (userID,address)=>{
    try{
        const data = await userData(userID,address);
        
        const dataPost = await modifyUser(userID,data);
        console.log('Modification made: ',dataPost);
        } catch (error){
            console.log('Error happened: ',error)
        }
    
}

callingAPI(userID,newAddress)