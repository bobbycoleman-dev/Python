function rSigma(num) {
	if (num < 1) {
		return num;
	}
	num = Math.floor(num);
	return rSigma(num - 1) + num;
}

// console.log(rSigma(5));

/* 
Recursive Factorial
Given a number `num`, return the product of integers from 1 upward to that number.
If less than or equal to zero, return -1. If not an integer, treat as an integer.

Input: integer
Output: product of integers from 1 to input integer
*/

const num1 = 3;
const expected1 = 6;
// Explanation: 1 * 2 * 3 = 6

const num2 = 5;
const expected2 = 120;
// Explanation: 1 * 2 * 3 * 4 * 5 = 120

const num3 = 3.5;
const expected3 = 6;
// Explanation: 1 * 2 * 3 = 6

const num4 = 0;
const expected4 = -1;
// Explanation: num is zero, return -1

const num5 = -1;
const expected5 = -1;
// Explanation: num is less than zero, return -1

/**
 * Recursively sum the given int and every previous positive int.
 * - Time: O(?).
 * - Space: O(?).
 * @param {number} num
 * @returns {number}
 */
function rFactorial(num) {
	if (num == 1) {
		return num;
	} else if (num <= 0) {
		return -1;
	}
	num = Math.floor(num);
	return rFactorial(num - 1) * num;
}

// console.log(rFactorial(num1), "should equal", expected1);
// console.log(rFactorial(num2), "should equal", expected2);
// console.log(rFactorial(num3), "should equal", expected3);
// console.log(rFactorial(num4), "should equal", expected4);
// console.log(rFactorial(num5), "should equal", expected5);

/* 
  Recursively sum an arr of ints
*/

const nums1 = [1, 2, 3];
const expecteds1 = 6;

const nums2 = [1];
const expecteds2 = 1;

const nums3 = [];
const expecteds3 = 0;

/**
 * Add params if needed for recursion
 * Recursively sums the given array.
 * - Time: O(?).
 * - Space: O(?).
 * @param {Array<number>} nums
 * @returns {number} The sum of the given nums.
 */
function sumArr(nums) {
	if (nums.length == 0) {
		return 0;
	}
	let x = nums.pop();
	return sumArr(nums) + x;
}

console.log(sumArr(nums1), "should be", expecteds1);
console.log(sumArr(nums2), "should be", expecteds2);
console.log(sumArr(nums3), "should be", expecteds3);
