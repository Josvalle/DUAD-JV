const button = document.getElementById('change-color');

const changePColor = ()=>{
    const text = document.getElementById('textP');
    const colorArray = ['red', 'blue', 'green', 'yellow', 'cyan', 'pink'];
    const ramdonColor = Math.floor(Math.random() * colorArray.length);
    text.className = colorArray[ramdonColor]
}

button.addEventListener('click', changePColor)