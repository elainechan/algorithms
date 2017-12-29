/* Generate with Python:
import random
numbers = [random.randrange(1000000) for _ in range(1000000)]
with open("numbers.json", "w") as f: print(numbers, file=f)
*/
let arr = require('./numbers.json');

function bubble_sort(arr) {
    let swapped = true;
    while (swapped) {
        swapped = false;
        for (let i = 0; i < arr.length - 1; ++i) {
            if (arr[i] > arr[i + 1]) {
                const tmp = arr[i];
                arr[i] = arr[i + 1];
                arr[i + 1] = tmp;
                swapped = true;
            }
        }
    }
    return arr;
}

function merge(arr1, arr2) {
    let d1 = 0, d2 = 0;
    const result = [];
    //Step through the arrays until we run out
    //Advance the denoters every time we "take" an element
    while (d1 < arr1.length && d2 < arr2.length) {
        if (arr1[d1] <= arr2[d2]) {
            result.push(arr1[d1++]);
        } else {
            result.push(arr2[d2++]);
        }
    }
    while (d1 < arr1.length) result.push(arr1[d1++]);
    while (d2 < arr2.length) result.push(arr2[d2++]);
    return result;
}

//Inefficient implementation of merge sort
function merge_sort(arr) {
    //if (arr.length < 2) return arr;
    //We can actually improve performance by using a worse
    //algorithm - because at array sizes this low, Big O makes
    //less difference than the inefficiencies in the algorithms.
    if (arr.length < 64) return bubble_sort(arr);
    //Fracture the array in half
    const mid = Math.floor(arr.length / 2);
    let left = arr.slice(0, mid);
    let right = arr.slice(mid);
    //Sort each half
    left = merge_sort(left);
    right = merge_sort(right);
    //Merge the sorted halves into the final result
    return merge(left, right);
}

function fast_sort(arr) {
    return arr.sort((x, y) => (x > y));
}

//arr = bubble_sort(arr);
//arr = fast_sort(arr);
arr = merge_sort(arr);
console.log("The largest three are:");
for (let i = 0; i < 3; ++i) console.log(arr[arr.length - 1 - i]);