const loginButton = document.getElementById('login-button')
const alreadyLogin = localStorage.getItem('userID')

if (alreadyLogin !== null){
    window.location.href = './my-profile.html'
}
async function userData(userID){
    try{
        const response = await axios.get(`https://api.restful-api.dev/objects/${userID}`)
        return response.data
    } catch(error){
        alert(`There was an error: ${error}` )
    }
}

function compareData(userInfo,inputID,password){
    if (inputID === userInfo.id && password=== userInfo.data.password){
        alert('Login succesfull')
        localStorage.setItem('userID',inputID)
        window.location.href = './my-profile.html'
    } else{
        alert('Incorrect user or password please try again ')
    }
}

loginButton.addEventListener('click', async ()=>{
    const userID = document.getElementById('user-login')
    const password = document.getElementById('password-id')
    const id = userID.value.trim();
    const pwd = password.value.trim();
    if (!id || !pwd){
        alert('Please fill both fields');
        (!id ? userID : password).focus();
        return;
    }
    try{
        const userInfo = await userData(id)
        compareData(userInfo,id,pwd)
        } catch (error){
            alert(`An error ocurs: ${error}`)
        }
    
})