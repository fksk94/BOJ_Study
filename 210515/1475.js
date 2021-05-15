let fs = require('fs');
// let inputlist = fs.readFileSync('input.txt').toString().split('\r\n');
let inputlist = fs.readFileSync('/dev/stdin').toString().split('\n');

let s = String(inputlist[0]);
let arr = new Array(9);
for (let i = 0; i < arr.length; i++) {
  arr[i] = 0;
}

for (let i = 0; i < s.length; i++) {
  if (s[i] === '0') {
    arr[0] += 1 
  } else if (s[i] === '1') {
    arr[1] += 1 
  } else if (s[i] === '2') {
    arr[2] += 1 
  } else if (s[i] === '3') {
    arr[3] += 1 
  } else if (s[i] === '4') {
    arr[4] += 1 
  } else if (s[i] === '5') {
    arr[5] += 1
  } else if (s[i] === '6') {
    arr[6] += 0.5
  } else if (s[i] === '7') {
    arr[7] += 1 
  } else if (s[i] === '8') {
    arr[8] += 1
  } else if (s[i] === '9') {
    arr[6] += 0.5 
  }
}

console.log(Math.ceil(Math.max(...arr)));