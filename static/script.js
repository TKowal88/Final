
$(document).ready(function(){
  $( function() {
    var dragposition = '';
    $( ".item" ).draggable({containment: ".storage"},   
     {snap: true}       
  )})
  });

 
addEventListener("DOMContentLoaded", function () {

let save = document.querySelector("#save")
save.addEventListener("click", function () {
let storage = document.querySelector(".storage");
let storageSize = storage.getBoundingClientRect();
console.log(storageSize)

fetch(`${window.origin}/storage` , {
  method: "POST", 
  credentials: "include",
  body: JSON.stringify(storageSize),
  cache: "no-cache",
  headers: new Headers({ 
    "Content-Type": "application/json"
  })
})
.then(() => {
let items = document.querySelectorAll(".item")
let itemInfo = [];
for (let item of items) {
itemInfo.push({top: item.offsetTop, left: item.offsetLeft, id: item.id});
console.log(item.offsetLeft, item.offsetTop, item.id)
}
fetch(`${window.origin}/saved` , {
  method: "POST", 
  credentials: "include",
  body: JSON.stringify(itemInfo),
  cache: "no-cache",
  headers: new Headers({ 
    "Content-Type": "application/json"
  })
})
.then((response) => {
if (response.status === 200) {
   let saved = document.querySelector("#saved");
   saved.innerHTML = "Saved" 

}})
})
})
})
