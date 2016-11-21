import os
import sys
import urllib
import shutil
import os.path
import fileinput


""" WELCOME """
print"******************************"
print"*  Regionhax Installer v1.0  *"
print"******************************\n"
print"******************************"
print"*       16-nov-2016          *"
print"*                            *"
print"*   Script by Vickdu31       *"
print"* email : vickdu31@yahoo.fr  *"
print"******************************"
raw_input("Press enter to start...")
os.system('cls' if os.name == 'nt' else 'clear') 
print"**************************************"
print"*         DISCLAIMER :               *"
print"**************************************\n"
print"**************************************"
print"*  I AM NOT RESPONSIBLE FOR BRICK    *"
print"*    DO NOT MODIFY THIS TOOL         *"
print"*                                    *"
print"*  This tool have been tested a lot  *"
print"* It should be safe if you follow .  *"
print"**************************************"
raw_input("Press enter to continue...")
os.system('cls' if os.name == 'nt' else 'clear') 


""" ASK CONFIRMATION """
print"******************************"
print"*  Regionhax Installer v1.0  *"
print"******************************\n"
for retry in range(5):
    confirm = raw_input("Would you like to set your Wii U Region Free ? (y/n) ")
    if (confirm == 'y' or confirm == 'Y' or confirm == 'yes'):
        ansr = raw_input("Are you sure ? (y/n)  ")
        if (ansr == 'y' or ansr == 'Y' or ansr == 'yes'):
            break
    if (confirm == 'n' or confirm == 'N' or confirm == 'no' or confirm == 'NO'):
        ansr = raw_input("Are you sure ? (y/n)  ")
        if (ansr == 'y' or ansr == 'Y' or ansr == 'yes'):
            raw_input("Press enter to exit program....")
            sys.exit()
            break
    print "\nPlease decide.\n"
else:
    sys.exit(1)

""" ASK REGION """
os.system('cls' if os.name == 'nt' else 'clear') 
print"******************************"
print"*  Regionhax Installer v1.0  *"
print"******************************\n"
for retry in range(5):
    creg = raw_input("What is your console region ? (eur/us/jap) (IMPORTANT!!!) ")
    if (creg == 'eur' or creg == 'us' or creg == 'jap'):
        ansr = raw_input("Your console region is " + creg + ". Is that correct ? (y/n)  ")
        if (ansr == 'y' or ansr == 'Y' or ansr == 'yes'):
            break
    print "\nPlease enter values correctly.\n"
else:
    sys.exit(1)


""" IP FINDER FOR USER """
for retry in range(10):
    know_ip = raw_input("\nDo you have your Wii U IP adress somewhere ? (y/n)  ")
    if (know_ip == 'y' or know_ip == 'Y' or know_ip == 'yes' or know_ip == 'YES'):
        wiiuip = raw_input("Please write the Wii U Ip adress Ex :(192.168.x.x)\n").replace('\n', '')
        f = open('Your_Wii_U_IP.txt', 'w')
        f.write(wiiuip)
        f.close()
        break
    if (know_ip == 'n' or know_ip == 'N' or know_ip == 'no' or know_ip == 'NO'):
        print "Downloading WNetwatcher...(800KB)"
        urllib.urlretrieve('http://www.nirsoft.net/utils/wnetwatcher.zip', "wnetwatcher.zip")
        print "Please open the .exe and try to find the IP address of a Nintendo device Ex.(192.168.X.X)\nOnce you found it, press enter to continue\n"
        os.startfile('wnetwatcher.zip')
        raw_input("")
        wiiuip = raw_input("Please write the Wii U IP adress (192.168.x.x)\n").replace('\n', '')
        f = open('Your_Wii_U_IP.txt', 'w')
        f.write(wiiuip)
        f.close()
        break
    print "\nChoose beetween yes or no...\n"
else:
    sys.exit(1)

""" IP CHECK """
for retry in range(10):
    with open('Your_Wii_U_IP.txt', 'r') as ipfile:
        ipcheck = ipfile.read().replace('\n', '')
    ansr = raw_input("Your console IP adress is -->" + ipcheck + "<--  Is that correct ? (y/n)  ")
    if (ansr == 'y' or ansr == 'Y' or ansr == 'yes'):
        break
    wiiuip = raw_input("Please write the Wii U Ip adress. Use correct format : 192.168.x.x\n").replace('\n', '')
    f = open('Your_Wii_U_IP.txt', 'w')
    f.write(wiiuip)
    f.close()
else:
    sys.exit(1)


print "\n*  Initialise connexion  *\n"

from wupclient import wupclient
wupclient = wupclient()

print "*  If an error is displayed, your IP adress is wrong or the Wii U is not reachable  *\n"
raw_input("We are now connected to WUPServer on your Wii U, press enter when you are ready!")


""" FLASHING REGION FREE """

PATH8 = "/vol/system_slc/config/sys_prod.xml"
wupclient.dl(PATH8)
print "\n\n* File downloaded ! *"
from shutil import copyfile
copyfile('sys_prod.xml', 'sys_prod.xml.bak')
print "* Backup created ! *"
regionfile = 'sys_prod.xml'
with open(regionfile, 'r') as f:
  text = f.read()
if creg == 'eur':
    text = text.replace('>4</game_region>', '>119</game_region>')
if creg == 'us':
    text = text.replace('>2</game_region>', '>119</game_region>')
if creg == 'jap':
    text = text.replace('>1</game_region>', '>119</game_region>')        
with open(regionfile, 'w') as f:
  f.write(text)
  f.close()
print "* File edited ! *"
wupclient.up("sys_prod.xml", PATH8)
wupclient.kill()
print "* File uploaded ! *\n"
raw_input("Press enter to continue...")
os.system('cls' if os.name == 'nt' else 'clear') 


""" GOODBYE """  
print"******************************"
print"*  Regionhax Installer v1.0  *"
print"******************************\n"
print"******************************"
print"*Your Wii U is now Region Free*"
print"******************************\n"
print"******************************"
print"*    SHUTDOWN YOUR WII U     *"
print"*   Once program is closed   *"
print"*                            *"
print"*                            *"
print"*   Script by Vickdu31       *"
print"* email : vickdu31@yahoo.fr  *"
print"******************************"
raw_input("Press enter to continue...")
os.system('cls' if os.name == 'nt' else 'clear') 

""" CREDITS """ 
print"******************************"
print"*   Regionhax Installer v1.0  *"
print"******************************\n"        
print"**************************************"
print"*            CREDITS :               *"
print"**************************************\n"
print"**************************************"
print"*   @NETOOBUNTU for finding this!    *"
print"*   @smealum for iosuhax/wupserver   *"
print"  Everyone contribuing to WII U HACK *"
print"**************************************"
raw_input("Press enter to exit program...")
sys.exit()