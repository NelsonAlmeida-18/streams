import PySimpleGUI as sg

class passwordManager:
	def __init__(self):
		self.ModeSelection()

	def ModeSelection(self):
		layOut = [[sg.Button('Sign In'), sg.Button('Log In')]]	
		windowModeSelection = sg.Window('Password Manager', layOut)
		self.windowModeSelection = windowModeSelection
		loop = True
		while loop:             
			event, values = windowModeSelection.read()
			if event in ('Sign In', None):
				self.windowModeSelection.close()
				self.signin()
			if event in ('Log In', None):
				loop = False
				self.windowModeSelection.close()
				self.login()

	def signin(self):
		layout = [
			[sg.Text('Username', size=(15,1)),sg.InputText()],
			[sg.Text('Password', size=(15, 1)), sg.InputText(password_char='*')],
			[sg.Submit(), sg.Cancel()]
			]
		logger = 0
		windowSignIn = sg.Window('Sign In', layout)
		file = open('logs.txt', 'r')
		loopSignIn = True
		self.loopSignIn = loopSignIn
		while loopSignIn:             
			event, values = windowSignIn.read()
			if event in (sg.WIN_CLOSED, 'Cancel'):
				loopSignIn = False
				windowSignIn.close()
				break
			if event in ('Submit', None):
				username = values[0]
				password = values[1]
				for line in file:
					usernameInLine = line.split(",")[0]
					if (username == usernameInLine):
						sg.Popup('Esse nome/password já existem')
						logger = 1
						windowSignIn.close()
						self.signin()
						break
				file2 = open('logs.txt','a')
				file2.write('\n'+username+','+password)
				file2.close()
				windowSignIn.close()
				loopSignIn=False
				break

	def login(self):
		layout = [
			[sg.Text('Username', size=(15,1)),sg.InputText()],
			[sg.Text('Password', size=(15, 1)), sg.InputText(password_char='*')],
			[sg.Submit(), sg.Cancel()]
			]
		loginWindow = sg.Window('Log In', layout)
		self.loginWindow =loginWindow
		loop = True
		while loop:             
			event, values = loginWindow.read()
			if event in (sg.WIN_CLOSED, 'Cancel'):
				loginWindow.close()
				break
			if event in ('Submit', None):
				username = values[0]
				password = values[1]
				loop=False
				loginWindow.close()
				self.checker(username,password)

	def checker(self,username,password):
		file = open('logs.txt','r')
		for line in file:
			if line != "\n":
				usernameInLogs = line.split(',')[0]
				passwordInLogs = line.split(',')[1]
				passwordInLogs = passwordInLogs.split('\n')[0]
				if(usernameInLogs == username and passwordInLogs == password):
					self.loggedIn(username,password)
					break
				sg.Popup("Username/Password incorretos")
				self.login()

	def loggedIn(self,username, password):
		file = open('data.txt','a')
		for line in file:
			if 
		numOfLogs=(len(data)-1)/3
		headers = ['Platform', 'Username', 'Password']
		Platform = ['Platform']
		Username = ['Username']
		Password = ['Password']
		layout = [[sg.Table(values=data,headings=Platform,num_rows = numOfLogs,auto_size_columns=True,justification='left'),
           		   sg.Table(values=data,headings=Username,num_rows = numOfLogs,auto_size_columns=True,justification='left'),
           		   sg.Table(values=data,headings=Password,num_rows = numOfLogs,auto_size_columns=True,justification='left')],
           		   [sg.Button('Add')]]
		window = sg.Window('Password Manager', layout, grab_anywhere=False)
		event, values = window.read()
		if event in ('Add', None):
			window.close()
			self.adder(username,password)

	def adder(self, username, password):
		file = open('data.txt', 'a+')
		layout = [
		    [sg.Text('Plataforma', size=(15,1)),sg.InputText()],
			[sg.Text('Username', size=(15,1)),sg.InputText()],
			[sg.Text('Password', size=(15, 1)), sg.InputText(password_char='*')],
			[sg.Submit(), sg.Cancel()]
			]
		adderWindow = sg.Window('Adder', layout)
		loop = True
		while loop:             
			event, values = adderWindow.read()
			if event in ('Cancel', None):
				adderWindow.close()
				loop = False
			if event in ('Submit', None):
				platformToSubmit = values[0]
				usernameToSubmit = values[1]
				passwordToSubmit = values[2]
				lineToWrite = username+','+platformToSubmit+','+usernameToSubmit+','+passwordToSubmit
				file = open('data.txt','a+')
				for line in file:
					usernameInLine = line.split(",")[0]
					if username == usernameInLine:
						lineToWrite = str(line)+','+str(platformToSubmit)+','+str(usernameToSubmit)+','+str(passwordToSubmit)
				file.write(lineToWrite)
				file.close()
				adderWindow.close()
				self.loggedIn(username,password)

passwordManager()