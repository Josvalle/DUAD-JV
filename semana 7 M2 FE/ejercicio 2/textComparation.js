const fs = require('fs');

fs.readFile('firstText.txt', 'utf8', (err, firstdata) => {
    
    fs.readFile('secondText.txt', 'utf8', (err, seconddata) => {
        
        const firstWords = firstdata.split(/\r?\n/);
        const secondWords = seconddata.split(/\r?\n/);
        let repeatWords = firstWords.filter(i => secondWords.includes(i));
        const newFrase = repeatWords.join(' ')
        console.log(newFrase)
});
});