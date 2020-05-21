from tkinter import *
from tkinter import messagebox
import socket
import sys

def start():
	text.delete(1.0,END)
	text.insert(INSERT, 'IP address = ')
	ip = Ip_entry.get()	
	text.insert(INSERT, ip)	
	print(ip)
	port_val = Port_entry.get()	
	text.insert(INSERT, '\n')
	text.insert(INSERT, 'Port = ')		
	port = int(port_val)
	print(port)
	text.insert(INSERT, port)
	text.insert(INSERT, '\n')
	text.insert(INSERT, '\n')				
				
	s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	text.insert(INSERT, 'Establishing connection....')
	text.insert(INSERT, '\n')
	s.bind((ip,port))		
	s.listen(1)		
	try:
		c,addr = s.accept()
		text.insert(INSERT, '\n')
		text.insert(INSERT, 'Connection has been established with {}'.format(addr))
		text.insert(INSERT, '\n')
		text.insert(INSERT, '\n')
		fname = c.recv(1024)
		fname = fname.decode()
		text.insert(INSERT, 'File name = {}'.format(fname))		
		text.insert(INSERT, '\n')		

		try:
			with open(fname,'rb') as f:
				content = f.read()
				while content:
					c.send(content)
					content = f.read()
				f.close()
				text.insert(INSERT, 'File has been send successfully..')
		except FileNotFoundError:
			c.send(b'no such file found')
			text.insert(INSERT, 'No such file has been found..')
		c.close()				
		s.close()
	except:
		text.insert(INSERT, '\n')
		text.insert(INSERT,"Unable to connect")	
	
root = Tk()
root.title("Sender")
canvas = Canvas(root,width=500,height=500,bg='light green')
	
# textfield
scroll = Scrollbar(root)
text = Text(root,width=50,height=15,wrap=WORD,padx=10,pady=10,yscrollcommand=scroll.set)	

# Labels
canvas.pack()
Ip_label = Label(root,text='IP address:-',bg='light green')
Port_label = Label(root,text='Port:-',bg='light green')

# Entry fields
Ip_entry = Entry(root,width=30)
Port_entry = Entry(root,width=30)

# Buttons
recieve = Button(root,text='Start',width=14,bg='green',command=start)


# placements
Ip_label.place(x=40,y=40)
Port_label.place(x=40,y=100)

Ip_entry.place(x=140,y=40)
Port_entry.place(x=140,y=100)

recieve.place(x=180,y=150)
text.place(x=40,y=200)

root.geometry('500x500')
root.mainloop()