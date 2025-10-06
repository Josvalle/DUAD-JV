const yesRadio = document.getElementById("yes-id");
const noRadio = document.getElementById("no-id");
const infoForm = document.getElementById('page-form');

yesRadio.addEventListener('change',()=>{
        const employeeInput = document.createElement('input');
        employeeInput.id = 'new-input';
        employeeInput.placeholder = 'Enter your Job title';
        employeeInput.type = 'text';
        infoForm.appendChild(employeeInput)
    
});

noRadio.addEventListener('change',()=>{
    const checkNewInput = document.getElementById('new-input')
    if (checkNewInput){
        infoForm.removeChild(checkNewInput)
    }
})