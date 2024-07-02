

let logoutBtn = document.getElementById('logout-btn')
logoutBtn.addEventListener('click', (e) => {
    e.preventDefault()
    localStorage.removeItem('access_token')
    alert('You are not login now')
})

let projectsUrl = 'http://127.0.0.1:8000/api/projects/'

let getProjects = () => {
    fetch(projectsUrl)
    .then(response => response.json())
    .then(data => {
        createProjectsList(data)
    })
}


let createProjectsList = (projects) => {
    let access_token = localStorage.getItem('access_token')
    let project_list_section = document.getElementById('projects--wrapper')
    project_list_section.innerHTML = ""

    for (let i=0; projects.length > i; i++) {
        let project = projects[i]
        // console.log(project)
        let projectCard = `
            <div class="project--card">
                <img src="http://127.0.0.1:8000/${project.featured_image}">

                <div>
                    <div class="card--header">
                        <h3>${project.title}</h3>
                        <strong class="vote--option" data-vote="up" data-project_id="${project.id}">&#43</strong>
                        <strong class="vote--option" data-vote="down" data-project_id="${project.id}">&#8722</strong>
                    </div>
                    <i>${project.vote_ratio}% Positive feedback</i>
                    <p>${project.description.substring(0, 150)}</p>
                </div>
            </div>
        `
        project_list_section.innerHTML += projectCard
    }

    addVotesListeners(access_token)

}


let addVotesListeners = (token) => {
    let voteElements = document.getElementsByClassName('vote--option')

    for (let i=0; voteElements.length > i; i++) {
        voteElements[i].addEventListener('click', (e) => {
            let vote = e.target.dataset.vote
            let project = e.target.dataset.project_id
            // console.log(vote, project)
            fetch(`http://127.0.0.1:8000/api/projects/${project}/vote/`, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                    "Authorization": `Bearer ${token}`
                },
                body: JSON.stringify({
                    "review_value": vote
                })
                
            }).then(
                () => {getProjects()}
            )
            
        })
    }
}


getProjects()
