model = {
    lastVal: '',
    currVal: '',
    operation: ''
}

//get result display element
resEl = document.getElementById("res")

//assign event listeners to the calculator numerical input buttons
for (let i = 0; i < 2; i++) {
    numEl = document.getElementById(`btn${i}`);
    numEl.addEventListener("click", (e) => {
        model.currVal += event.target.textContent
        resEl.textContent += event.target.textContent
    })
}

//assign event listener to "Clear" button
clearButton = document.getElementById("btnClr")
clearButton.addEventListener("click", (e) => {
    for (let item in model) {model[item] = ''}
    resEl.textContent = model.currVal
})


//add operator event listeners
addButton = document.getElementById("btnSum")
addButton.addEventListener("click", (e) => {
    if(model.currVal) {
        operation = '+'
        resEl.textContent += '+'
        model.lastVal = model.currVal
        model.currVal = ''
    }
})
