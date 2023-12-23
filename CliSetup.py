import  time, curses, os
import psutil, shutil


cnum=0

coin_requirements = {'btc': (1.5, 7), 'xmr': (1.5, 75), 'ltc': (1.5, 7), 'btg': (1.5, 7),
                     'xbc (pruning not supported high storage requirements)': (1.5, 400), 'btx': (1.5, 7),
                     'dash': (1.5, 40),
                     'doge': (1.5, 7),
                     'ftc': (1.5, 7), 'grs': (1.5, 7), 'html': (1.5, 7), 'lbtc': (1.5, 7),
                     'mona': (1.5, 7),
                     'polis': (1.5, 7), 'via': (1.5, 7)}

coin_list = ["btc", "xmr", "ltc", "btg", "xbc", "btx",
             "dash", "doge", "ftc", "grs", "lbtc",
             "mona", ]
addFragments = ["custom XMR node","opt-lnd-autocompact",
                "opt-lnd-autopilot", "opt-lnd-keysend",
                "opt-lnd-wtclient","opt-lnd-watchtower","opt-save-memory","opt-more-memory","opt-add-btcqbo","opt-add-librepatron","opt-add-woocommerce","opt-add-tor","opt-add-btctransmuter","opt-txindex","opt-expose-unsafe","opt-add-tor-relay","opt-add-electrumx","opt-add-electrum-ps","opt-add-electrum-bwt","opt-add-configurator","opt-add-pihole","opt-add-bluewallet-lndhub","opt-add-ndlc","opt-add-lightning-terminal","opt-add-mempool","opt-add-sphinxrelay","opt-add-thunderhub","opt-add-teos","opt-add-chatwoot","opt-add-zammad","opt-monero-expose","opt-add-fireflyiii","opt-add-joinmarket","opt-add-helipad","opt-add-nostr-relay","opt-add-cloudflared","opt-add-torq"]
cxmr = "custom XMR node"
def get_size(bytes, suffix="B"):
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor


def gather_ram():
    svmem = psutil.virtual_memory()
    avmem = get_size(svmem.available)
    return avmem


def gather_storage():
    path="/root"
    pathwin="C:\\"
    if os.name == "nt":
        av_space = get_size(shutil.disk_usage(pathwin)[2])
    else:
        av_space = get_size(shutil.disk_usage(path)[2])
    return av_space





print("Btc Pay easy installer by WanderingPi\n")
time.sleep(1.25)
print(
    "This program is intendend to assist you in setting up and using an istance of BtcPay server,\n"
    "you will be asked some questions about you current configuration and how you gonna utilize your server\n\n")
time.sleep(3)





print("Write down the domain at which your site should be accessed at, e.g btcpay.mydomain.com\n"
      "Remember to create an A record pointing to the vps or server you are using\n"
      "And a CNAME record if you want to use a subdomain\n\nPRESS ENTER TO CONTINUE\n\n")
input()

domain = input("Your BtcPay Server domain:")

lightning_mode=int(input("\n\n Do you want to enable lighning?\n"
      "0. No (7gb of hdd space required for most coins)\n"
      "1. Yes supporting up to 3 months old lightning channels trough clightning(around 27gb disk space required)\n"
      "2. Yes supporting up to 6 months old lightning channels trough clightning(around 55gb disk space required)\n"
      "3. Yes with full sync,required to usd LND or eclair implementations\n"
      ":"               ))
if lightning_mode == 3:
    ln_impl = int(input("Chose the implementation you want to use\n"
                    "4. LND\n"
                    "5. ECLAIR\n"
                    ":"))
    coin_requirements = {'btc': (1.5, 520), 'xmr': (1.5, 75), 'ltc': (1.5, 125), 'btg': (520, 520),
                         'xbc (pruning not supported high storage requirements)': (1.5, 520), 'btx': (1.5, 15),
                         'dash': (1.5, 40),
                         'doge': (1.5, 85),
                         'ftc': (1.5, 20), 'grs': (1.5, 55), 'html': (1.5, 55), 'lbtc': (1.5, 520),
                         'mona': (1.5, 15),
                         'polis': (1.5, 15), 'via': (1.5, 15)}
elif lightning_mode == 1:
    coin_requirements = {'btc': (1.5, 27), 'xmr': (1.5, 75), 'ltc': (1.5, 27), 'btg': (1.5, 27),
                         'xbc (pruning not supported high storage requirements)': (1.5, 400), 'btx': (1.5, 15),
                         'dash': (1.5, 40),
                         'doge': (1.5, 27),
                         'ftc': (1.5, 15), 'grs': (1.5, 15), 'html': (1.5, 15), 'lbtc': (1.5, 27),
                         'mona': (1.5, 15),
                         'polis': (1.5, 15), 'via': (1.5, 15)}
