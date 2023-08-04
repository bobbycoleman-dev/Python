const str1 = "a x a";
// expected: true

const str2 = "racecar";
// expected: true

const str3 = "Dud";
// expected: false

const str4 = "oho!";
// expected: false

/**
 * @param {string} str
 * @returns {boolean}
 */

function isPalindrome(str) {
	var newStr = "";
	for (let i = str.length - 1; i >= 0; i--) {
		newStr += str[i];
	}
	return newStr == str ? true : false;
}

// console.log(isPalindrome(str1));
// console.log(isPalindrome(str2));
// console.log(isPalindrome(str3));
// console.log(isPalindrome(str4));

/* --------------------------------------------------- */

const str5 = "what up, daddy-o?";
const expected5 = "dad";

const str6 = "uh, not much";
const expected6 = "u";

const str7 = "Yikes! my favorite racecar erupted!";
const expected7 = "e racecar e";

const str8 = "a1001x20002y5677765z";
const expected8 = "5677765";

const str9 = "a1001x20002y567765z";
const expected9 = "567765";

const str10 = "daddy";
/**
 * Finds the longest palindromic substring in the given string.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str
 * @returns {string} The longest palindromic substring from the given string.
 */
function longestPalindromicSubstring(str) {
	var longest = "";
	for (let i = 0; i < str.length; i++) {
		var newStr = "";
		for (let j = i; j < str.length; j++) {
			newStr += str[j];
			if (isPalindrome(newStr)) {
				console.log(newStr);
				if (newStr.length > longest.length) {
					longest = newStr;
				}
			}
		}
	}
	return longest;
}

console.log(longestPalindromicSubstring(str10));
