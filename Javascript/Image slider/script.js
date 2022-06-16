let curPos = 0;
let position = 0; 
const IMAGE_WIDTH = 815;
const prevBtn = document.querySelector(".prev")
const nextBtn = document.querySelector(".next")
const images = document.querySelector(".image")
//const는 뭐지? 

function prev() {
    if (curPos > 0) {
        nextBtn.removeAttribute("disabled");
        position += IMAGE_WIDTH;
        images.style.transform = `translateX(${position}px)`;
        curPos = curPos - 1;
    }
    if(curPos == 0){
        prevBtn.setAttribute('disabled', 'true')
    }
}
//이전 버튼

function next() {
    if (curPos < 4) {
        prevBtn.removeAttribute("disabled");
        position -= IMAGE_WIDTH;
        images.style.transform = `translateX(${position}px)`;
        curPos = curPos + 1
    }
    if(curPos == 4){
        nextBtn.setAttribute('disabled', 'true')
    }
}
//다음 버튼

function init(){
    prevBtn.setAttribute('disabled', 'true')
    prevBtn.addEventListener("click", prev)
    nextBtn.addEventListener("click", next)
    }
   
init();