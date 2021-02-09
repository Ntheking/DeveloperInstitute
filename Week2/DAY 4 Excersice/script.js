//Excersice 1

//let age = prompt("What age r u?");

/*function checkAge(age){
	if(age > 18){
		console.log("can drive");
	}else if(age<18){
		console.log("no driving")
	}else{
		console.log("Your 18 you can drive now yay");
	}
}

console.log(checkAge(45));

//Excercise 2

function changeEnough(arr, price){
	let sum =0;
	for(let i=0; i<arr.length; i++){
		sum+=arr[i];
	}
	if(sum>=price){
		return true;
	}else{
		return false;
	}
}

console.log(changeEnough([23,45,12], 50));

function mult(){
	let current =0;
	let sum=0;
	while(current<500){
		sum+=current;
		current+=23;
	}
	return sum;
}
console.log(mult());
//excesice 4

let amazonBasket = {
    glasses: 1,
    books: 2,
    floss: 100
}
function stringCheckFunc(hallo){
		if(hallo in amazonBasket){
			return true;
		}
}
console.log(stringCheckFunc('glasses'));
//ex 5
let shoppingList = [
	"banana", "apple", "orange"
]

let stock = { 
    "banana": 6, 
    "apple": 0,
    "pear": 12,
    "orange": 32,
    "blueberry":1
}  

let prices = {    
    "banana": 4, 
    "apple": 2, 
    "pear": 1,
    "orange": 1.5,
    "blueberry":10
} 
function check(shoppingStuff){
	let total = 0;
	for(let i=0; i<shoppingStuff.length; i++){
		if(shoppingStuff[i] in prices){
			if(stock[shoppingStuff[i]] > 0){
				stock[shoppingStuff[i]]--;
				total += prices[shoppingStuff[i]];
			}
		}
	}
	return total;
}

console.log(check(shoppingList));
*/
//ex6
/*function tipCalc(prices){
	let tips=[];
	let tots=[];
	for(let i = 0; i < prices.length; i++){
		if(prices[i]>200){
			tips.push(prices[i] * 0.1);
		}else if(prices[i] >50){
			tips.push(prices[i] * 0.15);
		}else{
			tips.push(prices[i] * 0.2);
		}
	}
	for(let i = 0; i < tips.length;i++){
		tots.push(tips[i]+ prices[i]);
	}
	return tots;
}
let prices = prompt("prices?").split(",");
for(let i =0; i < prices.length; i++){
	prices[i] = parseFloat(prices[i]);
}

console.log(tipCalc(prices));
*/
//ex 7
function hotel_cost(nights){
	
	return 140 * nights;
}
function planeCost(loc){

	if(loc=="London"){
		return 183;
	}else if(loc=="Paris"){
		return 220;
	}
	return 300;
}
function rentalCarCost(days){
	
	days *= 40;
	if(days/40 > 10){
		days *= 0.95;
	}
	return days;
}
function totCost(){
	let nights = prompt("How many nights?");	

	while (!/^[0-9]+$/.test(nights)) {
    alert("You did not enter a number.");
    nights = prompt("How many nights?");
	}
	let loc = prompt("Where did you go?");
	while(/^[0-9]+$/.test(loc)){
		alert("A number is not a place");
		loc = prompt("Where did you go?");
	}
	let days = prompt("How many days?");
	while(!/^[0-9]+$/.test(days)){
		alert("NOT A NUMBER");
		days = prompt("How many days?");
	}
	return hotel_cost(nights) + rentalCarCost(days) + planeCost(loc);
}
console.log(totCost());
