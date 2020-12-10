button5 = document.getElementById("btn5")

button5.addEventListener("click", function(e) {
    //get current labels on buttons
    let label_arr = []
    for (let i = 1; i<10; i++) {
        let curr_text = document.getElementById(`btn${i}`).textContent
        label_arr.push(curr_text)
    }
    console.log(label_arr)
    //now switch the text on the different buttons to rotate
    //clockwise
    //array with locations of new values from old array
    let new_arr_ind = [3, 0, 1, 6, 4, 2, 7, 8, 5]
    // label_arr[0] = label_arr[3], label_arr[1] = label_arr[0], label_arr[2] = label_arr[1], label_arr[3] = label_arr[6],
    // label_arr[5] = label_arr[2], label_arr[6] = label_arr[7], label_arr[7] = label_arr[8], label_arr[8] = label_arr[5]

    for (let i = 1; i < 10; i++) {
        document.getElementById(`btn${i}`).textContent = label_arr[new_arr_ind[i-1]]
    }
})
