let arr = prompt("Enter some words?").split(",");
let arrl = arr.length;
let longW = 0;
for(let k = 0; k < arrl; k++){
	if(arr[k].length>longW){
		longW = arr[k].length;
	}
}
let topBot = "";
for(let d=0; d < longW+2; d++){
	topBot+= "*";
}
console.log(topBot);
for(let i=0; i < arrl; i++){
	arr[i] = "*"+arr[i];
	let hold =arr[i].length;
	for(let j=0; j < (longW+1) - hold; j++){
		arr[i] = arr[i]+" ";
	}
	arr[i]+="*";
	console.log(arr[i]);
}
console.log(topBot);