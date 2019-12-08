function sumale() {
    var box1 = document.getElementById("importe");
    var box2 = document.getElementById("otros");
    var box3 = document.getElementById("total");
    
    var suma = Number(box1.value) + Number(box2.value);
    
    
    box3.value = suma;  
    
    
  }