import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import webbrowser


def make_file():
    nome_file = nome_file_entry.get()
    testo_preimpostato = "#!/bin/bash\nmkdir BTCPayServer\ncd BTCPayServer\ngit clone https://github.com/btcpayserver/btcpayserver-docker\ncd btcpayserver-docker\nexport BTCPAYGEN_REVERSEPROXY="+ '"'+ "nginx" + '"'+ '\nexport BTCPAY_ENABLE_SSH="'+'true'+'"'
    tickbox_count = 0
    testo_preimpostato += '\nexport BTCPAY_HOST='+'"'+nome_file + '"'
    if tickbox2.get():
        tickbox_count += 1
        testo_preimpostato += f'\nexport NBITCOIN_NETWORK="mainnet"\nexport BTCPAYGEN_CRYPTO'+str(tickbox_count)+"="+'"btc"'
    if tickbox1.get():
        tickbox_count += 1
        testo_preimpostato += f"\nexport BTCPAYGEN_CRYPTO"+str(tickbox_count)+"="+'"xmr"'
    if tickbox3.get():
        tickbox_count += 1
        testo_preimpostato += f"\nexport BTCPAYGEN_CRYPTO"+str(tickbox_count)+"="+'"dash"'
    if tickbox4.get():
        tickbox_count += 1
        testo_preimpostato += f"\nexport BTCPAYGEN_CRYPTO"+str(tickbox_count)+"="+'"doge"'
    if tickbox5.get():
        tickbox_count += 1
        testo_preimpostato += f"\nexport BTCPAYGEN_CRYPTO"+str(tickbox_count)+"="+'"ltc"'
    if tickbox6.get():
        tickbox_count += 1
        testo_preimpostato += f"\nexport BTCPAYGEN_CRYPTO"+str(tickbox_count)+"="+'"mona"'
    if tickbox7.get():
        tickbox_count += 1
        testo_preimpostato += f"\nexport BTCPAYGEN_CRYPTO"+str(tickbox_count)+"="+'"btg"'
    if tickbox8.get():
        tickbox_count += 1
        testo_preimpostato += f"\nexport BTCPAYGEN_CRYPTO"+str(tickbox_count)+"="+'"xbc"'
    if tickbox9.get():
        tickbox_count += 1
        testo_preimpostato += f"\nexport BTCPAYGEN_CRYPTO"+str(tickbox_count)+"="+'"via"'


    if radio_var.get() == 1:
        testo_preimpostato += '\nexport BTCPAYGEN_ADDITIONAL_FRAGMENTS="opt-save-storage-xxs"'
    elif radio_var.get() == 2:
        testo_preimpostato += '\nexport BTCPAYGEN_ADDITIONAL_FRAGMENTS="opt-save-storage-xs"\nexport BTCPAYGEN_LIGHTNING="clightning"'
    elif radio_var.get() == 3:
        testo_preimpostato += '\nexport BTCPAYGEN_ADDITIONAL_FRAGMENTS="opt-save-storage-s"\nexport BTCPAYGEN_LIGHTNING="clightning"'
    elif radio_var.get() == 4:
        testo_preimpostato += ""
        if dropdown_var.get() == "LND":
            testo_preimpostato += '\nexport BTCPAYGEN_LIGHTNING="lnd"'
        elif dropdown_var.get() == "Eclair":
            testo_preimpostato += '\nexport BTCPAYGEN_LIGHTNING="lnd"\nexport BTCPAYGEN_ADDITIONAL_FRAGMENTS="opt-txindex"'
    if check_var1.get():
        cdp = text_entry1.get()
        new_daemon_address = cdp
        testo_preimpostato += '\nnew_daemon_address ='+'"'+ new_daemon_address +'"'+ '\'\ncd docker-compose-generator/docker-fragments/\nsed -i "s/--daemon-address=monerod:18081/--daemon-address=$new_daemon_address/g" monero.yml'

    for i in range(36):
        listspecial = [12,15]
        if checkbox_vars[i].get() and i not in listspecial:
            print(i)
            testo_preimpostato += '\nBTCPAYGEN_ADDITIONAL_FRAGMENTS='+'"'+addFragments[i]+'"'

    file_path = filedialog.asksaveasfilename(defaultextension=".sh", filetypes=[("Bash file", "*.sh")])

    if file_path:
        with open(file_path, 'w') as file:
            file.write(testo_preimpostato)

        conferma_label.config(text=f"Successfuly saved file: {file_path}")


