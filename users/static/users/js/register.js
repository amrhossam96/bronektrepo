let ps = document.getElementsByTagName('p');
let submitBtn = document.getElementsByTagName('button').item(0);

submitBtn.id = 'sign-up-btn';



for(let i=0;i<5;i++){
  ps.item(i).classList.add('row');
}








































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