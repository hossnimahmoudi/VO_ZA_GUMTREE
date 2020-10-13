# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy import signals
#from scrapy.exporters import CsvItemExporter
from scrapy.exporters import CsvItemExporter
from csv import QUOTE_ALL
class AnnonceGumtreePipeline(object):
    def __init__(self):
        self.files = {}


    @classmethod
    def from_crawler(cls, crawler):
        pipeline = cls()
        crawler.signals.connect(pipeline.spider_opened, signals.spider_opened)
        crawler.signals.connect(pipeline.spider_closed, signals.spider_closed)
        return pipeline

    def spider_opened(self, spider):
        file = open('%s.csv' % spider.name, 'w+b')
        self.files[spider] = file
        self.exporter = CsvItemExporter(file, delimiter=';', quotechar='"', quoting=QUOTE_ALL)
        self.exporter.start_exporting()
        self.exporter.fields_to_export = [ "ANNONCE_LINK","ANNONCE_DATE","ID_CLIENT","GARAGE_ID","TYPE","SITE","MARQUE","MODELE","ANNEE","MOIS","NOM","CARROSSERIE","OPTIONS","CARBURANT","CYLINDRE","PUISSANCE","PORTE","BOITE","NB_VITESSE","PRIX","KM","PLACE","COULEUR","PHOTO","LITRE","IMMAT","NO_CHASSIS","VN_IND","CONTACT","CONTACT_PRENOM","CONTACT_NOM","GARAGE_NAME","ADRESSE","VILLE","CP","DEPARTEMENT","PROVINCE","COUNTRY","TELEPHONE","TELEPHONE_2","TELEPHONE_3","TELEPHONE_4","TELEFAX","EMAIL","MINI_SITE"] 
        #,'motor','valve_cylind' , 'color_caoutchouc', 'prop_uniq', 'plaque', 'hauteur','large','largeur','distance_axe','cp_reservoir','direction','control_traction']
    def spider_closed(self, spider):
        self.exporter.finish_exporting()
        file = self.files.pop(spider)
        file.close()


    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item
