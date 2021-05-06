let fs = require('fs');
// let inputlist = fs.readFileSync('input.txt').toString().split('\r\n');
let inputlist = fs.readFileSync('/dev/stdin').toString().split('\n');

let n = Number(inputlist[0]);
let dp = new Array(n);
for (let i = 0; i < n; i++) {
  dp[i] = 0;
}
for (let index = 0; index < n; index++) {
  let a = inputlist[index+1].split(" ")
  let start = 0
  if (index - 1 < 0) {
    start = 0
  } else {
    start = dp[index - 1]
  }
  for (let idx = index + Number(a[0]) - 1; idx < n; idx++) {
    dp[idx] = Math.max(dp[idx], start + Number(a[1]))
  }
}

console.log(Math.max(...dp));