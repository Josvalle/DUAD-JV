const submitButton = document.getElementById('submit');

const getID = ()=>{
    const id = document.getElementById('information')
    return id.value
}

const userID = getID()

async function userInformation(userID) {
    try{
        const response = await fetch(`https://jsonplaceholder.typicode.com/users/${userID}`);
        const data = await response.json();
        return data;
    } catch (error) {
        console.log(`There was an error: ${error}`)
    }
    
}

const resultsID = (data)=>{
    const divResult = document.getElementById('results')
    const name = document.createElement('p')
    const userName = document.createElement('p')
    const email = document.createElement('p')
    name.textContent = `Name: ${data.name}`;
    userName.textContent = `Username: ${data.username}`;
    email.textContent = `Email: ${data.email}`;
    divResult.appendChild(name);
    divResult.appendChild(userName)
    divResult.appendChild(email)

}

submitButton.addEventListener('click', async ()=> {
    const id = getID()
    const data = await userInformation(id);
    resultsID(data);
});