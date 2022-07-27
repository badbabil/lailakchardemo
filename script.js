function myFunction() {
    var x = document.getElementById("confpass");

    if (x.type === "password"){
      x.type = "text";
    } 
    else {
      x.type = "password";
    }
  }