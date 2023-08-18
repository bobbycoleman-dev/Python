/* 
  Given an int to represent how much change is needed
  calculate the fewest number of coins needed to create that change,
  using the standard US denominations
*/

const cents1 = 25;
const expected1 = { quarter: 1 };

const cents2 = 50;
const expected2 = { quarter: 2 };

const cents3 = 9;
const expected3 = { nickel: 1, penny: 4 };

const cents4 = 99;
const expected4 = { quarter: 3, dime: 2, penny: 4 };

const cents5 = 93;
const expected5 = { quarter: 3, dime: 1, nickel: 1, penny: 3 };

/**
 * Calculates the fewest coins of the standard American denominations needed
 *    to reach the given cents amount.
 * - Time: O(?).
 * - Space: O(?).
 * @param {number} cents
 * @param {string} sick
 * @returns {Object<string, number>} - A denomination table where the keys are
 *    denomination names and the value is the amount of that denomination
 *    needed.
 */
function fewestCoinChange(cents) {
	const coins = { quarter: 25, dime: 10, nickel: 5, penny: 1 };
	let output = {};

	for (const coin in coins) {
		const count = Math.floor(cents / coins[coin]);

		if (count > 0) {
			output[coin] = count;
			cents -= count * coins[coin];
		}
	}
	return output;
}

console.log(fewestCoinChange(cents1), "should equal:", expected1);
console.log(fewestCoinChange(cents2), "should equal:", expected2);
console.log(fewestCoinChange(cents3), "should equal:", expected3);
console.log(fewestCoinChange(cents4), "should equal:", expected4);
console.log(fewestCoinChange(cents5), "should equal:", expected5);
