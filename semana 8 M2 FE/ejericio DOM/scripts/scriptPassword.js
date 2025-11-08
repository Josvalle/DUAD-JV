const changeButton = document.getElementById('password-button')

async function userData(userID){
    try{
        const response = await axios.get(`https://api.restful-api.dev/objects/${userID}`)
        return response.data
    } catch(error){
        alert(`There was an error: ${error}` )
    }
}

function checkMatchInformation(userInfo,password,newP,confirmP){
    if (userInfo.data.password === password && newP === confirmP){
        try{
            const changeData = {
                "name":userInfo.name,
                "data":{
                    "email": userInfo.data.email,
                    "password":newP,
                    "address": userInfo.data.address
                    }
                    
                    }
                    return changeData
            }catch (error){
                alert(`There was an error: ${error}`)
                            }
    }else{
        return alert('Current password incorrect or new password do not match with confirm password')
    }
}

changeButton.addEventListener('click', async ()=>{
    const userID = document.getElementById('userID')
    const currentPassword = document.getElementById('old-password');
    const newPassword = document.getElementById('new-password');
    const confirmPassword = document.getElementById('confirm-password');
    const id = userID.value.trim();
    const password = currentPassword.value.trim()
    const newP = newPassword.value.trim()
    const confirmP = confirmPassword.value.trim()
    
    if (!id || !password || !newP || !confirmP){
        alert('Please fill all fields')
        (!id ? userID : (!password ? currentPassword : (!newP ? newPassword : confirmPassword))).focus();
        return console.error('Fills all fields');
        ;
    }
    try{
        const userInfo = await userData(id);
        if(!userInfo) return;
        const returnData = checkMatchInformation(userInfo,password,newP,confirmP);
        if(!returnData) return;
        const updataPassword = await axios.put(`https://api.restful-api.dev/objects/${id}`,returnData)
        alert('Password change successfully')
        window.location.href = './login-page.html'
    }catch (error){
        alert(`An Error happen ${error}`)
    }
})