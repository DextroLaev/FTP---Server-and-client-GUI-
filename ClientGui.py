from tkinter import *
from tkinter import messagebox
import socket

def send():
	text.delete(1.0,END)
	try:
		ip = Ip_entry.get()
		port_val = Port_entry.get()
		file = file_entry.get()

		text.insert(INSERT, 'IP address = ')
		text.insert(INSERT, ip)	
		host = ip
		text.insert(INSERT, '\n')
		text.insert(INSERT, 'Port = ')		
		port = int(port_val)
		text.insert(INSERT, port)
		text.insert(INSERT, '\n')
		text.insert(INSERT, "filename = ")
		text.insert(INSERT, file)
		text.insert(INSERT, '\n')				
				
		s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		text.insert(INSERT, 'Establishing conenction...')
		text.insert(INSERT, '\n')							
		s.connect((host,port))
		text.insert(INSERT, '\n')	
		text.insert(INSERT, 'Connection has been established.')
		text.insert(INSERT, '\n')				
		s.send(file.encode())
		text.insert(INSERT, '\n')
		text.insert(INSERT, 'Request send, waiting for respond...')

		with open(file,'wb') as f:
			text.insert(INSERT, '\n')
			text.insert(INSERT, 'Receiving the contents of the file.....')			
			while True:				
				data = s.recv(1024)
				if not data:
					break
				f.write(data)

		text.insert(INSERT, '\n')
		text.insert(INSERT, 'File recieved succcessfully...:)')			
		f.close()
		s.close()

	except:		
		text.insert(INSERT,'Some error has occured.')	

root = Tk()
root.title("Receiver")
canvas = Canvas(root,width=500,height=500,bg='light green')
	
# textfield
scroll = Scrollbar(root)
text = Text(root,width=50,height=10,wrap=WORD,padx=10,pady=10,yscrollcommand=scroll.set)	

# Labels
canvas.pack()
Ip_label = Label(root,text='IP address:-',bg='light green')
Port_label = Label(root,text='Port:-',bg='light green')
Choose_file = Label(root,text='File name:-',bg='light green')

# Entry fields

Ip_entry = Entry(root,width=30)
Port_entry = Entry(root,width=30)
file_entry = Entry(root,width=30)

# Buttons
recieve = Button(root,text='Send request',width=14,bg='green',command=send)

# placements
Ip_label.place(x=40,y=40)
Port_label.place(x=40,y=100)
Choose_file.place(x=40,y=160)

Ip_entry.place(x=140,y=40)
Port_entry.place(x=140,y=100)
file_entry.place(x=140,y=160)


recieve.place(x=180,y=230)
text.place(x=40,y=270)

root.geometry('500x500')
root.mainloop()