const registratioButton = document.getElementById('registation-button');
const alreadyLogin = localStorage.getItem('userID')

if (alreadyLogin !== null){
    window.location.href = './to-do-list.html'
}
function getInputs(username,password,confirmP){
    if (password === confirmP){
        const data = {
        "name": username,
        "data":{
            "password":password,
            "tasks":{
            }
        }
    };
    return data;
    }else{
        return alert('Password does not match ');
    };
    
};


registratioButton.addEventListener('click', async () =>{
    const username = document.getElementById('name-registration');
    const passwordInput = document.getElementById('password-id');
    const confirmPassword = document.getElementById('password-confirm');
    const id = username.value.trim();
    const password = passwordInput.value.trim();
    const confirmP = confirmPassword.value.trim();

    if (!id || !password || !confirmP){
        alert('Missing fields please enter all the information requested')
        if(!id){
            username.value = ""
            username.focus();
            return;
        }
        if(!password){
            passwordInput.value = ""
            passwordInput.focus();
            return;
        }
        if(!confirmP){
            confirmPassword.value = ""
            confirmPassword.focus();
            return;
        }
        
    };
    try{
        const userInfo = getInputs(id,password,confirmP)
        if(!userInfo){
            username.value = "";
            passwordInput.value ="";
            confirmPassword.value =""
            return
        } ;
        const registerUser = await axios.post('https://api.restful-api.dev/objects',userInfo);
        localStorage.setItem('userID',registerUser.data.id);
        window.location.href = './to-do-list.html';
        alert(`User created correctly : ${registerUser.data.id}`);
    }catch (error){
        alert(`There was and error ${error}`);
    };
})