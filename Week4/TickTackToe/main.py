defRow = [" ", " ", " "]
arr = [defRow, defRow, defRow]


def render_arr(arr):
	print("*****************")
	counterR = 0;
	for column in arr:
		row=""
		row+='*  '
		counteri = 0;
		for item in column:
			row +=" "
			row += item
			row += ' '
			if counteri != 2:
				row+="|"
			counteri+=1
		row+='  *'
		print(row);
		if counterR != 2:
			print('*  ---|---|---')
		counterR +=1

	print("*****************")
def checkWin(arr):
	returnVal = false
	column1 = []
	column2 = []
	column3 = []
	for row in arr:
		if row[0] == row[1] and row[1] == row[2]:
			if row[0]!=" ":
				returnVal=true
		column1.append(row[0])
		column2.append(row[1])
		column3.append(row[2])
	cols = [column1, column2, column3]
	for col in cols:
		if col[0] == col[1] and col[1] == col[2]:
			if col[0]!=" ":
				returnVal=true

	if cols[0][0] == cols[1][1] and cols[1][1] == cols[2][2]:
		if col[0][0]!=" ":
				returnVal=true
	if cols[0][2] == cols[1][1] and cols[1][1] == cols[2][0]:
		if col[0][2]!=" ":
				returnVal=true

	return returnVal;

def changeArr(arr, plyr):
	print("The current turn is ", plyr, "...")
	rowVal = int(input("Enter Row (1-3)"))
	colVal = int(input("Enter Col (1-3)")) 
	arr[rowVal-1][colVal-1] = 'x'
	print(arr[rowVal-1][colVal-1])
	return arr;


curPlayer = 'x'
while checkWin:
	if curPlayer=='x':
		arr = changeArr(arr, 'X')
		curPlayer='o'
	elif curPlayer=='o':
		arr =changeArr(arr, 'O')
		curPlayer='x'
	render_arr(arr)


if curPlayer=='x':
	print("Player O has won!")
elif curPlayer=='o':
	print("Player X has won!")