
addEventListener("DOMContentLoaded", function () {
  let edit = document.querySelector("#editLayout")
  let items = document.querySelectorAll(".item")
  let details = document.querySelectorAll(".details")
  

  function displayDetails(e) {   
    console.log(e.currentTarget.attributes.index.value)
    let i = e.currentTarget.attributes.index.value
    console.log(i)
    if (details[i].style.display === "block") {
      details[i].style.display = "none";
    } else {
      details[i].style.display = "block";
    }
  }
  
  for (let i = 0; i < items.length; i++){ 
    console.log(i)
    items[i].setAttribute("index", i)
    items[i].addEventListener("click", displayDetails)
    }  
  
  edit.addEventListener("change", function () {
    if (edit.checked) {
      for (let i = 0; i < items.length; i++) {
          console.log("checked", items)
          items[i].removeEventListener("click", displayDetails)
          details[i].style.display = "none" 
        }
      
  $(document).ready(function(){

    $( function() {
      var dragposition = '';
      $( ".item" ).draggable({containment: ".storage"},   
       {snap: true}       
    )
    $( ".item" ).draggable( "enable" );
    })
    }) 
 
  } else {
  console.log(edit.checked)
  $( ".item" ).draggable( "disable" )
  for (let i = 0; i < items.length; i++) {
    items[i].addEventListener("click", displayDetails)
  }
  }   
    
let save = document.querySelector("#save")
save.addEventListener("click", function () {
let storage = document.querySelector(".storage");
let storageSize = storage.getBoundingClientRect();

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
.then(() => {window.location.reload()});
})
})
})
this.window.addEventListener("resize" , event => {
  this.location.reload();
})
})
