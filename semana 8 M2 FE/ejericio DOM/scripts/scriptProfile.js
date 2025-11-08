const userID = localStorage.getItem('userID')
const dataName = document.getElementById('data-name')
const dataEmail = document.getElementById('data-email')
const dataAddress = document.getElementById('data-address')
const closeButton = document.getElementById('close-button')
async function showdata(userID,dataName,dataEmail,dataAddress) {
    try{
    const response = await axios.get(`https://api.restful-api.dev/objects/${userID}`)
    console.log(response.data)
    dataName.textContent = response.data.name
    dataEmail.textContent = response.data.data.email
    dataAddress.textContent = response.data.data.address
    } catch(error){
        console.log('There was an error: ', error)
    }}
    


showdata(userID,dataName,dataEmail,dataAddress)

closeButton.addEventListener('click', ()=>{
    localStorage.removeItem('userID')
    window.location.href = './login-page.html'
})
