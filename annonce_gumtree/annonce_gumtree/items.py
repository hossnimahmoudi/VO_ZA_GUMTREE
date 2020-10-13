# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class GumtreeItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # About the car    
        
    ANNONCE_LINK= scrapy.Field(serializer=str)
    ANNONCE_DATE= scrapy.Field(serializer=str)
    ID_CLIENT= scrapy.Field(serializer=str)
    GARAGE_ID= scrapy.Field(serializer=str)
    TYPE= scrapy.Field(serializer=str)
    SITE= scrapy.Field(serializer=str)
    MARQUE= scrapy.Field(serializer=str)
    MODELE= scrapy.Field(serializer=str)
    ANNEE= scrapy.Field(serializer=str)
    MOIS= scrapy.Field(serializer=str)
    NOM= scrapy.Field(serializer=str)
    CARROSSERIE= scrapy.Field(serializer=str)
    OPTIONS= scrapy.Field(serializer=str)
    CARBURANT= scrapy.Field(serializer=str)
    CYLINDRE= scrapy.Field(serializer=str)
    PUISSANCE= scrapy.Field(serializer=str)
    PORTE= scrapy.Field(serializer=str)
    BOITE= scrapy.Field(serializer=str)
    NB_VITESSE= scrapy.Field(serializer=str)
    PRIX= scrapy.Field(serializer=str)
    KM= scrapy.Field(serializer=str)
    PLACE= scrapy.Field(serializer=str)
    COULEUR= scrapy.Field(serializer=str)
    PHOTO= scrapy.Field(serializer=str)
    LITRE= scrapy.Field(serializer=str)
    IMMAT= scrapy.Field(serializer=str)
    NO_CHASSIS= scrapy.Field(serializer=str)
    VN_IND= scrapy.Field(serializer=str)
    CONTACT= scrapy.Field(serializer=str)
    CONTACT_PRENOM= scrapy.Field(serializer=str)
    CONTACT_NOM= scrapy.Field(serializer=str)
    GARAGE_NAME= scrapy.Field(serializer=str)
    ADRESSE= scrapy.Field(serializer=str)
    VILLE= scrapy.Field(serializer=str)
    CP= scrapy.Field(serializer=str)
    DEPARTEMENT= scrapy.Field(serializer=str)
    PROVINCE= scrapy.Field(serializer=str)
    COUNTRY= scrapy.Field(serializer=str)
    TELEPHONE= scrapy.Field(serializer=str)
    TELEPHONE_2= scrapy.Field(serializer=str)
    TELEPHONE_3= scrapy.Field(serializer=str)
    TELEPHONE_4= scrapy.Field(serializer=str)
    TELEFAX= scrapy.Field(serializer=str)
    EMAIL= scrapy.Field(serializer=str)
    MINI_SITE= scrapy.Field(serializer=str)
