
$(document).ready(function(){
  $( function() {
    var dragposition = '';
    $( ".dropzone" ).draggable({containment: ".storage"},
    
     {snap: true},
     {stop: function(event, ui){
      
      dragposition = ui.position;
      console.log(dragposition)
    }   
})
  });

let save = document.querySelector("#save")
save.addEventListener("click", function() {
  let items = document.querySelectorAll(".dropzone")
for (let item of items) {
let itemInfo = {top: item.offsetTop, left: item.offsetLeft, id: item.id};
console.log(itemInfo)
}
})
})



  
 

