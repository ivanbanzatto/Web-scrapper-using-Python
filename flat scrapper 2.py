# This code only reads from a specific website and prints in the console, the plan is to dump the data into a DB or a sheet
# Tasks already created in a project, ETA Apr 2024
#
#

from bs4 import BeautifulSoup
import requests


with open("barao.html", "rb") as file:
	doc = file.read()
	result = BeautifulSoup(doc, "lxml")

flat = {
        "codigo": None,
        "valor_aluguel": None,
        "valor_condominio": None,
        "localizacao": None,
        "tamanho": None,
        "link": None,
        "imobiliaria": None,
		"titulo": None
    		}

# this is the container that is each card
list_cards = result.find_all("div",class_="col-xs-12 grid-imovel")
print(len(list_cards)) # console print for verification


flats = []

for i in range(len(list_cards)):
	
    card = result.find_all("div",class_="col-xs-12 grid-imovel")[i] #get entire card

    flat["codigo"] = card.find(class_="imo-cod-floated").text
    flat["valor_aluguel"] = card.find(class_="thumb-price").text
    flat["valor_condominio"] = card.find(id="div-cond-iptu").span #fix this text
    flat["titulo"] = card.find(class_="titulo-grid").text
    flat["localizacao"] = card.find(itemprop="streetAddress").text
    flat["tamanho"] = card.find(class_="property-amenities amenities-main").span #fix this 
    flat["link"] = card.find("a")["href"]
    flat["titulo"] = card.find(class_="titulo-anuncio hidden-xs").h3.text

    flats.append(flat)

    print("Flat: ",i,"\nValues: ",flat.values())

#print("\nFlats: ",flats)




#####################################################################################
#
# TO DO list
# 1. work with pagination on websites 
# 2. scrappe other websites
# 3. write on DB, sheets or SQL
# 4. fix small scrapping tags issues
# 5. 
#
#
#
#
