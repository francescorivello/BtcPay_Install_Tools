# BtcPay Server install tool
This is a set of python scripts intend to facilitate the installation of a BtcPay server istance
for people less accustomed to the use of the console or the bash enviroments
It is divided in 3 three scripts

# CliSetup.py
This setup is meant to be used directly on the target server,it is a guided setup in wich the user will need to input the domain and other datas while also choosing with checkboxes the coin/features it want to support
The Cli setup differentiate itself from the gui counterpart by having a dynamic Ram/hdd space requirements counter wich (approximately) tracks ram and space usage of the selected cryptos and warn the user if their selection could cause instability or problems
# GuiSetup.py
This is the Gui version and is meant to be used on wider range of scenarios,delivering the easiest experince of setup,it is divided in different tabs each one with checkboxes or empty entries to fill
At the end you will be able to save a .sh bash script wich can either be used by the user itself on the target machine,or ran by the remote installer.
# RemoteInstaller.py
This python script help user to run the generated bash script on the target machine,it supports both public key auth and user/password based authentication,after filling the required entries you can run it,it will connect to the target host and run the script,if it encounters any error it will output it,and if everything work it will also confirm it to the user

# Basic functionality of the two setup tools  
 Both tools,excluded for some differences like the resource usage meter on the cli version,offer the same options such as:
- Choosing domain name
- Choosing the required Lightning network implementation
- Support for all the additional enviroments variable of btcpay server,tough this are considered as for advanced users and there will be no informations on them inside the scripts except for a link wich points to the official documentation in the gui script
- Support for custom xmr node(TBA very soon in the cli script)
