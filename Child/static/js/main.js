const taskInput = document.getElementById('add-task-text'),
      taskBtn = document.getElementById('add-task-input'),
      taskWrapper = document.getElementById('tasks');

taskBtn.addEventListener('click', function(){
    let taskValue = taskInput.value;

    if(taskValue == ''){
        alert('يجب عليك ادخال نص للمهمة')
    }else{
        let newTaskWrapper = document.createElement('div');
        newTaskWrapper.classList.add('task');
        newTaskWrapper.classList.add('p-1');
        newTaskWrapper.classList.add('mb-1');
        
        let newTaskcheckbox = document.createElement('input');
        newTaskcheckbox.setAttribute('id', 'task3');
        newTaskcheckbox.setAttribute('type', 'checkbox');
    
        let newTasklable = document.createElement('label');
        newTasklable.setAttribute('for', 'task3');
        newTasklable.innerText = taskValue;
    
        newTaskWrapper.append(newTaskcheckbox);
        newTaskWrapper.append(newTasklable);
        taskWrapper.append(newTaskWrapper);
        taskInput.value = '';
    }

});




function changeVideoLink(link) {
    const frame = document.querySelector('iframe');
    let endLink = link.split('.be/')[1];
    console.log(endLink);
    frame.src =   `https://www.youtube.com/embed/${endLink}`;
}