async function userInformation(userID) {
    try{
        const response = await fetch(`https://reqres.in/api/users/${userId}`);
        const data = await response.json();
    } catch (error) {
        console.log(`There was an error: ${error}`)
    }
    
}

const id = 23;
userInformation(id);
