let equ = "";

function my_f(hi){

	if(hi == "="){
		alert(eval(equ));
		return;
	}
	if(hi == "c"){
		equ = "";
		return;
	}

	equ += hi;
	console.log(equ);
}
