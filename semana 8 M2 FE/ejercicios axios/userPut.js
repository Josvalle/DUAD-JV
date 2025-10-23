import axios from "axios";

const userID = 'ff8081819782e69e0199dfe9224e3220'
const newAddress = '205 st new york ave, suite 100'

async function userData(userID, address ){
    try{
        
    const response = await axios.get(`https://api.restful-api.dev/objects/${userID}`)
    const userInfo = response.data
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

const callingAPI = async (userID,address)=>{
    try{
        const data = await userData(userID,address);
        
        const dataPost = await axios.put(`https://api.restful-api.dev/objects/${userID}`,data);
        console.log('Modification made: ',dataPost.data);
        } catch (error){
            console.log('Error happened: ',error)
        }
    
}

callingAPI(userID,newAddress)