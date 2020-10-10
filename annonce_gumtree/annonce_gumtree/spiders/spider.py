# -*- coding: utf-8 -*-
import pandas as pd
import scrapy
from annonce_gumtree.items import GumtreeItem
import re
class GumSpider(scrapy.Spider):
	name = 'gumtree_annonce_2020_09'
	allowed_domains = ['gumtree.co.za']
	#global tab_id_client
	#tab_id_client=[]
	start_urls=list(pd.read_csv("/home/h.mahmoudi/gumtree/annonce_gumtree/annonce_gumtree/spiders/GUmtree.csv")['url'])

	def correct(self,itm):
		itm = str(itm)
		itm = itm.replace("\r","")
		itm = itm.replace("-"," ")
		itm = itm.replace(","," ")
		itm = itm.replace(";"," ")
		itm = itm.replace("\t"," ")
		itm = itm.replace("\n","")
		itm = itm.replace("\r","")
		itm = itm.replace("\"","")
		itm = itm.replace("\'","")
		itm = itm.replace("+","")
		itm = itm.replace("(","")
		itm = itm.replace(")","")
		itm = itm.replace(".","")
		itm = itm.replace('None','')
		itm = itm.replace("  "," ")
		return itm

	def clean_tel(self,itm):
		itm = itm.replace(" ","")
		itm = itm.replace(".","")
		itm = itm.replace("-","")
		itm = itm.replace("/","")
		itm = itm.replace("(","")
		itm = itm.replace(")","")
		itm = itm.replace("+","")
		return itm


	def parse(self,response):
		ck= response.xpath("//span[@class='breadcrumbs']/span/a/span").extract() 
		if ck != None:
			item=GumtreeItem()
	#        print("details -------------------------------")
			telephone =""
			site="gumtree.co.za"
			url=response.url

			try:
				id_client=str(url).split("/")[-1]
				
			except:
				id_client=""


			try:
				contact_prenom=response.xpath("//span[@class='username']/a/text()").extract_first()


			except:
				contact_prenom=""


			try:

				nom=response.xpath("//h1[@class='item-title']/div[@class='title']/text()").extract_first()
			except:
				nom=""
			if nom == "":
				nom=response.xpath("//span[@class='myAdTitle']/text()").extract_first()
			else:
				nom=response.xpath("//div[@class='vip-summary']/div[@class='title']/h1/text()").extract_first()

			try:
				prix3=0
			   # prix1=0
			   # prix2=response.xpath("//div[@class='price']/span/span[@class='value']/span[@class='ad-price']/text()").extract()
			   # prix=response.xpath("//div[@class='vip-title clearfix']/div[@class='price']/span[@class='value']/span[@class='amount']/text()").extract_first()
				prix_final=""
				pr=response.xpath("//div[@class='price']/h3/span[@class='value wrapper']/span[@class='ad-price']/text()").extract_first().strip()
				if pr != []:
					prix3="".join(re.findall("\d+",pr))
				#if prix != []:
				#    prix1="".join(re.findall("\d+",prix))
				prix_final=prix3
			except:
				prix= "00"
			prix = prix_final
			print("-----------------------------",prix)
			try:
				nb_photo= response.xpath("//div[@class='gallery-toolkit']/div/span[@class='count']/text()").extract_first().split()[0]
				#nb_photo=response.xpath("//img/@data-index").extract()[-1]
				#if str(nb_photo) != "None" and str(nb_photo) != "":
				#    nb_photo= int(nb_photo)+1
				#else:
				#    nb_photo=0
			except:
				nb_photo=""

			try:
				#province=response.xpath("//div[@class='location']/a[@itemprop='addressRegion']/text()").extract_first()
				ville = response.xpath("//div/a[@itemprop='addressLocality']/text()").extract_first()
				departement = response.xpath("//div/a[@itemprop='addressRegion']/text()").extract_first()

				#province = response.xpath("//a[@class='category']/span[@itemprop='title']/text()").extract_first()
				province=response.xpath("//span[@class='breadcrumbs']/span[2]/a/span/text()").extract_first()
				if province is None :
					province=response.xpath("//div[@class='breadcrumbs']/span/a/span/text()").extract_first()
			except:
				province=""
				ville =""
				departement =""
	#        print(province)
			#-------------------------------- tableau detail
			try:
				date=response.xpath("//span[contains(.,'Date Listed')]/following-sibling::span/text()").extract_first()
			   # if date == None:
			   #     date=response.xpath("//span[@class='creation-date']/text()").extract_first()
					
			except:
				date=""



			#try:
			#    ville=response.xpath("//div[@class='location']/a[@itemprop='addressLocality']/text()").extract_first()


			#except:
			#    ville=""

			try:
				type_announceur=response.xpath("//span[contains(.,'For Sale By')]/following-sibling::span/text()").extract_first()
				if type_announceur == None:
					type_announceur=response.xpath("//span[@class='username']/a/text()").extract_first()
				
				if type_announceur == None:
					type_announceur=response.xpath("//span[@class='seller-name']/text()").extract_first()

				if type_announceur == "Gumtree User":
					type_announceur="Owner"

			except:
				type_announceur=""

			try:
				marque=response.xpath("//span[contains(.,'Make')]/following-sibling::a/span/text()").extract_first()


			except:
				marque=""
			try:
				model=response.xpath("//span[contains(.,'Model')]/following-sibling::a/span/text()").extract_first()


			except:
				model=""
			try:
				carrosserie =response.xpath("//span[contains(.,'Body Type')]/following-sibling::span/text()").extract_first()

			except:
				carrosserie=""
			try:
				annee=response.xpath("//span[contains(.,'Year')]/following-sibling::span/text()").extract_first()
			except:
				annee=""
				pass
			try:
			   scr =response.xpath("//body/script").extract_first()
			   if re.findall('"yr":\d+',str(scr)) !=[]:
				   annee = re.findall('"yr":\d+',str(scr))[0].split(":")[1]
			except:
			   pass
			try:
				km=response.xpath("//span[contains(.,'Kilometers')]/following-sibling::span/text()").extract_first()

			except:
				km=""
				pass
			try:
				boite=response.xpath("//span[contains(.,'Transmission')]/following-sibling::span/text()").extract_first()

			except:
				boite=""
			try:
				carburant=response.xpath("//span[contains(.,'Fuel Type')]/following-sibling::span/text()").extract_first()

			except:
				carburant=""
			try:
				couleur=response.xpath("//span[contains(.,'Colour')]/following-sibling::span/text()").extract_first()

			except:
				couleur=""
			#----------------------------------------------------
			telephone=""
		   # try:

		   #     telephone=response.xpath("//meta[@itemprop='telephone']/@content").extract_first()
		   # except:
		   #     telephone=""

			try:
				scr =response.xpath("//script").extract()
				if re.findall('"telephone":"(.*?)"',str(scr)) !=[]:
					telephone=re.findall('"telephone":"(.*?)"',str(scr))[0]
			except:
				telephone = telephone
				pass

			try:
				desc1=response.xpath("//div[@class='description-content']/p/text()").extract()
				if desc1 == []:
					desc1=response.xpath("//div[@class='description-content']/p/b/text()").extract()
				if desc1 == []:
					desc1=response.xpath("//div[@class='description-content']/text()").extract()
				if desc1 == []:
					desc1=response.xpath("//div[@class='description']/span/text()").extract_first
			except:
				desc1=""
			print("++++++++++++++++++++++++++++++++++++++++++++",telephone)
			try:
			   if telephone is  None:
				   telephone=response.xpath("//a[@class='masked-phone phoneclick-increment']/text()").extract_first().replace(" ","")
			except:
				pass
			try:
			   if telephone == None:
				   scr =response.xpath("//script[@type='application/ld+json']").extract_first() 
			   if re.findall('"telephone":"(.*?)"',str(scr)) !=[]:
				   telephone=re.findall('"telephone":"(.*?)"',str(scr)) [0]
			except:
				pass


			#try:
			#    desc2=response.xpath("//div[@class='description']/span/b/text()").extract()

			#except:
			#    desc2=""


			try:
				description=" ".join(desc1)
				#+" Details : "+" ".join(desc2)

			except:
				description=""

			try:
				garage_id=response.xpath("//a[@class='seller-link']/@href").extract_first().split("/")[-1]
			except:
				garage_id=""

			item['SITE']=str(site)
			item['ANNONCE_LINK']=str(url)
			item['ID_CLIENT']=self.correct(id_client)
			item['CONTACT_PRENOM']=self.correct(contact_prenom)
			item['NOM']=self.correct(nom)
			item['PRIX']=self.correct(prix)
			item['ANNONCE_DATE']=self.correct(date)
			item['MARQUE']=self.correct(marque)
			item['MODELE']=self.correct(model)
			item['PRIX']=self.correct(prix_final)
			item['KM']=self.correct(km)
			item['CARBURANT']=self.correct(carburant)
			item['ANNEE']=self.correct(annee)
			item['CARROSSERIE']=self.correct(carrosserie)
			if self.correct(type_announceur) != "Dealer":
				type_annonceur = "Owner"
			item['TYPE']=self.correct(type_announceur)
			item['BOITE']=self.correct(boite)
			item['COULEUR']=self.correct(couleur)
			item['PROVINCE']=self.correct(province)
			#item['VILLE']=ville
			print(telephone)
			item['TELEPHONE']=self.clean_tel(telephone)
			try:
			   item['OPTIONS']=self.correct(description)
			except:
			   pass
			item['PHOTO']=self.correct(nb_photo)
			item['GARAGE_ID']=self.correct(garage_id)
			item["DEPARTEMENT"]=self.correct(departement)
			item["VILLE"]=self.correct(ville)
			try:
			   garage_name=response.xpath("//span[@class='seller-name']/text()").get()
			   item["GARAGE_NAME"]=garage_name
			except:
			   pass
			print("#########################################",telephone)
			#print (item)
			if "?status=adInactive" not  in  item['ID_CLIENT'] and item['ID_CLIENT'] !="":
			   yield item
