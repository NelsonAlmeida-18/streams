from collections import Counter

class globalBS():
    A1 = "   "
    A2 = "   "
    A3 = "   "
    B1 = "   "
    B2 = "   "
    B3 = "   "
    C1 = "   "
    C2 = "   "
    C3 = "   "

def printerMatriz():
	print("   A   B   C ")
	print("1|"+globalBS.A1+"|"+globalBS.B1+"|"+globalBS.C1+"|")
	print(" -----------")
	print("2|"+globalBS.A2+"|"+globalBS.B2+"|"+globalBS.C2+"|")
	print(" ------------")
	print("3|"+globalBS.A3+"|"+globalBS.B3+"|"+globalBS.C3+"|")


def diagonalWinning(plays):
	if ("A,1" in plays and "B,2" in plays and "C,3" in plays):
		return 1
	elif  ("A,3" in plays and "B,2" in plays and "C,1" in plays):
		return 1
	return 0

def sameColumnWinning(plays):
	size_of_array = len(plays)
	pos = 0
	row = []
	column=[]
	for i in plays:
		row.append(i.split(",")[0])
		column.append(i.split(",")[1])
	nums = str(Counter(column))
	nums = nums.split("{")[1]
	for i in nums:
		if i == "3":
			return 1
	return 0	


def winbyletter(plays):
	size_of_array = len(plays)
	pos = 0
	row = []
	column = []
	for i in plays:
		row.append(i.split(",")[0])
		column.append(i.split(",")[1])
	numOfLetters = str(Counter(row))
	numOfLetters = numOfLetters.split("{")[1]
	for i in numOfLetters:
		if i == "3":
			return 1
	return 0	

def assertion(plays):
	row = plays.split(",")[0]
	collumn = plays.split(",")[1]
	if (row<="C" and row >= "A" and collumn<="3" and collumn>="1"):
		return 1
	else:
		return 0

def populaArray(player, jogada):
	row = jogada.split(",")[0]
	column = jogada.split(",")[1]
	sprite = " "
	if player == "player1":
		sprite = " X "
		if(row=="A"):
			if(column=="1"):
				globalBS.A1 = sprite
			elif(column=="2"):
				globalBS.A2 = sprite
			elif(column =="3"):
				globalBS.A3 = sprite
		elif(row=="B"):
			if(column=="1"):
				globalBS.B1 = sprite
			elif(column == "2"):
				globalBS.B2 = sprite
			elif(column=="3"):
				globalBS.B3 = sprite
		elif(row=="C"):	
			if(column==1):
				globalBS.C1 = sprite
			elif(column=="2"):
				globalBS.C2 = sprite
			elif(column == "3"):
				globalBS.C3 = sprite
	else:
		sprite = " O "
		if(row=="A"):
			if(column=="1"):
				globalBS.A1 = sprite
			elif(column=="2"):
				globalBS.A2 = sprite
			elif(column =="3"):
				globalBS.A3 = sprite
		elif(row=="B"):
			if(column=="1"):
				globalBS.B1 = sprite
			elif(column == "2"):
				globalBS.B2 = sprite
			elif(column=="3"):
				globalBS.B3 = sprite
		elif(row=="C"):	
			if(column==1):
				globalBS.C1 = sprite
			elif(column=="2"):
				globalBS.C2 = sprite
			elif(column == "3"):
				globalBS.C3 = sprite

def main():
	player1Plays = []
	player2Plays = []
	win = False
	namePlayer1 = input("Nome do Jogador1: ")
	namePlayer2 = input("Nome do Jogador2: ")
	printerMatriz()
	while(win==False):
		if(len(player1Plays)+len(player2Plays)<=9):
			player1Input = input("Faz a tua jogada "+namePlayer1+"(Ex: A,1): ")
			while(len(player1Input)< 3 or assertion(player1Input)!=1 or player1Input in player1Plays or player1Input in player2Plays):
				print(namePlayer1+" faz uma jogada válida!")
				player1Input = input("Faz a tua jogada "+namePlayer1+"(Ex: A,1): ")
			populaArray("player1",player1Input)
			printerMatriz()
			player1Plays.append(player1Input)
			if (len(player1Plays)>=3):
				if (winbyletter(player1Plays)==1 or sameColumnWinning(player1Plays)==1 or diagonalWinning(player1Plays)==1):
					print("Parabéns "+namePlayer1+" ganhaste!")
					return None
			player2Input = input("Faz a tua jogada "+namePlayer2+"(Ex: A,1): ")
			while(len(player2Input)<3 or assertion(player2Input)!=1 or player2Input in player1Plays or player2Input in player2Plays):
				print(namePlayer2+" faz uma jogada válida!")
				player2Input = input("Faz a tua jogada "+namePlayer2+"(Ex: A,1): ")
			populaArray("player2",player2Input)
			printerMatriz()
			player2Plays.append(player2Input)
			if(len(player2Plays)>=3):
				if(winbyletter(player2Plays)==1 or sameColumnWinning(player2Plays)==1 or diagonalWinning(player2Plays)==1):
					print("Parabéns "+namePlayer2+" ganhaste!")
					return None
		else:
			print("Empataram!")
			replay = input("Querem jogar novamente?(y or n) ")
			if (replay == "y"):
				player2Plays=[]
				player1Plays=[]
			else:
				return None
main()