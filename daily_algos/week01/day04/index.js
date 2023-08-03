//! Encode String
const estr1 = "aaaabbcddd";
// expected = "a4b2c1d3"
const estr2 = "";
// expected2 = '';
const estr3 = "a";
// expected3 = 'a';
const estr4 = "bbcc";
// expected4 = 'bbcc';

function encodeStr(str) {
	var output = "";
	var letter = "";
	var counter = 1;
	for (var i = 0; i < str.length; i++) {
		letter += str[i];
		while (str[i] == str[i + 1]) {
			letter = str[i];
			counter++;
			i++;
		}
		output += letter;
		output += counter;
		letter = "";
		counter = 1;
	}
	if (output.length >= str.length) {
		output = str;
	}
	console.log(output);
}

encodeStr(estr1);
encodeStr(estr2);
encodeStr(estr3);
encodeStr(estr4);
/* ----------------------------------- */
/* ----------------------------------- */

//! Decode String
const dstr1 = "a3b2c1d3";
// expected: "aaabbcddd"

const dstr2 = "a3b2c12d10";
// expected2 = 'aaabbccccccccccccdddddddddd';

function decodeStr(str) {
	// code
}
