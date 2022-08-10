
document.addEventListener("DOMContentLoaded", function () {
   

 /* var draggableElements = document.getElementsByClassName("item")

for (var i = 0; i < draggableElements.length; i++) {
    dragElement(draggableElements[i])
}

function dragElement(elmnt) {
    var pos1 = 0, pos2 = 0, pos3 = 0, pos4 = 0;
    elmnt.onmousedown = dragMouseDown;

    function dragMouseDown(e) {
        e = e || window.event
        pos3 = parseInt(e.clientX);
        pos4 = parseInt(e.clientY);
        document.onmouseup = closeDragElement;
        document.onmousemove = elementDrag;
        return false;
    }

    function elementDrag(e) {
        e = e || window.event;
        pos1 = pos3 - parseInt(e.clientX);
        pos2 = pos4 - parseInt(e.clientY);
        pos3 = parseInt(e.clientX);
        pos4 = parseInt(e.clientY);
        let storage = document.querySelector(".storage")
        if (elmnt.offsetTop - pos2 >= 0 && elmnt.offsetLeft - pos1 >= 0) {
        elmnt.style.top = (elmnt.offsetTop - pos2) + "px";
        elmnt.style.left = (elmnt.offsetLeft - pos1) + "px";
        }
        console.log(pos1, pos2, pos3, pos4, storage.offsetHeight, storage.offsetWidth)
        
        
    }

    function closeDragElement() {
        document.onmouseup = null;
        document.onmousemove = null;
    }
} */
})  

