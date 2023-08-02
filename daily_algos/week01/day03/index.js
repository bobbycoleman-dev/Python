const arr1 = ["a", "b", "c", "d"];
const separator1 = ", ";

const arr2 = [1, 2, 3, 4];
const separator2 = "-";

const arr3 = [1, 2, 3];
const separator3 = " - ";

const arr4 = [1];
const separator4 = ", ";

const arr5 = [];
const separator5 = ", ";

function join(arr, separator) {
	var joinedStr = "";
	for (var i = 0; i < arr.length; i++) {
		if (arr[i] == arr[arr.length - 1]) {
			joinedStr += arr[i];
		} else {
			joinedStr += arr[i];
			joinedStr += separator;
		}
	}
	console.log(joinedStr);
}

join(arr1, separator1);
join(arr2, separator2);
join(arr3, separator3);
join(arr4, separator4);
join(arr5, separator5);
