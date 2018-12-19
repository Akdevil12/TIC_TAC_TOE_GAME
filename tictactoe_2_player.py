#This is a python project to print tic tac toe game
import sys as s
import random as r
print("This is a tic tac toe game.")
print("Enter values 1-9 for position in the tile:-")
print("1 | 2 | 3")
print("---------")
print("4 | 5 | 6")
print("---------")
print("7 | 8 | 9")
print("By player 1 is O in this game and player 2 is X")
row1=[" "," "," "]
row2=[" "," "," "]
row3=[" "," "," "]
win="NONE"
try:	
	for j in range(9):
		val=int(input("Enter your position player 1:"))
		if(val in [1,2,3]):
			if(row1[val-1]=="X")or(row1[val-1]=="O"):
				print("Enter position where it is empty player 1.")
				continue
			else:
				row1[val-1]="O"
				print(" | ".join(row1))
				print("---------")
				print(" | ".join(row2))
				print("---------")
				print(" | ".join(row3))
		if(val in [4,5,6]):
			if(row2[val-4]=="X")or(row2[val-4]=="O"):
				print("Enter position where it is empty player 1.")
				continue
			else:
				row2[val-4]="O"
				print(" | ".join(row1))
				print("---------")
				print(" | ".join(row2))
				print("---------")
				print(" | ".join(row3))
		if(val in [7,8,9]):
			if(row3[val-7]=="X")or(row3[val-7]=="O"):
				print("Enter position where it is empty player 1.")
				continue
			else:
				row3[val-7]="O"
				print(" | ".join(row1))
				print("---------")
				print(" | ".join(row2))
				print("---------")
				print(" | ".join(row3))
		val=0
		if((row1==["O","O","O"])or(row2==["O","O","O"])or(row3==["O","O","O"])):
			win="player 1"
			break
		win2=1
		for i in range(3):
			if((row1[i]==row2[i])and(row2[i]==row3[i])and(row1[i]=="O")):
				win="player 1"
				win2=0
				break
		if(win2==0):
			break
		if((row1[0]==row2[1])and(row2[1]==row3[2])):
			if(row1[0]=="O"):
				win="player 1"
				break
		if((row1[2]==row2[1])and(row2[1]==row3[0])):
			if(row1[2]=="O"):
				win="player 1"
				break
		i=0
		while i<2:
			val2=int(input("Enter your position player 2:"))
			if(val2 in [1,2,3]):
				if((row1[val2-1]=="X")or(row1[val2-1]=="O")):
					i=1
					print("Enter an empty position player 2")
				else:
					row1[val2-1]="X"
					print(" | ".join(row1))
					print("---------")
					print(" | ".join(row2))
					print("---------")
					print(" | ".join(row3))
					i=3
			if(val2 in [4,5,6]):
				if((row2[val2-4]=="X")or(row2[val2-4]=="O")):
					i=1
					print("Enter an empty position player 2")
				else:
					row2[val2-4]="X"
					print(" | ".join(row1))
					print("---------")
					print(" | ".join(row2))
					print("---------")
					print(" | ".join(row3))
					i=3
			if(val2 in [7,8,9]):
				if((row3[val2-7]=="X")or(row3[val2-7]=="O")):
					i=1
				else:
					row3[val2-7]="X"
					print(" | ".join(row1))
					print("---------")
					print(" | ".join(row2))
					print("---------")
					print(" | ".join(row3))
					i=3
		val2=0
		if((row1==["X","X","X"])or(row2==["X","X","X"])or(row3==["X","X","X"])):
			win="player 2"
			break
		win1=1
		for i in range(3):
			if((row1[i]==row2[i])and(row2[i]==row3[i])and(row1[i]=="X")):
				win="player 2"
				win1=0
				break
		if(win1==0):
			break	
		if((row1[0]==row2[1])and(row2[1]==row3[2])):
			if(row1[0]=="X"):
				win="player 2"
				break
		if((row1[2]==row2[1])and(row2[1]==row3[0])):
			if(row1[2]=="X"):
				win="player 2"
				break
	print("The winner is:",win)
except:
	print("Enter valid value!!")
	s.exit()
