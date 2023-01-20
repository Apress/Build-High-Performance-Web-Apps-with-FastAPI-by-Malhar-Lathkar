function myFunction() {
  let text;
  if (confirm("Do You Want to Continue\nChoose Ok/Cancel") == true) {
    text = "You pressed OK!";
  } else {
    text = "You pressed cancel";
  }
  document.getElementById("response").innerHTML = text;
}
