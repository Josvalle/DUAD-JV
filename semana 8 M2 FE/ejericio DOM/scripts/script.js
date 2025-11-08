const registerButton = document.getElementById('register-button')


function getInformation(){
    const name = document.getElementById('username')
    const email = document.getElementById('email')
    const password = document.getElementById('password')
    const address = document.getElementById('address')
    const data = {
    "name":name.value,
    "data":{
        "email": email.value,
        "password":password.value,
        "address": address.value
    }
    }
    return data
}


registerButton.addEventListener('click',async ()=>{
    try{
        const data = getInformation()
        const registerUser = await axios.post('https://api.restful-api.dev/objects',data)
        localStorage.setItem('userID',registerUser.data.id)
        window.location.href = './my-profile.html'
        alert(`User created correctly : ${registerUser.data.id}`)
        
    } catch (error){
        alert(`There was and error ${error}`);
    };
})

