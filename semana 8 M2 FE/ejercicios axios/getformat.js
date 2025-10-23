import axios from "axios";

const response = await axios.get('https://api.restful-api.dev/objects')
const  listtest = response.data


listtest.forEach(i => {
    if (i.data !== null){
        console.log ( `${i.name} :  `, i.data)
    }
    
});