elif lightning_mode == 2:
    coin_requirements = {'btc': (1.5, 55), 'xmr': (1.5, 75), 'ltc': (1.5, 55), 'btg': (1.5, 55),
                         'xbc (pruning not supported high storage requirements)': (1.5, 400), 'btx': (1.5, 15),
                         'dash': (1.5, 40),
                         'doge': (1.5, 55),
                         'ftc': (1.5, 20), 'grs': (1.5, 5), 'html': (1.5, 5), 'lbtc': (1.5, 55),
                         'mona': (1.5, 15),
                         'polis': (1.5, 15), 'via': (1.5, 15)}
#print(coin_requirements.items())
time.sleep(0)
print("\n\nPlease select the coin you want to support on your server,move with the up and down arrow keys\n"
      "and press enter to select the desired crypto,when all the needed selections\n"
      "are made go down to exit and press enter to proceed into the setup\nestimated ram and disk usage will also be shown\nplease consider this data may vary with time\n"
      "PRESS ENTER TO CONTINUE")
input()

def cselect(stdscr, checkbox_values=coin_requirements):

    selected_item = 0
    checkboxes = ["btc", "xmr", "ltc", "btg", "xbc (pruning not supported high storage requirements)", "btx",
                  "dash", "doge", "ftc", "grs", "lbtc",
                  "mona", "via", "exit"]
    checkbox_states = [False] * len(checkboxes)
    ram_usage = 0
    disk_usage = 0
    required_coins = []
    warning_message = ""
    r = float(gather_ram()[:-2])
    d = float(gather_storage()[:-2])
    while True:
        stdscr.clear()


        for i, item in enumerate(checkboxes):
            if i == selected_item:
                stdscr.addstr(i, 0, "X " if checkbox_states[i] else "O ")
            else:
                stdscr.addstr(i, 0, "> " if checkbox_states[i] else "  ")
            stdscr.addstr(item)


        stdscr.addstr(len(checkboxes), 0, f"RAM Usage: {ram_usage} / {gather_ram()[:-2]} GB")
        stdscr.addstr(len(checkboxes) + 1, 0, f"Disk Usage: {disk_usage} / {gather_storage()[:-2]} GB")

        stdscr.refresh()

        if ram_usage > r or disk_usage > d:
            warning_message = (
                "WARNING:Estimated ram or disk usage is over the available resource of the system\n                      "
                "        it is advised to deselect some coin or upgrade the system")
        else:
            warning_message = ""
        stdscr.addstr(0, 22, warning_message)

        stdscr.refresh()

        key = stdscr.getch()
        if key == curses.KEY_DOWN:
            selected_item = (selected_item + 1) % len(checkboxes)
        elif key == curses.KEY_UP:
            selected_item = (selected_item - 1) % len(checkboxes)
        elif key == 10:
            if selected_item == len(checkboxes) - 1:
                break
            checkbox_name = checkboxes[selected_item]
            checkbox_states[selected_item] = not checkbox_states[selected_item]
            if checkbox_name in checkbox_values:
                delta_ram, delta_disk = checkbox_values[checkbox_name]
                if checkbox_states[selected_item]:
                    ram_usage += delta_ram
                    disk_usage += delta_disk
                    required_coins.append(checkbox_name)
                else:
                    ram_usage -= delta_ram
                    disk_usage -= delta_disk
                    required_coins.remove(checkbox_name)
        elif key == 27:
            break
    return ram_usage, disk_usage, required_coins

data1 = curses.wrapper(cselect)
while data1[0] > float(gather_ram()[:-2]) or data1[1] > float(gather_storage()[:-2]):
    print("\n\n\n\nWarning current selction may cause stability issue,do you want to continue or\n"
          "chose a different set of supported cryptos?")
    dec =input(print("Type y to continue setup\n"
                   "type n to revert to coin choosing:"))
    if dec == "n":
        data1=curses.wrapper(cselect)
    elif dec == "y":
        break
    else:
        print("Wrong letter inserted\n\n")
cl = data1[2]

def foptselect(stdscr, checkbox_values=addFragments):

    selected_item = 0
    checkboxes = ["custom XMR node","opt-lnd-autocompact","opt-lnd-autopilot","opt-lnd-keysend","opt-lnd-wtclient","opt-lnd-watchtower","opt-save-memory","opt-save-memory","opt-add-btcqbo","opt-add-librepatron","opt-add-woocommerce","opt-add-tor","opt-add-btctransmuter","opt-add-txindex","opt-expose-usnafe","opt-add-tor-relay","opt-add-electrumx","opt-add-electrum-ps","opt-add-electrum-bwt","Go to page 2"]
    checkbox_states = [False] * len(checkboxes)
    required_opt = []
    warning_message = ""
    while True:
        stdscr.clear()


        for i, item in enumerate(checkboxes):
            if i == selected_item:
                stdscr.addstr(i, 0, "X " if checkbox_states[i] else "O ")
            else:
                stdscr.addstr(i, 0, "> " if checkbox_states[i] else "  ")
            stdscr.addstr(item)


        stdscr.refresh()

        key = stdscr.getch()
        if key == curses.KEY_DOWN:
            selected_item = (selected_item + 1) % len(checkboxes)
        elif key == curses.KEY_UP:
            selected_item = (selected_item - 1) % len(checkboxes)
        elif key == 10:
            if selected_item == len(checkboxes) - 1:
                break
            checkbox_name = checkboxes[selected_item]
            checkbox_states[selected_item] = not checkbox_states[selected_item]
            if checkbox_name in checkbox_values:
                if checkbox_states[selected_item]:
                    required_opt.append(checkbox_name)
                else:
                    required_opt.remove(checkbox_name)
        elif key == 27:
            break
    return  required_opt

