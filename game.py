import tkinter as tk


root = tk.Tk()
root.title("Spēlīte")
root.geometry("350x250")


def start_scene():
    error_label.config(text="")
    try:
        number = int(number_choice.get())
    except:
        error_label.config(text="Kļūda: Lūdzu ievadi skaitli!")
        return

    # pārbauda vai skaitlis ir starp 20 un 30
    if number < 20 or number > 30:
        error_label.config(text="Kļūda: Skaitlim jābūt starp 20 un 30")
        return
    choice_scene.pack_forget()
    algo = choice_algorithm.get()
    print("Izvēlētais algoritms: "+algo)
    game_scene.pack()
    
    
    #num_label.config(text="Skaitlis: " + str(current_num))
    #pnts_label.config(text="Kopējie punkti: " + str(pnts))
    #bank_pnts.config(text="Banka: " + str(bank))

def btn_click():
    print("Poga nospiesta")

def end_game():
    print("Nospiesta poga beigt spēli")
    game_scene.pack_forget()
    choice_scene.pack()
#izvēles scenes (pirmais)

choice_scene = tk.Frame(root)
choice_scene.pack()



choice_label = tk.Label(choice_scene, text="Izvēlies skaitli 20-30")
choice_label.pack(pady=10)

choice_algorithm = tk.StringVar(value="none")


algo1 = tk.Radiobutton(choice_scene, text="Minimax", variable=choice_algorithm, value="minimax")
algo1.pack()

algo1 = tk.Radiobutton(choice_scene, text="Alpha-Beta", variable=choice_algorithm, value="alphabeta")
algo1.pack()

number_choice = tk.Spinbox(choice_scene, from_=20, to=30)
number_choice.pack(pady=10)

error_label = tk.Label(choice_scene, text="", fg="red")
error_label.pack(pady=5)

#sāk spēli primais scene -> otrais scene
start_button = tk.Button(choice_scene, text="Sākt spēli", command=start_scene)
start_button.pack(pady=10)

#
game_scene = tk.Frame(root)
#
pnts_label = tk.Label(game_scene, text="Kopējie punkti:")
pnts_label.pack(pady=5)
#
bank_pnts = tk.Label(game_scene, text="Bankas punkti:")
bank_pnts.pack(pady=5)
#
num_label = tk.Label(game_scene, text="Skaitlis:")
num_label.pack(pady=5)
#pogas
btn_frame = tk.Frame(game_scene)
btn_frame.pack(pady=10)
button1 = tk.Button(btn_frame, text="Reiz 3", width=10, fg="white", bg="black", command=btn_click)
button1.grid(column=0, row=1, padx=5)
button2 = tk.Button(btn_frame, text="Reiz 4", width=10, fg="white", bg="black", command=btn_click)
button2.grid(column=1, row=1, padx=5) 
button3 = tk.Button(btn_frame, text="Reiz 5", width=10, fg="white", bg="black", command=btn_click)
button3.grid(column=2, row=1, padx=5)
button4 = tk.Button(btn_frame, text="Atkārtot spēli", width = 10, bg="black", fg="red", command=end_game)
button4.grid(column=1, row=2, pady=10)
root.mainloop()