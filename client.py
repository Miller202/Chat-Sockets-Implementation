import tkinter
from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread

HOST = "localhost"
PORT = 33000
if not PORT:
    PORT = 33000
else:
    PORT = int(PORT)

BUFF_SIZE = 1024
ADDRESS = (HOST, PORT)

client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect(ADDRESS)


# Configure tkinter
window = tkinter.Tk()
window.title("Client")

# Variables declaration
client_name = tkinter.StringVar()
client_receiver = tkinter.StringVar()
client_subject = tkinter.StringVar()
client_msg = tkinter.StringVar()


# Labels
label_name = tkinter.Label(window, text="Seu nome:")
label_receiver = tkinter.Label(window, text="Destinatário")
label_subject = tkinter.Label(window, text="Assunto:")
label_msg = tkinter.Label(window, text="Mensagem:")
label_inbox = tkinter.Label(window, text="Caixa de entrada:")

# Display messages in the inbox
frame_msg = tkinter.Frame(window)
bar = tkinter.Scrollbar(frame_msg)
list_msg = tkinter.Listbox(window, yscrollcommand=bar.set)


# Inputs
input_name = tkinter.Entry(window, textvariable=client_name)
input_name.bind("<Return>", )
input_receiver = tkinter.Entry(window, textvariable=client_receiver)
input_receiver.bind("<Return>", )
input_subject = tkinter.Entry(window, textvariable=client_subject)
input_subject.bind("<Return>", )
input_msg = tkinter.Entry(window, textvariable=client_msg)
input_msg.bind("<Return>", )


# Grids
label_name.grid(row=1, column=1)
label_receiver.grid(row=2, column=1)
label_subject.grid(row=3, column=1)
label_msg.grid(row=4, column=1)
label_inbox.grid(row=9, column=1)

frame_msg.grid()
bar.grid()
list_msg.grid(row=10, column=1, columnspan=2)

input_name.grid(row=1, column=2)
input_receiver.grid(row=2, column=2)
input_subject.grid(row=3, column=2)
input_msg.grid(row=4, column=2)


# Starts GUI execution.
window.mainloop()
