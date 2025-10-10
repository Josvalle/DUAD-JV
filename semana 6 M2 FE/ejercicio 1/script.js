const addButton = document.getElementById('add-item')

const addItem = ()=> {
    const item = document.createElement('li')
    item.innerHTML = 'Add ramdon item'
    const list = document.getElementById('list-items')
    list.appendChild(item)

}

addButton.addEventListener('click', addItem)

const removeButton = document.getElementById('clear-list')

const removeItem = ()=> {
    
    const list = document.getElementById('list-items')
    list.innerHTML = 'Ramdon item'
}

removeButton.addEventListener('click', removeItem)