const setupApp = () => {
  hookUpBtns();
};

// function hookUpBtns() {
//   let csrf_token = document.getElementsByTagName("input").item(0).value;
//   const submitBtn = document.getElementById("sign-up-btn");
//   submitBtn.addEventListener("click", (event) => {
//     event.preventDefault();
//     console.log(csrf_token);

   

//   // Example POST method implementation:



function getCookie(cname) {
  var name = cname + "=";
  var decodedCookie = decodeURIComponent(document.cookie);
  var ca = decodedCookie.split(';');
  for(var i = 0; i <ca.length; i++) {
    var c = ca[i];
    while (c.charAt(0) == ' ') {
      c = c.substring(1);
    }
    if (c.indexOf(name) == 0) {
      return c.substring(name.length, c.length);
    }
  }
  return "";
}


async function postData(url = '', myData = {}) {

      const response = await fetch(url, {
        method:'POST',
        headers:{
          'Content-type':'application/json',
          'X-CSRFToken':getCookie('csrftoken'),
        },
        body:JSON.stringify(myData)
      });
  }




function hookUpBtns(){
  const submitBtn = document.getElementById("sign-up-btn");
  submitBtn.addEventListener('click',(event)=>{
    event.preventDefault();
    let data = {
      'username':document.getElementById('username').value,
      'first_name':document.getElementById('first_name').value,
      'last_name':document.getElementById('last_name').value,
      'email':document.getElementById('email').value,
      'password':document.getElementById('password').value,
    };
    postData('http://127.0.0.1:8000/',data);


  });


}






window.onload = setupApp;






































 // fetch("http://127.0.0.1:8000?username=amr", {
    //   method: "POST",
    //   headers: {
    //     "Content-Type": "application/json",
    //     "X-CSRFToken": csrf_token,
    //   },
    //   data: JSON.stringify({
    //     username: "Amr El gamed awy",
    //   }),
    // });

  //   fetch("http://127.0.0.1:8000", {
  //     method: "post",
  //     headers: {
  //       Accept: "application/json",
  //       "Content-Type": "application/json",
  //       "X-CSRFToken": csrf_token,
  //     },
  //     data: JSON.stringify({ a: 7, str: "Some string: &=&" }),
  //   })
  //     .then((res) => res.json())
  //     .then((res) => console.log(res));
  // });