// Modal Information from Django
const modalButtons = [...document.getElementsByClassName('modal-button')]

const modalBody = document.getElementById('modal-body-confirm')

const startButton = document.getElementById('start-button')

const url = window.location.href

modalButtons.forEach(Button => Button.addEventListener('click', ()=>{
    const pk = Button.getAttribute('data-pk')
    const date = Button.getAttribute('data-date')
    const name = Button.getAttribute('data-name')
    const description = Button.getAttribute('data-description')
    const topic = Button.getAttribute('data-topic')
    const numQuestions = Button.getAttribute('data-questions')
    const difficulty = Button.getAttribute('data-difficulty')
    const time = Button.getAttribute('data-time')
    const scoreToPass = Button.getAttribute('data-pass')


    modalBody.innerHTML = `
        <div class="mb-3">
            <h5>Are you sure you want to begin "<b>${name}</b>"</h5>
        </div>
        
        <div class="text-muted">
            <p>${description}</p>
            <ul>
                <li>Created at: <b>${date}</b></li>
                <li>Difficulty: <b>${difficulty}</b></li>
                <li>Topic: <b>${topic}</b></li>
                <li>Number of questions: <b>${numQuestions}</b></li>
                <li>Time available: <b>${time} minutes</b></li>
                <li>Score needed to pass: <b>${scoreToPass} %</b></li>
            </ul> 
        </div>
    
    `
    startButton.addEventListener('click', ()=>{
        window.location.href = url + 'quiz/' + pk // Takes the user to the detail view
    })
}))