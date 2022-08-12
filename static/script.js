
document.addEventListener("DOMContentLoaded", function () {
    let storage = document.querySelector(".storage")
    let rect = storage.getBoundingClientRect()
    var gridTarget = interact.snappers.grid({
        // can be a pair of x and y, left and top,
        // right and bottom, or width, and height
        x: 10,
        y: 5
    })

    interact('.dropzone').draggable({
        
      modifiers: [
      interact.modifiers.snap({ targets: [gridTarget], 
        
        limits: {
          top: rect.top,
          left: rect.left,
          bottom: rect.bottom,
          height: rect.height
        }
      }),
        interact.modifiers.restrictRect({
          restriction: '.storage', 
          
          endOnly: true
        })
      ],
        
  

      

      listeners: {
        start (event) {
          console.log(event.type, event.target)
        },
        move (event) {
        const target = event.target;
        const dataX = target.getAttribute("data-x");
        const dataY = target.getAttribute("data-y");
        console.log(dataX, dataY);
        const initialX = parseFloat(dataX) || 0;
        const initialY = parseFloat(dataY) || 0;

        const deltaX = event.dx;
        const deltaY = event.dy;

        const newX = initialX + deltaX;
        const newY = initialY + deltaY;

        target.style.transform = `translate(${newX}px, ${newY}px)`;

        target.setAttribute("data-x", newX);
        target.setAttribute("data-y", newY);

        
            
        },
      }
    })
    
   

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

