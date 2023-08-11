/* 
  An anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
  typically using all the original letters exactly once.

  Is there a quick way to determine if they aren't an anagram before spending more time?

  Given two strings
  return whether or not they are anagrams
*/

const strA1 = "yes";
const strB1 = "eys";
const expected1 = true;

const strA2 = "yes";
const strB2 = "eYs";
const expected2 = true;

const strA3 = "no";
const strB3 = "noo";
const expected3 = false;

const strA4 = "silent";
const strB4 = "listen";
const expected4 = true;

/**
 * Determines whether s1 and s2 are anagrams of each other.
 * Anagrams have all the same letters but in different orders.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} s1
 * @param {string} s2
 * @returns {boolean} Whether s1 and s2 are anagrams.
 */

function isAnagram(s1, s2) {
	let new_s1 = s1.toLowerCase().split("").sort().join();
	let new_s2 = s2.toLowerCase().split("").sort().join();
	return new_s1 == new_s2 ? true : false;
}

// function isAnagram(s1, s2) {
// 	s1l = s1.toLowerCase();
// 	s2l = s2.toLowerCase();
// 	if (s1.length == s2.length) {
// 		for (const letter of s1l) {
// 			if (!s2l.includes(letter)) {
// 				return false;
// 			}
// 		}
// 		return true;
// 	}
// 	return false;
// }

console.log(isAnagram(strA1, strB1), "should equal", expected1);
console.log(isAnagram(strA2, strB2), "should equal", expected2);
console.log(isAnagram(strA3, strB3), "should equal", expected3);
console.log(isAnagram(strA4, strB4), "should equal", expected4);

/* 
  Given a string that may have extra spaces at the start and the end,
  return a new string that has the extra spaces at the start and the end trimmed (removed)
  do not remove any other spaces.
*/

const str1 = "   hello world     ";
const expected5 = "hello world";

/**
 * Trims any leading or trailing white space from the given str.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str
 * @returns {string} The given string with any leading or trailing white space
 *    stripped.
 */
function trim(str) {
	let output = "";
	let split = str.split(" ");
	for (const word of split) {
		if (word != "") {
			output += word;
			output += " ";
		}
	}
	let final = output.slice(0, output.length - 1);
	return final;
}

console.log(trim(str1), "should equal", expected5);
