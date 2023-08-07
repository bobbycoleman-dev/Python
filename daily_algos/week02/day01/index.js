const arr1 = ["a", "a", "a"];
// expected: {a: 3}

const arr2 = ["a", "b", "a", "c", "Bob", "c", "c", "d"];
/* 
expected: {
    a: 2,
    b: 1,
    c: 3,
    Bob: 1,
    d: 1
}
*/

const arr3 = [];

function createObject(arr) {
	var obj = {};
	for (let i = 0; i < arr.length; i++) {
		obj[arr[i]] ? (obj[arr[i]] += 1) : (obj[arr[i]] = 1);
	}
	return obj;
}

console.log(createObject(arr1));
console.log(createObject(arr2));
console.log(createObject(arr3));

const nums1 = [1];
const expected1 = 1;

const nums2 = [5, 4, 5];
const expected2 = 4;

const nums3 = [5, 4, 3, 4, 3, 4, 5];
const expected3 = 4; // there is a pair of 4s but one 4 has no pair.

const nums4 = [5, 2, 6, 2, 3, 1, 6, 3, 2, 5, 2];
const expected4 = 1;

function nonPairNum(arr) {
	let obj = createObject(arr);
	for (let i = 0; i < arr.length; i++) {
		if (obj[arr[i]] % 2 == 1) {
			return arr[i];
		}
	}
}

console.log(nonPairNum(nums1));
console.log(nonPairNum(nums2));
console.log(nonPairNum(nums3));
console.log(nonPairNum(nums4));
