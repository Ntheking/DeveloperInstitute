

String.prototype.replaceAt = function(index, replacement) {
    return this.substr(0, index) + replacement + this.substr(index + replacement.length);
}


let word = prompt("Insert a word?");

let wl = word.length;

while(wl < 8){
	word = prompt("Insert a word with more letters?");
	wl = word.length;
}
word = word.toLowerCase();
let ph = "";
for(let i = 0; i < wl; i++){
	ph += "*";
}
console.log(ph);
let gv = [];
let lives = 10;
while(lives > 0){
	let guess = prompt("Guess a letter?");
	let strike = true;
	if(gv.indexOf(guess) != -1){
		console.log("Already guessed")
		continue;
	}
	for(let i = 0; i <wl; i++){
		if(guess == null){
			i = wl;
		}
		if(word.charAt(i) == guess.charAt(0)){
			ph = ph.replaceAt(i, guess);
			console.log(ph[i]);
			strike = false;
		}
	}
	if(strike){
		lives--;
	}
	gv.push(guess);
	console.log("Lives: " + lives);
	console.log("Word: " + ph);
	console.log("Guessed: " + gv);
	if(ph.indexOf('*') == -1){
		break;
	}
}
if(lives==0){
	console.log("LOSER");
}else{
	console.log("VICTORY");
}


