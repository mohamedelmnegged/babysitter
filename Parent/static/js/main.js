const // taskInput = document.getElementById('add-task-text'),
      eduVedioInput = document.getElementById('add-new-eduVedio'),
      cartoonVedioInput = document.getElementById('add-new-cartoonVedio'),
      // taskBtn = document.getElementById('add-task-input'),
      eduVidoBtn = document.getElementById('add-new-eduVedio-input'),
      cartoonVidoBtn = document.getElementById('add-new-cartoonVedio-input'),
      // taskWrapper = document.getElementById('tasks'),
      eduVidoesWrapper = document.getElementById('eduVidoes'),
      cartoonVidoesWrapper = document.getElementById('cartoonVidoes');

let removeVideo = document.getElementsByClassName('remove');
let removeTask = document.getElementsByClassName('removeTask');

// REMOVE VED
Array.prototype.forEach.call(removeVideo, function(span) {
    span.addEventListener('click', function(){
        this.parentElement.parentElement.remove();
    })
});

Array.prototype.forEach.call(removeTask, function(span) {
    span.addEventListener('click', function(){
        this.parentElement.remove();
        console.log(this.previousElementSibling.innerText); // TASK NAME
    })
});


// ADD NEW CARTOON VED
cartoonVidoBtn.addEventListener('click', function(){
    let cartoonVidoLink = cartoonVedioInput.value;
    let vidID = cartoonVidoLink.split('.be/')[1]
    if(cartoonVidoLink == ''){
        alert('يجب عليك ادخال رابط الفيديو')
    }else{
        let newVedioWrapper = document.createElement('div');
        newVedioWrapper.classList.add('control-wrapper');
        newVedioWrapper.classList.add('col-12');
        newVedioWrapper.classList.add('col-md-4');
        
        let newVedio = document.createElement('div');
        newVedio.classList.add('control');
        newVedio.classList.add('control-1');
        newVedio.classList.add('mb-2');
    
        let removeVedio = document.createElement('span');
        removeVedio.classList.add('remove');
        removeVedio.innerText = "x";

        let iframe = document.createElement('iframe');
        iframe.setAttribute('src', `https://www.youtube.com/embed/${vidID}`);
        iframe.setAttribute('width', '560');
        iframe.setAttribute('height', '315');
        iframe.setAttribute('title', 'YouTube video player');
        iframe.setAttribute('frameborder', '0');
        iframe.setAttribute('allow', 'accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture');
        iframe.setAttribute('allowfullscreen', true);
    
        newVedio.append(removeVedio);
        newVedio.append(iframe);

        newVedioWrapper.append(newVedio);

        console.log(newVedioWrapper);
        
        cartoonVidoesWrapper.append(newVedioWrapper);
        cartoonVedioInput.value = '';
        
        removeVideo = document.getElementsByClassName('remove');
        
        Array.prototype.forEach.call(removeVideo, function(span) {
            span.addEventListener('click', function(){
                this.parentElement.parentElement.remove();
            })
        });
    }

});

// ADD NEW EDU VED
eduVidoBtn.addEventListener('click', function(){
    let eduVedioLink = eduVedioInput.value;
    let vidID = eduVedioLink.split('.be/')[1]
    if(eduVedioLink == ''){
        alert('يجب عليك ادخال رابط الفيديو')
    }else{
        let newVedioWrapper = document.createElement('div');
        newVedioWrapper.classList.add('control-wrapper');
        newVedioWrapper.classList.add('col-12');
        newVedioWrapper.classList.add('col-md-4');
        
        let newVedio = document.createElement('div');
        newVedio.classList.add('control');
        newVedio.classList.add('control-1');
        newVedio.classList.add('mb-2');
    
        let removeVedio = document.createElement('span');
        removeVedio.classList.add('remove');
        removeVedio.innerText = "x";

        let iframe = document.createElement('iframe');
        iframe.setAttribute('src', `https://www.youtube.com/embed/${vidID}`);
        iframe.setAttribute('width', '560');
        iframe.setAttribute('height', '315');
        iframe.setAttribute('title', 'YouTube video player');
        iframe.setAttribute('frameborder', '0');
        iframe.setAttribute('allow', 'accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture');
        iframe.setAttribute('allowfullscreen', true);
    
        newVedio.append(removeVedio);
        newVedio.append(iframe);

        newVedioWrapper.append(newVedio);

        console.log(newVedioWrapper);
        
        eduVidoesWrapper.append(newVedioWrapper);
        eduVedioInput.value = '';
        
        removeVideo = document.getElementsByClassName('remove');
        
        Array.prototype.forEach.call(removeVideo, function(span) {
            span.addEventListener('click', function(){
                this.parentElement.parentElement.remove();
            })
        });
    }

});

// ADD NEW TASK
// taskBtn.addEventListener('click', function(){
//     let taskValue = taskInput.value;

//     if(taskValue == ''){
//         alert('يجب عليك ادخال نص للمهمة')
//     }else{
//         let newTaskWrapper = document.createElement('div');
//         newTaskWrapper.classList.add('task');
//         newTaskWrapper.classList.add('p-1');
//         newTaskWrapper.classList.add('mb-1');
        
//         let newTaskcheckbox = document.createElement('input');
//         newTaskcheckbox.setAttribute('id', 'task3');
//         newTaskcheckbox.setAttribute('type', 'checkbox');
    
//         let newTasklable = document.createElement('label');
//         newTasklable.setAttribute('for', 'task3');
//         newTasklable.innerText = taskValue;
    
//         newTaskWrapper.append(newTaskcheckbox);
//         newTaskWrapper.append(newTasklable);
//         taskWrapper.append(newTaskWrapper);
//         taskInput.value = '';
//     }

// });


function test() {
    const frame = document.querySelector('iframe');
    let link = "https://youtu.be/YeQH_cMEbrI",
        endLink = link.split('.be/')[1];
        console.log(endLink);
    frame.src =   `https://www.youtube.com/embed/${endLink}`;
}