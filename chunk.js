let a = [1,2,3,4,5,6,7,8]
// chunk of 3
let x = 0;
console.log(a.length % 3)

// last chunk
x = a.length-2
console.log(a.slice(a.length-2))

x = a.length - 2 - 3
console.log(a.slice(3, a.length-2))

console.log(a.slice(0, a.length-2-3))

let b = [1,2,3,4,5,6,7,8,9,10,11,12,13,14];
console.log(b.length % 3)

console.log(b.slice(b.length-2));

console.log(b.slice(9,b.length-2));

console.log(b.slice(6,b.length-2-3));

console.log(b.slice(3,b.length-2-6));

console.log(b.slice(0,b.length-2-9));
