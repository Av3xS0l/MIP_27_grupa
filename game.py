import tkinter as tk
from klases import Node
from klases import Minimax, AlfaBeta, Veiktspeja


root = tk.Tk()
root.title("Spēlīte")
root.geometry("350x250")


MAX_SKAITLIS = 3000

COMP_STATE = Node(0, 0, 0, True, True)
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
    result_scene.pack_forget()
    izvele_dat_spel = choice_speletajs_izvele.get()
    ALGO = choice_algorithm.get()
    print("-- jauns raunds --")
    print("generets | izskatits | kopējais laiks")
    VEIKTS = Veiktspeja()
    if izvele_dat_spel == "dators":
        COMP_STATE = Node(number, 0, 0, True, True)
        datora_gajiens(0)
    else:
        COMP_STATE = Node(number, 0, 0, False, False)
    num_label.config(text="Skaitlis: " + str(COMP_STATE.number))
    pnts_label.config(text="Kopējie punkti: " + str(COMP_STATE.score))
    bank_pnts.config(text="Banka: " + str(COMP_STATE.bank))
    game_scene.pack()
    
def calculate_new_state(reiz):
    COMP_STATE.number = COMP_STATE.number*reiz
    COMP_STATE.score  = COMP_STATE.score + COMP_STATE.new_punkti(COMP_STATE.number)
    COMP_STATE.bank = COMP_STATE.bank + COMP_STATE.new_banka(COMP_STATE.number)
    COMP_STATE.next = []

def datora_gajiens(num):
    if num != 0:
        calculate_new_state(num)
    
    if COMP_STATE.number >= MAX_SKAITLIS:
        print(VEIKTS)
        end_game()
        return

    if ALGO == "minimax":
        cels = Minimax(COMP_STATE, VEIKTS)
    else:
        cels = AlfaBeta(COMP_STATE, VEIKTS)
    calculate_new_state(cels[0])
    print(VEIKTS)
    if COMP_STATE.number >= MAX_SKAITLIS:
        end_game()

def refresh_labels():
    num_label.config(text="Skaitlis: " + str(COMP_STATE.number))
    pnts_label.config(text="Kopējie punkti: " + str(COMP_STATE.score))
    bank_pnts.config(text="Banka: " + str(COMP_STATE.bank))
    num_end_label.config(text="Skaitlis: " + str(COMP_STATE.number))
    pnts_end_label.config(text="Kopējie punkti: " + str(COMP_STATE.score))
    bank_end_pnts.config(text="Banka: " + str(COMP_STATE.bank))

def reiz3_komanda():
    datora_gajiens(3)
    refresh_labels()


def reiz4_komanda():
    datora_gajiens(4)
    refresh_labels()


def reiz5_komanda():
    datora_gajiens(5)
    refresh_labels()


def reset_game():
    # print("Nospiesta poga beigt spēli")
    game_scene.pack_forget()
    result_scene.pack_forget()
    choice_scene.pack()
    COMP_STATE.score = 0
    COMP_STATE.bank = 0
    COMP_STATE.number = 0
    num_label.config(text="Skaitlis: " + str(COMP_STATE.number))
    pnts_label.config(text="Kopējie punkti: " + str(COMP_STATE.score))
    bank_pnts.config(text="Banka: " + str(COMP_STATE.bank))
    #izvēles scenes (pirmais)

def get_winner():

    result = COMP_STATE.score % 2 == COMP_STATE.bank % 2
    if result and COMP_STATE.max:
        return "dators"
    elif not COMP_STATE.max and not result:
        return "dators"
    else:
        return "cilveks"

def end_game():
    game_scene.pack_forget()
    result_scene.pack()
    refresh_labels()
    winer_label.config(text=f"Spēli uzvarēja {get_winner()}!")



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
button4 = tk.Button(btn_frame, text="Atkārtot spēli", width = 10, bg="black", fg="red", command=reset_game)
button4.grid(column=1, row=2, pady=10)

# Uzvara / zaudējums
result_scene = tk.Frame(root)
pnts_end_label = tk.Label(result_scene, text="Kopējie punkti: ")
pnts_end_label.pack(pady=5)
#
bank_end_pnts = tk.Label(result_scene, text="Bankas punkti:")
bank_end_pnts.pack(pady=5)
#
num_end_label = tk.Label(result_scene, text="Skaitlis:")
num_end_label.pack(pady=5)

winer_label = tk.Label(result_scene, text=f"Spēli uzvarēja {get_winner()}!")
winer_label.pack(pady=5)

restart_end_btn = tk.Button(result_scene, text="Atkārtot spēli", width = 10, bg="black", fg="red", command=reset_game)
restart_end_btn.pack()

root.mainloop()
