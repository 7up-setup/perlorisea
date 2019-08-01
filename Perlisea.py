#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Author 7up#0001 and UrxuDotCom#8468 aka @perlise._ (instagram)


import os
import time
import urllib
import requests
from bs4 import BeautifulSoup
from terminaltables import SingleTable
import requests
import sys
import colorama
from colorama import init, Fore,  Back,  Style

r = requests.get("https://www.youtube.com")
print(r.text)

print("\r")
print("\r")
author = ("Authors")
warning = ("WARNING")
agree = ("AGREE")
error = ("ERROR")
version = ("Version")
name = ("UrxuDotCom#8468")
answ = ("$")
un = ("1")
deux = ("2")
trois = ("3")
quatre = ("4")
cent = ("100")
star = ("*")
#bannière

if sys.platform == 'linux2':
	os.system('clear')

elif sys.platform == 'win32':
	os.system('cls')



time.sleep(2.0)
#MENU
def retourmenu():
	if sys.platform == 'linux2':
				os.system('clear')

	elif sys.platform == 'win32':
		os.system('cls')
	print("\r")
	print("\r")

	print("                                          _________________________")
	print("    _ \          | _)                    | {"+Fore.YELLOW + Style.BRIGHT + version +Fore.RESET+"}: 1.0.0        |")
	print("    __/ -_)   _| |  | (_-<   -_)   _` |  | {" + Fore.BLUE + Style.BRIGHT + author + Fore.RESET + "}: Perlise, 7up | ")
	print("   _| \___| _|  _| _| ___/ \___| \__,_|  |_________________________|")
	print("                                      ")

	print(" |!|" + Fore.WHITE + Back.RED + Style.BRIGHT + warning + Back.RESET + Fore.RESET +"|!| I am not responsible of your actions |!|"+ Fore.WHITE + Back.RED + warning + Fore.RESET + Back.RESET +"|!|")
	print("\r")
	print("["+ Fore.YELLOW + un + Fore.RESET + "] - Name Search")
	print("["+ Fore.YELLOW + deux + Fore.RESET + "] - Phone Search (use fax for best results)")
	print("["+ Fore.YELLOW + trois + Fore.RESET + "] - Username Search")
	print("["+ Fore.YELLOW + quatre + Fore.RESET + "] - Join our discord server")
	print("\r")
	print("["+ Fore.YELLOW + cent + Fore.RESET +"] - Clear Terminal")
	print("\r")
	choice = input(":"+ Fore.RED + answ + Fore.RESET + "> ")

	if choice == "1":

		Ville = input("Ville : ")
		personne = input("Personne : ")
		print("["+ Fore.MAGENTA + star + Fore.RESET + "] Recherche pour ( " + personne + " à "+ Ville +" ) en cours ....")
		headers = {
				'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
	    	    'referrer': 'https://google.com',
	        	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
	        	'Accept-Encoding': 'utf-8',
	        	'Accept-Language': 'en-US,en;q=0.9',
	        	'Pragma': 'no-cache'
	        }

		url=("https://www.pagesjaunes.fr/recherche/"+Ville+"/"+personne)
		requete = requests.get(url, headers=headers)
		page = requete.content
		features="html.parser"
		soup = BeautifulSoup(page)	
		try:
			nameList = soup.find_all("a", {"class": "denomination-links pj-lb pj-link"})
			addressList = soup.find_all("a", {"class": "adresse pj-lb pj-link"})
			numList = soup.find_all("strong", {"class": "num"})
		except AttributeError:
			pass

		namesList2 = []
		addressesList2 = []
		numesList2 = []
		operatorList = []

		# try:
		for name in nameList:
			namesList2.append(name.text.strip())
		for addresse in addressList:
			addressesList2.append(addresse.text.strip())
		for num in numList: 
			numesList2.append(num.text.strip())

		regroup = zip(namesList2,addressesList2,numesList2)
		
		title = " Particulier "

		TABLE_DATA = [
			('Name', 'Adresse', 'Phone'),
		]

		listeInfos = []

		for infos in regroup:
			
			try:

				TABLE_DATA.append(infos)

			except AttributeError:
				pass

		table_instance = SingleTable(TABLE_DATA, title)
		if sys.platform == 'linux2':
				os.system('clear')

		elif sys.platform == 'win32':
				os.system('cls')

		print("["+ Fore.MAGENTA + star + Fore.RESET + "] Resultat pour ( " + personne + " à "+ Ville +" ) en cours ....")
		print("\n"+table_instance.table)
		input("[*]>>Retournez au menu ")
		retourmenu()

		#debut code person seach
	elif choice == "2":
		num = input("Search a phone number : ")
		print("["+ Fore.MAGENTA + star + Fore.RESET + "] Recherche pour ( " + num + " ) en cours ....")
		time.sleep(1.0)
		headers = {
				'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
	    	    'referrer': 'https://google.com',
	        	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
	        	'Accept-Encoding': 'utf-8',
	        	'Accept-Language': 'en-US,en;q=0.9',
	        	'Pragma': 'no-cache'
	        }
		url = ("https://www.pagesjaunes.fr/annuaireinverse/recherche?quoiqui=")
		requete = requests.get(url+num, headers=headers)
		

		page = requete.content
		features="html.parser"
		soup = BeautifulSoup(page)	
		try:
			nameList = soup.find_all("a", {"class": "denomination-links pj-lb pj-link"})
			addressList = soup.find_all("a", {"class": "adresse pj-lb pj-link"})
			numList = soup.find_all("strong", {"class": "num"})
		except AttributeError:
			pass

		namesList2 = []
		addressesList2 = []
		numesList2 = []
		operatorList = []

		# try:
		for name in nameList:
			namesList2.append(name.text.strip())
		for addresse in addressList:
			addressesList2.append(addresse.text.strip())
		for num in numList: 
			numesList2.append(num.text.strip())

		regroup = zip(namesList2,addressesList2,numesList2)
		
		title = " Particulier "

		TABLE_DATA = [
			('Name', 'Adresse', 'Phone'),
		]

		listeInfos = []

		for infos in regroup:
			
			try:

				TABLE_DATA.append(infos)

			except AttributeError:
				pass

		table_instance = SingleTable(TABLE_DATA, title)
		if sys.platform == 'linux2':
				os.system('clear')

		elif sys.platform == 'win32':
			os.system('cls')
		print("["+ Fore.MAGENTA + star + Fore.RESET + "] Resultat pour ( " + num + " ) en cours ....")
		print("\n"+table_instance.table)
		input("[*]>>Retournez au menu ")
		retourmenu()

	elif choice == "3":
		id = input("Search an username : ")
		print("\n["+ Fore.MAGENTA + star + Fore.RESET + "] Searching for ( "+ id +" ) in progress ...")
		time.sleep(1.0)
		#debut code username search
	elif choice == "4":
		print("Invitation : https://discord.gg/JSaADXF")
		input("[*]>> Retournez au menu !")
		retourmenu()
	elif choice == "100":
		retourmenu()
	else:
		print("|!| "+ Fore.WHITE + Back.RED + error + Fore.RESET + Back.RESET +" |!| Type a correct number ...")

		time.sleep(2.0)
		if sys.platform == 'linux2':
			os.system('clear')

		elif sys.platform == 'win32':
			os.system('cls')
		retourmenu()
retourmenu()	