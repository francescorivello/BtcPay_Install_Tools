# BTCPay Install Tools

Questo progetto è stato iniziato come contributo per la **community open source della criptovaluta Monero (XMR)** tramite la piattaforma [Monero Bounties](https://bounties.monero.social/posts/77/10-052m-make-btcpay-server-configuration-accessible).  
Il lavoro è stato presentato con l’alias **WanderingPI**, e da lì è nato il fork di questa repository.  

BTCPay Install Tools è una suite di strumenti in **Python** per semplificare la configurazione e l’installazione di **BTCPay Server**.  
Il progetto fornisce tre modalità di utilizzo:  
- **CLI interattiva**  
- **Interfaccia grafica (GUI)**  
- **Installer remoto via SSH**  

L’obiettivo è permettere a utenti con diversi livelli di competenza di generare ed eseguire uno script di installazione personalizzato di BTCPay Server, riducendo errori manuali e accelerando il deployment.

---

## 📂 Componenti principali

### 1. `CliSetup.py`
- Installer basato su **riga di comando interattiva (CLI)** con supporto a `curses`.  
- Funzionalità:
  - Inserimento dominio host.  
  - Scelta del supporto **Lightning Network** (clightning, LND, Eclair).  
  - Selezione delle criptovalute supportate con calcolo automatico di RAM e spazio disco richiesti.  
  - Attivazione di **opzioni avanzate** (fragments Docker Compose).  
  - Creazione di uno script finale `install.sh` pronto da eseguire.  
- Include **check delle risorse disponibili** per evitare configurazioni che eccedano RAM o spazio disco.  

### 2. `GuiSetup.py`
- Interfaccia **grafica Tkinter** per utenti meno esperti.  
- Funzionalità:
  - Inserimento dominio e selezione criptovalute tramite checkbox.  
  - Configurazione Lightning Network (no LN, LN parziale, full node con LND/Eclair).  
  - Abilitazione di oltre 30 fragments opzionali (Electrum, Tor, Mempool, WooCommerce, ecc.).  
  - Configurazione di **nodo Monero personalizzato**.  
  - Generazione di uno script `.sh` salvabile in una directory a scelta.  

### 3. `RemoteInstaller.py`
- Strumento con GUI che permette di **installare BTCPay Server su un server remoto** via SSH.  
- Funzionalità:
  - Connessione SSH con password o chiave privata.  
  - Selezione dello script locale `install.sh` generato con CLI o GUI.  
  - Upload automatico sul server remoto ed esecuzione.  
  - Output dell’installazione mostrato in tempo reale.  

---

## 🚀 Flusso di utilizzo

1. **Preparazione**  
   - Decidi se utilizzare la **CLI** o la **GUI** per generare il file `install.sh`.  

2. **Generazione script**  
   - Inserisci dominio, criptovalute, supporto LN, fragments opzionali.  
   - Salva lo script personalizzato (`install.sh`).  

3. **Installazione**  
   - Opzione 1: esegui lo script localmente con `./install.sh`.  
   - Opzione 2: utilizza `RemoteInstaller.py` per caricarlo ed eseguirlo automaticamente su un server remoto via SSH.  

---

## 🛠️ Tecnologie utilizzate

- **Python 3.8+**  
- Librerie standard:  
  - `os`, `time`, `subprocess`, `shutil`, `curses` (CLI)  
  - `tkinter`, `ttk`, `filedialog`, `webbrowser` (GUI)  
- Librerie esterne:  
  - `psutil` (analisi risorse)  
  - `paramiko` (SSH remoto)  

---

## ⚙️ Requisiti

- **Sistema operativo:** Linux o Windows (con Python 3.8+)  
- **Dipendenze Python:**  

```bash
pip install -r requirements.txt


## Conclusione

Questo progetto unisce tre modalità di utilizzo (CLI, GUI e installazione remota) per facilitare il deployment di **BTCPay Server**.  
È un esempio concreto di:

- Sviluppo di interfacce CLI/GUI con Python
- Automazione di installazioni complesse
- Integrazione con SSH e gestione remota
- Attenzione a UX sia per utenti avanzati che principianti

> ### ⚠️ Nota importante
> 
> A causa di cambiamenti nel funzionamento interno di **BTCPay Server**, questo progetto è da considerarsi attualmente **deprecato**.



