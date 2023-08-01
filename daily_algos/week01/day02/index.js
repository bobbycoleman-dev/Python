const str1 = "object oriented programming";
const str2 = "abstract polymorphism inheritance encapsulation";
const str3 = "software development life cycle";
const str4 = " global  information tracker    ";

function acronymize(str) {
	var arr = str.split(" ");
	var newStr = "";

	for (var i = 0; i < arr.length; i++) {
		if (arr[i].length > 0) {
			// Edge Case: Checks for spaces in string
			newStr += arr[i][0].toUpperCase();
		}
	}

	return newStr;
}

console.log(acronymize(str1));
console.log(acronymize(str2));
console.log(acronymize(str3));
console.log(acronymize(str4));

function acronymize2(str) {
	var newStr = "";
	newStr += str[0].toUpperCase();
	for (var i = 0; i < str.length; i++) {
		if (str[i] == " ") {
			newStr += str[i + 1].toUpperCase();
		}
	}
	// Edge Case
	var finalStr = "";
	for (var i = 0; i < newStr.length; i++) {
		if (newStr[i] != " ") {
			finalStr += newStr[i];
		}
	}

	return finalStr;
}

console.log(acronymize2(str1));
console.log(acronymize2(str2));
console.log(acronymize2(str3));
console.log(acronymize2(str4));
