/* 
  Given a string containing space separated words
  Reverse each word in the string.

  If you need to, use .split to start, then try to do it without.
*/

const str1 = "hello";
const expected1 = "olleh";

const str2 = "hello world";
const expected2 = "olleh dlrow";

const str3 = "abc def ghi";
const expected3 = "cba fed ihg";

/**
 * Reverses the letters in each words in the given space separated
 * string of words. Does NOT reverse the order of the words themselves.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str Contains space separated words.
 * @returns {string} The given string with each word's letters reversed.
 */
function reverseWords(str) {
	var newStr = "";
	let splitStr = str.split(" ");
	for (const word of splitStr) {
		for (let j = word.length - 1; j >= 0; j--) {
			newStr += word[j];
		}
		newStr += " ";
	}
	return newStr;
}

console.log(reverseWords(str1));
console.log(reverseWords(str2));
console.log(reverseWords(str3));

/* 
  Given a string,
  return a new string with the duplicates excluded

  Bonus: Keep only the last instance of each character.
*/

console.log("********************************");

const str4 = "abcABC";
const expected4 = "abcABC";

const str5 = "helloo";
const expected5 = "helo";

const str6 = "";
const expected6 = "";

const str7 = "aa";
const expected7 = "a";

/**
 * De-dupes the given string.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str A string that may contain duplicates.
 * @returns {string} The given string with any duplicate characters removed.
 */

function stringDedupe(str) {
	let finalStr = "";
	for (const letter of str) {
		if (!finalStr.includes(letter)) {
			finalStr += letter;
		}
	}
	return finalStr;
}

console.log(stringDedupe(str4));
console.log(stringDedupe(str5));
console.log(stringDedupe(str6));
console.log(stringDedupe(str7));
