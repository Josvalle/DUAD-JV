const submitButton = document.getElementById('submit');

const showInfo = ()=> {
    const info = document.getElementById('box-info');
    const oldP = document.getElementById('information')
    oldP.textContent = info.value
    info.value = '';
    
};

submitButton.addEventListener('click', showInfo);