def soptselect(stdscr, checkbox_values=addFragments):

    selected_item = 0
    checkboxes = ["opt-add-configurator","opt-add-pihole","opt-add-bluewallet-lndhub","opt-add-ndlc","opt-add-lightning-terminal","opt-add-mempool","opt-add-sphinxrelay","opt-add-tallycoin-connect","opt-add-thunderhub","opt-add-teos","opt-monero-expose","opt-add-fireflyiii","opt-add-joinmarket","opt-add-heliapd","nostr-relay","opt-add-cloudflared","opt-add-torq","exit"]
    checkbox_states = [False] * len(checkboxes)
    required_opt = []
    warning_message = ""
    while True:
        stdscr.clear()


        for i, item in enumerate(checkboxes):
            if i == selected_item:
                stdscr.addstr(i, 0, "X " if checkbox_states[i] else "O ")
            else:
                stdscr.addstr(i, 0, "> " if checkbox_states[i] else "  ")
            stdscr.addstr(item)


        stdscr.refresh()

        key = stdscr.getch()
        if key == curses.KEY_DOWN:
            selected_item = (selected_item + 1) % len(checkboxes)
        elif key == curses.KEY_UP:
            selected_item = (selected_item - 1) % len(checkboxes)
        elif key == 10:
            if selected_item == len(checkboxes) - 1:
                break
            checkbox_name = checkboxes[selected_item]
            checkbox_states[selected_item] = not checkbox_states[selected_item]
            if checkbox_name in checkbox_values:
                if checkbox_states[selected_item]:
                    required_opt.append(checkbox_name)
                else:
                    required_opt.remove(checkbox_name)
        elif key == 27:
            break
    return  required_opt

data2 = curses.wrapper(foptselect)
print(data2)
if data2[0] == cxmr:
    print("Input your custom xmr node domain and press enter:")
    cnode = input(":")

data3 = curses.wrapper(soptselect)

with open("install.sh", "w") as file:
    fuse = False
    file.write("#!/bin/bash\n")
    file.write("mkdir BTCPayServer\n")
    file.write("cd BTCPayServer\n")
    file.write("git clone https://github.com/btcpayserver/btcpayserver-docker\n")
    file.write("cd btcpayserver-docker\n")
    file.write(f"export BTCPAY_HOST="+f'"{domain.strip()}"\n')
    if "btc" in cl:
        file.write("export NBITCOIN_NETWORK="+"\"mainnet"+"\"\n")
    else:
        time.sleep(0.01)
    try:
        if ln_impl == 4:
            file.write("export BTCPAYGEN_LIGHTNING=" + "\"lnd" + "\"\n")
        elif ln_impl == 5:
            file.write("export BTCPAYGEN_LIGHTNING=" + "\"eclair" + "\"\n")
            file.write("export BTCPAYGEN_ADDITIONAL_FRAGMENTS=" + "\"opt-txindex" + "\"\n")
    except:
        file.write("export BTCPAYGEN_LIGHTNING=" + "\"clightning" + "\"\n")
    for c in cl:
        cnum +=1
        file.write(f"export BTCPAYGEN_CRYPTO"+str(cnum)+"="+f'"{c}"\n')
    for n in data2:
        if n == cxmr:
            new_daemon_address = cnode
            fuse = True
        else:
            file.write(f"export BTCPAYGEN_ADDITIONAL_FRAGMENTS"+"="+f'"{n}"\n')
    for z in data3:
        file.write(f"export BTCPAYGEN_ADDITIONAL_FRAGMENTS"+"="+f'"{z}"\n')
    file.write("export BTCPAYGEN_ADDITIONAL_FRAGMENTS="+"\"opt-save-storage-xxs"+"\"\n")
    file.write("export BTCPAYGEN_REVERSEPROXY="+"\"nginx"+"\"\n")
    file.write("export BTCPAY_ENABLE_SSH="+"\"true"+"\"\n")
    if fuse:
        file.write('\nnew_daemon_address =' + '"' + new_daemon_address + '"' + '\'\ncd docker-compose-generator/docker-fragments/\nsed -i "s/--daemon-address=monerod:18081/--daemon-address=$new_daemon_address/g" monero.yml')
    file.write(". ./btcpay-setup.sh -i")
os.chmod("install.sh", 101)
print("install.sh written in current directory, run it using ./install.sh")
time.sleep(3)




