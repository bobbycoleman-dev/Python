// 0, 1, 1, 2, 3, 5...

const num1 = 0;
const expected1 = 0;

const num2 = 1;
const expected2 = 1;

const num3 = 2;
const expected3 = 1;

const num4 = 3;
const expected4 = 2;

const num5 = 4;
const expected5 = 3;

const num6 = 8;
const expected6 = 21;

function fibonacci(num) {
	// base case
	let arr = [0, 1];
	for (let i = 2; i <= num; i++) {
		arr.push(arr[i - 1] + arr[i - 2]);
	}

	return arr[num];
}

// console.log(fibonacci(num1), "should equal", expected1);
// console.log(fibonacci(num2), "should equal", expected2);
// console.log(fibonacci(num3), "should equal", expected3);
// console.log(fibonacci(num4), "should equal", expected4);
// console.log(fibonacci(num5), "should equal", expected5);
// console.log(fibonacci(num6), "should equal", expected6);

function rFib(num) {
	if (num < 2) {
		return num;
	}

	return rFib(num - 1) + rFib(num - 2);
}

console.log(rFib(num1), "should equal", expected1);
console.log(rFib(num2), "should equal", expected2);
console.log(rFib(num3), "should equal", expected3);
console.log(rFib(num4), "should equal", expected4);
console.log(rFib(num5), "should equal", expected5);
console.log(rFib(num6), "should equal", expected6);
