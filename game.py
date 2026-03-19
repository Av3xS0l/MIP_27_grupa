import tkinter as tk
from klases import Node
from klases import Minimax, AlfaBeta, Veiktspeja


root = tk.Tk()
root.title("Spēlīte")
root.geometry("350x250")


MAX_SKAITLIS = 3000

COMP_STATE = Node(0, 0, 0, True)
VEIKTS = None
ALGO = None
 
def start_scene():
    global COMP_STATE, VEIKTS, ALGO
    
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
    COMP_STATE.number = number
    izvele_dat_spel = choice_speletajs_izvele.get()
    VEIKTS = Veiktspeja()
    if izvele_dat_spel == "dators":
        COMP_STATE = Node(number, 0, 0, True)
        print(COMP_STATE.max)
    else:
        COMP_STATE = Node(number, 0, 0, False)
        print(COMP_STATE.max)
    rez = Minimax(COMP_STATE, VEIKTS)
    print(rez)
    ALGO = choice_algorithm.get()
    # print("Izvēlētais algoritms: "+algo)
    game_scene.pack()
    
    
    #num_label.config(text="Skaitlis: " + str(current_num))
    #pnts_label.config(text="Kopējie punkti: " + str(pnts))
    #bank_pnts.config(text="Banka: " + str(bank))
def calculate_new_state(reiz):
    COMP_STATE.number = COMP_STATE.number*reiz
    COMP_STATE.score  = COMP_STATE.score + COMP_STATE.new_punkti(COMP_STATE.number)
    COMP_STATE.bank = COMP_STATE.bank + COMP_STATE.new_banka(COMP_STATE.number)

def reiz3_komanda():
    calculate_new_state(3)
    if ALGO == "minimax":
        cels = Minimax(COMP_STATE, VEIKTS)
    else:
        cels = AlfaBeta(COMP_STATE, VEIKTS)
    print(cels)
    current_num= COMP_STATE.number*3
    num_label.config(text="Skaitlis: " + str(current_num))
    pnts_label.config(text="Kopējie punkti: " + str(COMP_STATE.score))
    bank_pnts.config(text="Banka: " + str(COMP_STATE.bank))
    # TODO update labels
    # TODO make the path choice


def reiz4_komanda():
    calculate_new_state(4)
    if ALGO == "minimax":
        cels = Minimax(COMP_STATE, VEIKTS)
    else:
        cels = AlfaBeta(COMP_STATE, VEIKTS)
    print(cels)
    current_num = COMP_STATE.number*4
    num_label.config(text="Skaitlis: " + str(current_num))
    pnts_label.config(text="Kopējie punkti: " + str(COMP_STATE.score))
    bank_pnts.config(text="Banka: " + str(COMP_STATE.bank))
    # TODO update labels
    # TODO make the path choice

def reiz5_komanda():
    calculate_new_state(5)
    if ALGO == "minimax":
        cels = Minimax(COMP_STATE, VEIKTS)
    else:
        cels = AlfaBeta(COMP_STATE, VEIKTS)
    print(cels)
    current_num= COMP_STATE.number*5
    num_label.config(text="Skaitlis: " + str(current_num))
    pnts_label.config(text="Kopējie punkti: " + str(COMP_STATE.score))
    bank_pnts.config(text="Banka: " + str(COMP_STATE.bank))
    # TODO update labels
    # TODO make the path choice



def end_game():
    print("Nospiesta poga beigt spēli")
    game_scene.pack_forget()
    choice_scene.pack()
    COMP_STATE.score = 0
    COMP_STATE.bank = 0
    COMP_STATE.number = 0
    num_label.config(text="Skaitlis: " + str(COMP_STATE.number))
    pnts_label.config(text="Kopējie punkti: " + str(COMP_STATE.score))
    bank_pnts.config(text="Banka: " + str(COMP_STATE.bank))
#izvēles scenes (pirmais)

choice_scene = tk.Frame(root)
choice_scene.pack()



choice_label = tk.Label(choice_scene, text="Izvēlies skaitli 20-30")
choice_label.pack(pady=10)

choice_algorithm = tk.StringVar(value="none")

choice_algorithm.set('minimax')
algo1 = tk.Radiobutton(choice_scene, text="Minimax", variable=choice_algorithm, value="minimax")
algo1.pack()

algo1 = tk.Radiobutton(choice_scene, text="Alpha-Beta", variable=choice_algorithm, value="alphabeta")
algo1.pack()

choice_speletajs_izvele = tk.StringVar(value="none")

choice_speletajs_izvele.set('speletajs')
dators_speletajs = tk.Radiobutton(choice_scene, text="Dators", variable=choice_speletajs_izvele, value="dators")
dators_speletajs.pack()

dators_speletajs = tk.Radiobutton(choice_scene, text="Speletajs", variable=choice_speletajs_izvele, value="speletajs")
dators_speletajs.pack()

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
button1 = tk.Button(btn_frame, text="Reiz 3", width=10, fg="white", bg="black", command=reiz3_komanda)
button1.grid(column=0, row=1, padx=5)
button2 = tk.Button(btn_frame, text="Reiz 4", width=10, fg="white", bg="black", command=reiz4_komanda)
button2.grid(column=1, row=1, padx=5) 
button3 = tk.Button(btn_frame, text="Reiz 5", width=10, fg="white", bg="black", command=reiz5_komanda)
button3.grid(column=2, row=1, padx=5)
button4 = tk.Button(btn_frame, text="Atkārtot spēli", width = 10, bg="black", fg="red", command=end_game)
button4.grid(column=1, row=2, pady=10)
root.mainloop()