def open_linkENVar(event):
    webbrowser.open_new("https://docs.btcpayserver.org/Docker/#under-the-hood")

def on_mousewheel(event):
    canvas.yview_scroll(int(-1*(event.delta/120)), "units")

def seleziona_dropdown(event):
    if radio_var.get() == 4:
        if dropdown_var.get() == "Option 1":
            add_line_label.config(text="")
        elif dropdown_var.get() == "Option 2":
            add_line_label.config(text="")
    else:
        add_line_label.config(text="")



def enable_text_entry1():
    if check_var1.get():
        text_entry1.config(state=tk.NORMAL)
    else:
        text_entry1.delete(0, tk.END)
        text_entry1.config(state=tk.DISABLED)


def on_mousewheel(event):
    canvas.yview_scroll(int(-1*(event.delta/120)), "units")


def manage_dropdown_visibility(*args):
    if radio_var.get() == 4:
        dropdown_label.pack()
        dropdown_menu.pack()
    else:
        dropdown_label.pack_forget()
        dropdown_menu.pack_forget()
        add_line_label.config(text="")  # hide text when option is not chosen

def toggle_text_entry(entry, var):
    if var.get():
        entry.config(state=tk.NORMAL)
    else:
        entry.delete(0, tk.END)
        entry.config(state=tk.DISABLED)

def toggle_text_entry(var):
    for i, entry in enumerate(entry_widgets):
        if checkbox_vars[i] is var:
            if var.get():
                entry.config(state=tk.NORMAL)
            else:
                entry.delete(0, tk.END)
                entry.config(state=tk.DISABLED)
    canvas.update_idletasks()




addFragments = ["opt-lnd-autocompact", "opt-lnd-autopilot", "opt-lnd-keysend","opt-lnd-wtclient","opt-lnd-watchtower","opt-save-memory","opt-more-memory","opt-add-btcqbo","opt-add-librepatron","opt-add-woocommerce","opt-add-tor","opt-add-btctransmuter","opt-txindex","opt-expose-unsafe","opt-add-tor-relay","opt-add-electrumx","opt-add-electrum-ps","opt-add-electrum-bwt","opt-add-configurator","opt-add-pihole","opt-add-bluewallet-lndhub","opt-add-ndlc","opt-add-lightning-terminal","opt-add-mempool","opt-add-sphinxrelay","opt-add-thunderhub","opt-add-teos","opt-add-chatwoot","opt-add-zammad","opt-monero-expose","opt-add-fireflyiii","opt-add-joinmarket","opt-add-helipad","opt-add-nostr-relay","opt-add-cloudflared","opt-add-torq"]
# Main window
root = tk.Tk()
root.title("Btc Pay server install script GUI generator")

# tabs
schede = ttk.Notebook(root)

# domain name
tab_campi = ttk.Frame(schede)
schede.add(tab_campi, text="Domain name")

tk.Label(tab_campi, text="Host domain:").pack()
nome_file_entry = tk.Entry(tab_campi)
nome_file_entry.pack()

# crypto tickboxes
tab_tickbox = ttk.Frame(schede)
schede.add(tab_tickbox, text="Cryptos")



#  Checkbutton
tickbox1 = tk.BooleanVar()
tickbox2 = tk.BooleanVar()
tickbox3 = tk.BooleanVar()
tickbox4 = tk.BooleanVar()
tickbox5 = tk.BooleanVar()
tickbox6 = tk.BooleanVar()
tickbox7 = tk.BooleanVar()
tickbox8 = tk.BooleanVar()
tickbox9 = tk.BooleanVar()

# labels
tk.Label(tab_tickbox, text="Chose the crypto you want to support:").grid(row=0, column=0, columnspan=3)
tk.Label(tab_tickbox, text="Please keep in mind each additional coin requires more space, RAM, and CPU power").grid(row=1, column=0, columnspan=3)

# checkboxes texts
checkboxes = [
    ("XMR", tickbox1),
    ("BTC", tickbox2),
    ("DASH", tickbox3),
    ("DOGE", tickbox4),
    ("LTC", tickbox5),
    ("MONA", tickbox6),
    ("BTG", tickbox7),
    ("XBC", tickbox8),
    ("VIA", tickbox9)
]


