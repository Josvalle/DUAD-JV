const userID = localStorage.getItem('userID')
const closeSession = document.getElementById('close-user')
const newTask = document.getElementById('add-task-button')
const tbody =document.getElementById('table-body')
const completeRadio = document.getElementById('complete')
const incompleteRadio = document.getElementById('incomplete')
const noneRadio = document.getElementById('none')

async function userData(userID) {
    try{
        const response = await axios.get(`https://api.restful-api.dev/objects/${userID}`);
        return response.data
    }catch(error){
        console.log('There was an error: ',error)
    }
}

function showdata(userData){
    const welcoID = document.getElementById('welco-user')
    welcoID.textContent = (`Welcome: ${userData.name}`)

}

async function main() {
    const userDataR = await userData(userID)

    if (userID === null){
    window.location.href = './login-page.html'
    }else{
    showdata(userDataR)
    showingTaskTable(userDataR.data.task)
    }
}

main()

function addingNewTask(userInfo, newname){
    try{
        const newTaskData = {
            "name":userInfo.name,
            "data":{
                "password":userInfo.data.password,
                "task":{
                    ...userInfo.data.task,
                    [newname]:"in-progress"
                }
            }
            
        }
        return newTaskData
    }catch (error){
        console.log(`An error occurs gatheing the information for task ${error}`)
    }
}

function updateTask(userInfo, taskName, state){
    try{
        if (state === 'complete'){
            const updateTask = {
                "name":userInfo.name,
                "data":{
                        "password":userInfo.data.password,
                        "task":{
                                ...userInfo.data.task,
                                [taskName]:'complete'
                                }}};
        return updateTask;
        }else if (state === 'delete'){
            const {[taskName]: _omit, ...deleteTask} = userInfo.data.task;
            const updateDeTask = {
                "name":userInfo.name,
                "data":{
                        "password":userInfo.data.password,
                        "task":{...deleteTask
                                }}};
            return updateDeTask
        }else{
            const originalstate = {
                "name":userInfo.name,
                "data":{
                        "password":userInfo.data.password,
                        "task":{
                                ...userInfo.data.task,
                                [taskName]:'in-progress'
                                }}};
            return originalstate
        };
        
    }catch(error){
        console.log(`error happen when performing the upgrade ${error}`)
    }
}

function filtertask(tasks, state){
    try{
        
        const filteredTask = Object.fromEntries(Object.entries(tasks).filter(([key,value])=> value === state));
        return filteredTask

    }catch (error){
        console.log(`An error has occurs when doing the filter: ${state}: error: ${error}`)
    }
}

function showingTaskTable(taskList){
    const tbody =document.getElementById('table-body');
    tbody.innerHTML = '';
    Object.entries(taskList).forEach(([taskName, state], possition) => {
        const row = `
    <tr class="table-tr">
      <td>${possition + 1}</td>
      <td>${taskName}</td>
      <td>${state}</td>
      <td>
        <button class="action-complete" data-task="${taskName}">✅</button>
        <button class="action-in-progress" data-task="${taskName}">🕓</button>
        <button class="action-delete" data-task="${taskName}">🗑️</button>
      </td>
    </tr>
  `;
  tbody.insertAdjacentHTML("beforeend", row);
    })
}



newTask.addEventListener('click', async()=>{
    const userDataR = await userData(userID);
    const taskInput = document.getElementById('task-input');
    const inputValue = taskInput.value
    const newTaskFormat = addingNewTask(userDataR,inputValue)
    const updateDBNewTask = await axios.put(`https://api.restful-api.dev/objects/${userID}`,newTaskFormat)
    const updateUserData = await userData(userID);
    const taskList = updateUserData.data.task;
    showingTaskTable(taskList)
    taskInput.value=''

})

closeSession.addEventListener('click', ()=>{
    localStorage.removeItem('userID')
    window.location.href = './login-page.html'
})

tbody.addEventListener("click", async(e)=>{
    const button = e.target;
    const taskName = button.dataset.task;
    const userInfo = await userData(userID);

    if (button.classList.contains("action-complete")){
        updateInfo = updateTask(userInfo, taskName, "complete")
    } else if (button.classList.contains("action-in-progress")){
        updateInfo = updateTask(userInfo, taskName, "in-progess")
    } else if (button.classList.contains("action-delete")){
        updateInfo = updateTask(userInfo, taskName, "delete")
    };
    
    const updatingDB = await axios.put(`https://api.restful-api.dev/objects/${userID}`,updateInfo);
    const updateUserData = await userData(userID);
    const taskList = updateUserData.data.task;
    showingTaskTable(taskList)
})

completeRadio.addEventListener("change", async()=>{
    const userInfo = await userData(userID);
    const filterToDo = filtertask(userInfo.data.task,'complete');
    showingTaskTable(filterToDo)
})

incompleteRadio.addEventListener("change",async()=>{
    const userInfo = await userData(userID);
    const filterToDo = filtertask(userInfo.data.task,'in-progress');
    showingTaskTable(filterToDo)
})

noneRadio.addEventListener('change', async()=>{
    const userInfo = await userData(userID);
    const taskList = userInfo.data.task;
    showingTaskTable(taskList)
})