/*
  Recursive Binary Search

  Input: SORTED array of ints, int value
  Output: bool representing if value is found

  Recursively search to find if the value exists, do not loop over every element.

  Approach:
  Take the middle item and compare it to the given value.
  Based on that comparison, narrow your search to a particular section of the array
*/

//             V
const nums1 = [1, 3, 5, 6];
const searchNum1 = 4;
const expected1 = false;

//             V
const nums2 = [4, 5, 6, 8, 12];
const searchNum2 = 5;
const expected2 = true;

const nums3 = [3, 4, 6, 8, 12];
const searchNum3 = 3;
const expected3 = true;

// don't be afraid to add parameters!

// base case(s)
// logic
// recursive call(s) / return(s)

// 1. Driver 🚗
// 2. Presenter 👩‍💻
// 3. Navigator 🧭

// take 5-8 mins to write the pseudocode first
// create the function and decide what params it needs and what it will return

function rBinary(num, arr, low = 0, high = arr.length - 1) {
	let mid = Math.floor((low + high) / 2);

	if (high < low) {
		return false;
	} else if (arr[mid] == num) {
		return true;
	}

	if (num < arr[mid]) {
		return rBinary(num, arr, low, (high = mid - 1));
	} else {
		return rBinary(num, arr, (low = mid + 1), high);
	}
}

console.log(rBinary(searchNum1, nums1));
console.log(rBinary(searchNum2, nums2));
console.log(rBinary(searchNum3, nums3));