# lightning
tab_sinistra = ttk.Frame(schede)
schede.add(tab_sinistra, text="Lightning Support")

radio_var = tk.IntVar()
radio_var.set(1)  # default value

tk.Radiobutton(tab_sinistra, text="No lightning support(Best for saving disk space)", variable=radio_var, value=1).pack()
tk.Radiobutton(tab_sinistra, text="Support channels up to 3 months old", variable=radio_var, value=2).pack()
tk.Radiobutton(tab_sinistra, text="Support channels up to 6 months old", variable=radio_var, value=3).pack()
tk.Radiobutton(tab_sinistra, text="Download whole chain,required for LND or Eclair lightning implementations", variable=radio_var, value=4).pack()


# Dropdown per la quarta opzione dei radio button
dropdown_var = tk.StringVar()
dropdown_var.set("Lnd")  # defaul value
dropdown_label = tk.Label(tab_sinistra, text="Choose the requested lightning implementation:")
dropdown_label.pack()

dropdown_menu = ttk.Combobox(tab_sinistra, textvariable=dropdown_var, values=["LND", "Eclair"])
dropdown_menu.pack()


add_line_label = tk.Label(tab_sinistra, text="")
add_line_label.pack()




radio_var.trace_add("write", manage_dropdown_visibility)



manage_dropdown_visibility()



for i, (text, variable) in enumerate(checkboxes):
    row = i // 3 + 2  # Inizia dalla terza riga, aggiungendo 2 per le prime due etichette
    col = i % 3
    tk.Checkbutton(tab_tickbox, text=text, variable=variable).grid(row=row, column=col)



entry_widgets = []




tab_envar = ttk.Frame(schede)
schede.add(tab_envar, text="Additional enn var")

canvas = tk.Canvas(tab_envar)
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

frame = tk.Frame(canvas)
canvas.create_window((0, 0), window=frame, anchor=tk.NW)

scrollbar = ttk.Scrollbar(tab_envar, orient=tk.VERTICAL, command=canvas.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
canvas.config(yscrollcommand=scrollbar.set)

frame.bind("<Configure>", lambda event, canvas=canvas: canvas.configure(scrollregion=canvas.bbox("all")))
corg = 0
# Checkbuttons variables
checkbox_vars = [tk.BooleanVar() for _ in range(36)]
# Place checkbutton in 2 columns
for i in range(36):
    var = checkbox_vars[i]
    corg += 1
    checkbox = tk.Checkbutton(frame, text=f"{addFragments[i]}", variable=var, command=lambda v=var: toggle_text_entry(v))
    if corg <= 3:
        checkbox.grid(row=i, column=0, padx=10, pady=5)
    elif corg <= 6:
        checkbox.grid(row=(i-3), column=1, padx=10, pady=5)
    else:
        corg = 0

root.bind("<MouseWheel>", on_mousewheel)  # let mouse wheel control scrollbar

entext = tk.Label(tab_envar, text="Additional option for expert users only\n Click here to read more about it", cursor="hand2")
entext.pack()

canvas.update_idletasks()
entext.bind("<Button-1>", open_linkENVar)


#tab additional options
tab_addopt = ttk.Frame(schede)
schede.add(tab_addopt, text="Additional options")

# Variabili per i Checkbutton
check_var1 = tk.BooleanVar()


# Checkbutton 1
checkbutton1 = tk.Checkbutton(tab_addopt, text="Custom XMR node", variable=check_var1, command=enable_text_entry1)
checkbutton1.grid(row=0, column=0, padx=10, pady=10)

# Casella di testo 1
text_entry1 = tk.Entry(tab_addopt, state=tk.DISABLED)
text_entry1.grid(row=0, column=1, padx=10, pady=10)
tk.Label(tab_addopt, text="Ip/hostname:port").grid(row=0, column=2, columnspan=3)


# Button
conferma_label = tk.Label(root, text="")
conferma_label.pack()


# dropdown choice label
aggiungi_linea_label = tk.Label(root, text="")
aggiungi_linea_label.pack()

make_file = tk.Button(root, text="Save install script", command=make_file)
make_file.pack()

schede.pack()

root.mainloop()
