model = {
    lastVal: '',
    currVal: '',
    operation: ''
}

operations = {
    '+': (a, b) => a+b,
    '-': (a, b) => a-b,
    '/': (a, b) => Math.floor(a/b),
    '*': (a, b) => a*b,
}

function toBinary(x) {
    let output = ''
    //first find max power of 2 that is larger than the number
    let max_pow = 0
    //always overshoots by one
    while(Math.pow(2, max_pow) <= x) {
        max_pow += 1
    }
    max_pow -= 1
    for (let i = max_pow; i >= 0; i--) {
        if(x - Math.pow(2, i) >= 0) {
            output += '1'
            x -= Math.pow(2, i)
        }
        else {
            output += '0'
        }
    }
    return output
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
//sum button
addButton = document.getElementById("btnSum")
addButton.addEventListener("click", (e) => {
    if(model.currVal) {
        model.operation = '+'
        resEl.textContent += '+'
        model.lastVal = model.currVal
        model.currVal = ''
    }
})

//subtract button
addButton = document.getElementById("btnSub")
addButton.addEventListener("click", (e) => {
    if(model.currVal) {
        model.operation = '-'
        resEl.textContent += '-'
        model.lastVal = model.currVal
        model.currVal = ''
    }
})

//multiply button
addButton = document.getElementById("btnMul")
addButton.addEventListener("click", (e) => {
    if(model.currVal) {
        model.operation = '*'
        resEl.textContent += '*'
        model.lastVal = model.currVal
        model.currVal = ''
    }
})

//multiply button
addButton = document.getElementById("btnDiv")
addButton.addEventListener("click", (e) => {
    if(model.currVal) {
        model.operation = '/'
        resEl.textContent += '/'
        model.lastVal = model.currVal
        model.currVal = ''
    }
})


//add equals button functionality
equalsButton = document.getElementById("btnEql")
equalsButton.addEventListener("click", (e) => {
    console.log(model)
    if(model.operation && model.lastVal && model.currVal) {
        let result = operations[model.operation](parseInt(model.lastVal, 2), parseInt(model.currVal, 2))
        console.log(result)
        result = toBinary(result)
        console.log(result)
        model.lastVal = ''
        model.currVal = result
        resEl.textContent = result
    }
})
