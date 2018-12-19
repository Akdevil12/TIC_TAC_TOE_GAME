#This is a python project to print tic tac toe game
import random as r
print("This is a tic tac toe game.")
print("Enter values 1-9 for position in the tile:-")
print("01 | 02 | 03 | 04 | 05")
print("---------------------")
print("06 | 07 | 08 | 09 | 10")
print("---------------------")
print("11 | 12 | 13 | 14 | 15")
print("----------------------")
print("16 | 17 | 18 | 19 | 20")
print("----------------------")
print("21 | 22 | 23 | 24 | 25")
print("By default you are O in this game and computer is X")
row1=[" "," "," "," "," "]
row2=[" "," "," "," "," "]
row3=[" "," "," "," "," "]
row4=[" "," "," "," "," "]
row5=[" "," "," "," "," "]
        
win="NONE"
try:

	for j in range(25):
		val=int(input("Enter your position:"))
		if(val in [1,2,3,4,5]):
			if(row1[val-1]=="X")or(row1[val-1]=="O"):
				print("Enter position where it is empty.")
				continue
			else:
				row1[val-1]="O"
				print(" | ".join(row1))
				print("------------------")
				print(" | ".join(row2))
				print("------------------")
				print(" | ".join(row3))
				print("------------------")
				print(" | ".join(row4))
				print("------------------")
				print(" | ".join(row5))
				
		if(val in [6,7,8,9,10]):
			if(row2[val-6]=="X")or(row2[val-6]=="O"):
				print("Enter position where it is empty.")
				continue
			else:
				row2[val-6]="O"
				print(" | ".join(row1))
				print("------------------")
				print(" | ".join(row2))
				print("------------------")
				print(" | ".join(row3))
				print("------------------")
				print(" | ".join(row4))
				print("------------------")
				print(" | ".join(row5))
		if(val in [11,12,13,14,15]):
			if(row3[val-11]=="X")or(row3[val-11]=="O"):
				print("Enter position where it is empty.")
				continue
			else:
				row3[val-11]="O"
				print(" | ".join(row1))
				print("------------------")
				print(" | ".join(row2))
				print("------------------")
				print(" | ".join(row3))
				print("------------------")
				print(" | ".join(row4))
				print("------------------")
				print(" | ".join(row5))
		if(val in [16,17,18,19,20]):
			if(row4[val-16]=="X")or(row4[val-16]=="O"):
				print("Enter position where it is empty.")
				continue
			else:
				row4[val-16]="O"
				print(" | ".join(row1))
				print("------------------")
				print(" | ".join(row2))
				print("------------------")
				print(" | ".join(row3))
				print("------------------")
				print(" | ".join(row4))
				print("------------------")
				print(" | ".join(row5))
		if(val in[21,22,23,24,25]):
			if((row5[val-21]=="X")or(row5[val-21]=="O")):
				print("Enter position where it is empty")
				continue
			else:
				row5[val-21]="O"
				print(" | ".join(row1))
				print("------------------")
				print(" | ".join(row2))
				print("------------------")
				print(" | ".join(row3))
				print("------------------")
				print(" | ".join(row4))
				print("------------------")
				print(" | ".join(row5))
		val=0
		if((row1==["O","O","O","O","O"])or(row2==["O","O","O","O","O"])or(row3==["O","O","O","O","O"])or(row4==["O","O","O","O","O"])or(row5==["O","O","O","O","O"])):
			win="human"
			break
		win2=1
		for i in range(5):
			if((row1[i]==row2[i])and(row2[i]==row3[i])and(row3[i]==row4[i])and(row4[i]==row5[i])and(row5[i]=="O")):
				win="human"
				win2=0
				break
		if(win2==0):
			break
		if((row1[0]==row2[1])and(row2[1]==row3[2])and(row3[2]==row4[3])and(row4[3]==row5[4])):
			if(row1[0]=="O"):
				win="human"
				break
		if((row1[4]==row2[3])and(row2[3]==row3[2])and(row3[2]==row4[1])and(row4[1]==row5[0])):
			if(row1[4]=="O"):
				win="human"
				break
		none1=0
		for i in range(5):
			if((row1[i]==" ")or(row2[i]==" ")or(row3[i]==" ")or(row4[i]==" ")or(row5[i]==" ")):
				none1=1
		if(none1==0):
			break
		print("Its computer turn now:-")
		i=0
		while i<2:
			comp=r.randint(1,25)
			if(comp in [1,2,3,4,5]):
				if((row1[comp-1]=="X")or(row1[comp-1]=="O")):
					i=1
				else:
					row1[comp-1]="X"
					print(" | ".join(row1))
					print("------------------")
					print(" | ".join(row2))
					print("------------------")
					print(" | ".join(row3))
					print("------------------")
					print(" | ".join(row4))
					print("------------------")
					print(" | ".join(row5))
					i=3
			if(comp in [6,7,8,9,10]):
				if((row2[comp-6]=="X")or(row2[comp-6]=="O")):
					i=1
				else:
					row2[comp-6]="X"
					print(" | ".join(row1))
					print("------------------")
					print(" | ".join(row2))
					print("------------------")
					print(" | ".join(row3))
					print("------------------")
					print(" | ".join(row4))
					print("------------------")
					print(" | ".join(row5))
					i=3
			if(comp in [11,12,13,14,15]):
				if((row3[comp-11]=="X")or(row3[comp-11]=="O")):
					i=1
				else:
					row3[comp-11]="X"
					print(" | ".join(row1))
					print("------------------")
					print(" | ".join(row2))
					print("------------------")
					print(" | ".join(row3))
					print("------------------")
					print(" | ".join(row4))
					print("------------------")
					print(" | ".join(row5))
					i=3
			if(comp in [16,17,18,19,20]):
				if((row4[comp-16]=="X")or(row4[comp-16]=="O")):
					i=1
				else:
					row4[comp-16]="X"
					print(" | ".join(row1))
					print("------------------")
					print(" | ".join(row2))
					print("------------------")
					print(" | ".join(row3))
					print("------------------")
					print(" | ".join(row4))
					print("------------------")
					print(" | ".join(row5))
					i=3
			if(comp in [21,22,23,24,25]):
				if((row5[comp-21]=="X")or(row5[comp-21]=="O")):
					i=1
				else:
					row5[comp-21]="X"
					print(" | ".join(row1))
					print("------------------")
					print(" | ".join(row2))
					print("------------------")
					print(" | ".join(row3))
					print("------------------")
					print(" | ".join(row4))
					print("------------------")
					print(" | ".join(row5))
					i=3
		comp=0
		if((row1==["X","X","X","X","X"])or(row2==["X","X","X","X","X"])or(row3==["X","X","X","X","X"])or(row4==["X","X","X","X","X"])or(row5==["X","X","X","X","X"])):
			win="computer"
			break
		win1=1
		for i in range(3):
			if((row1[i]==row2[i])and(row2[i]==row3[i])and(row3[i]==row4[i])and(row4[i]==row5[i])and(row5[i]=="X")):
				win="computer"
				win1=0
				break
		if(win1==0):
			break	
		if((row1[0]==row2[1])and(row2[1]==row3[2])and(row3[2]==row4[3])and(row4[3]==row5[4])):
			if(row1[0]=="X"):
				win="computer"
				break
		if((row1[4]==row2[3])and(row2[3]==row3[2])and(row3[2]==row4[1])and(row4[1]==row5[0])):
			if(row1[4]=="X"):
				win="computer"
				break
		none1=0
		for i in range(5):
			if((row1[i]==" ")or(row2[i]==" ")or(row3[i]==" ")or(row4[i]==" ")or(row5[i]==" ")):
				none1=1
		if(none1==0):
			break

	print("The winner is:",win)
except:
	print("Enter valid data type!")