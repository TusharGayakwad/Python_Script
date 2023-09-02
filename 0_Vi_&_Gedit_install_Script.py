import subprocess

n= str(input("update your PC(Y/N): ")).strip().upper()

if n=='Y':
	subprocess.run(['sudo', 'apt', 'update'])
	print("Update a succfully.")
	
	i = str(input("what you want Vi & gedit: ")).strip().upper()

	if i== 'VI':
        	subprocess.run(['sudo', 'apt', 'install','vi'])
        	subprocess.run(['vi','vesion'])
        	subprocess.run(['vi'])


	elif i== 'GEDIT':
        	subprocess.run(['sudo', 'apt', 'install','gedit'])
        	subprocess.run(['gedit','vesion'])
        	subprocess.run(['gedit'])

	else:
        	 print("Invalid input, Please enter the 'Vi' or 'Gedit' .")

elif n=='N':
	print("Not Update performed.")

else:
	print("Invalid input, Please enter the 'Y' or 'N' .")
