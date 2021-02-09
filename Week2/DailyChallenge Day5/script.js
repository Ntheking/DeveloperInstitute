let start = prompt("How many bottles to start");

let changeVal = 1;
for(let i = start; i > 0; i += 0){
	let itThem = " them ";
	console.log(i + " bottles of beer on the wall");
	console.log(i + " bottles of beer");
	if(changeVal == 1){
		itThem = " it ";
	}
	console.log("Take " + changeVal + " down pass" + itThem + "around")
	if(i - changeVal > 0){
		console.log((i-changeVal) + " bottles of beer on the wall");
	}
	i -= changeVal;
	changeVal++;

}