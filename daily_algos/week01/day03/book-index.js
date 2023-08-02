/* 
Book Index

Given an array of ints representing page numbers
return a string with the page numbers formatted as page ranges when the nums
span a consecutive range.
*/

const nums1 = [1, 13, 14, 15, 37, 38, 70];
const expected1 = "1, 13-15, 37-38, 70";

const nums2 = [5, 6, 7, 8, 9];
const expected2 = "5-9";

const nums3 = [1, 2, 3, 7, 9, 15, 16, 17];
const expected3 = "1-3, 7, 9, 15-17";

/*

check if nums[i + 1] == num[i] + 1 !checks consecutive!
Put consecs into empty array, pull out arr[0] and arr[arr.length],
    var consecStr = ""
    consecStr =+ arr[0]
    consecStr =+ "-"
    consecStr =+ arr[arr.length]
    


*/

/**
 * Turns the given arr of page numbers into a string of comma hyphenated
 * page ranges.
 * - Time: O(?).
 * - Space: O(?).
 * @param {Array<number>} nums Page numbers.
 * @returns {string} The given page numbers as comma separated hyphenated
 *    page ranges.
 */
function bookIndex(nums) {
	var joinedStr = "";
	var separator1 = ", ";
	var separator2 = "-";
	var tempArr = [];
	var consecStr = "";
	for (var i = 0; i < nums.length; i++) {
		// Checks if nums starts with a consec, if not pushes to joined str
		if (nums[i] + 1 != nums[i + 1]) {
			joinedStr += nums[i];
			joinedStr += separator1;

			// Check if [i+1] = [i] + 1 // i.e. [i] = 14 + 1 == [i+1] = 15
		} else {
			if (nums[i] - 1 == nums[i - 1] && nums[i] + 1 != nums[i + 1]) {
				tempArr.push(nums[i]);
			} else if (nums[i + 1] == nums[i] + 1) {
				tempArr.push(nums[i]);
			}
			consecStr += tempArr[0];
			consecStr += separator2;
			consecStr += tempArr[tempArr.length - 1];
			joinedStr += consecStr;
		}
	}

	console.log(joinedStr);
}

bookIndex(nums1);
