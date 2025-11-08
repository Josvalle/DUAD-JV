import axios from "axios";
const userID = 'ff8081819782e69e0199dfe9224e3220'

const getUserID = async (userID) => {
    try{
    const response = await axios.get(`https://api.restful-api.dev/objects/${userID}`)
    console.log(response.data)
    } catch(error){
        console.log('There was an error: ', error)
    }
    
}

getUserID(userID)