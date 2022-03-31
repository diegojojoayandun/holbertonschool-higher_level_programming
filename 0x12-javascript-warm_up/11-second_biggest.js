#!/usr/bin/node

const nums = process.argv.slice(2).map((n) => parseInt(n));

if (process.argv.length > 3) {
  const minNumber = Math.min(...nums);
  const maxNumber = Math.max(...nums);
  let secMaxNum = minNumber;

  for (let i = 0; i < nums.length; i++) {
    if (nums[i] > secMaxNum && nums[i] < maxNumber) {
      secMaxNum = nums[i];
    }
  }
  console.log(secMaxNum);
} else {
  console.log(0);
}
