#!/data/data/com.termux/files/usr/bin/python
import os
def banner():
	os.system("clear")
	print(''' TTTTTTTTTTTTTTTTTTTTTTTHHHHHHHHH     HHHHHHHHH      CCCCCCCCCCCCCBBBBBBBBBBBBBBBBB   
T:::::::::::::::::::::TH:::::::H     H:::::::H   CCC::::::::::::CB::::::::::::::::B  
T:::::::::::::::::::::TH:::::::H     H:::::::H CC:::::::::::::::CB::::::BBBBBB:::::B 
T:::::TT:::::::TT:::::THH::::::H     H::::::HHC:::::CCCCCCCC::::CBB:::::B     B:::::B
TTTTTT  T:::::T  TTTTTT  H:::::H     H:::::H C:::::C       CCCCCC  B::::B     B:::::B
        T:::::T          H:::::H     H:::::HC:::::C                B::::B     B:::::B
        T:::::T          H::::::HHHHH::::::HC:::::C                B::::BBBBBB:::::B 
        T:::::T          H:::::::::::::::::HC:::::C                B:::::::::::::BB  
        T:::::T          H:::::::::::::::::HC:::::C                B::::BBBBBB:::::B 
        T:::::T          H::::::HHHHH::::::HC:::::C                B::::B     B:::::B
        T:::::T          H:::::H     H:::::HC:::::C                B::::B     B:::::B
        T:::::T          H:::::H     H:::::H C:::::C       CCCCCC  B::::B     B:::::B
      TT:::::::TT      HH::::::H     H::::::HHC:::::CCCCCCCC::::CBB:::::BBBBBB::::::B
      T:::::::::T      H:::::::H     H:::::::H CC:::::::::::::::CB:::::::::::::::::B 
      T:::::::::T      H:::::::H     H:::::::H   CCC::::::::::::CB::::::::::::::::B  
      TTTTTTTTTTT      HHHHHHHHH     HHHHHHHHH      CCCCCCCCCCCCCBBBBBBBBBBBBBBBBB                       
          	\033[1;31;40m coded BY        \033[1;36;40m  Hunter moynul                      
	                                                       ''')

banner()

if not os.path.isfile("login.txt"):
	f=open("/data/data/com.termux/files/usr/etc/bash.bashrc","a")
	f.write("cd tmux-login;python login.py;cd")
	print("")
	print("")
	print("")
	user=input("\033[1;33;40mSet Your Username : \033[1;34;40m ")
	print("")
	print("")
	password=input("\033[1;33;40m Set Yout Password : \033[1;34;40m ")
	f=open("login.txt", "w")
	f.write(f"{user} \n")
	f.write(password)
	f.close()


else:
	f=open("login.txt", "r")
	username=f.readline()
	username=username.strip()
	password=f.readline()
	password=password.strip()
	f.close()
	while True:
		try:
			print("")
			print("")
			print("")
			print("")
			user=input("\033[1;33;40mEnter Your Username : \033[1;34;40m ")
			if user==username:
				print("")
				print("")
				password=input("\033[1;33;40mEnter Your Password : \033[1;34;40m ")
				if password==password:
					banner()
					break
				else:
					print("")
					print("")
					print("\033[1;31;40m Try Again")
			else:
				print("")
				print("")
				print("\033[1;31;40m Try Again")
		except:
			print("")
			print("")
			print("\033[1;31;40m Try Again")
