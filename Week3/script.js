let color = "black";
let setTrue = false;
function setColor(colorSet){
	if(colorSet == 'clear'){
		window.location.reload(false);
	}
	color = colorSet;
	console.log(color);
}
function changeColor(obj){
	if(setTrue){
		obj.setAttribute("style", "background-color:"+color);
	}
}
for(let r = 0; r < 6800; r++){
	let hold = document.createElement('div');
	hold.setAttribute("id", "gridBox");
	hold.setAttribute("class", "gridBox");
	hold.setAttribute("onmouseenter", "changeColor(this)");
	document.getElementById("main").appendChild(hold);
}

function set(check){
	setTrue = check;
}
function clear(check){


}