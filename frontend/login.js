

let login_form = document.getElementById("login-form")
addEventListener('submit', (e) => {
    e.preventDefault()
    let login_info = {
        'username': login_form.username.value,
        'password': login_form.password.value
    }
    // console.log(login_info)
    fetch('http://127.0.0.1:8000/api/users/token/', {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(login_info)
    }).then(
        response => response.json()
    ).then(
        data => console.log(data)
    )

})