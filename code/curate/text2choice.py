##### add some code to statisfy reference  author:Hongcang Li

from pymongo import MongoClient
from curate.models import SchemaElement


MONGODB_URI = 'mongodb://mgi:mgi@localhost/mgi'
projectIDs = set(["blank"])
DB_NAME = "mgi"
client = MongoClient(MONGODB_URI)
db = client[DB_NAME]
xmldata = db['xmldata']

for cursor in xmldata.find({"content.amProjectDB.@xmlns:xsi": "http://www.w3.org/2001/XMLSchema-instance"}):
	projectIDs.add(cursor["content"]["amProjectDB"]["amProject"]["projectID"])



product_element = SchemaElement()
product_element.tag = u'restriction'
product_element.value = u"blank"
product_element.options = {u'base': u'xs:string'}
product_element.children = []
product_element.save()

for ProjectID in projectIDs:
	xsd_element = SchemaElement()
	xsd_element.tag = u'enumeration'
	xsd_element.value = str(ProjectID).decode('UTF-8')
	xsd_element.options = {}
	xsd_element.children = []
	xsd_element.save()
	product_element.children.append(xsd_element)
	product_element.save()
a = product_element
product_element = SchemaElement()
product_element.tag = u'simple_type'
product_element.value = None
product_element.options = {u'ns_prefix': None, u'xmlns': None, u'name': u'productNameEnumType'}
product_element.children = [a]
product_element.save()

a = product_element
product_element = SchemaElement()
product_element.tag = u'elem-iter'
product_element.value = None
product_element.options = {}
product_element.children = [a]
product_element.save()

b = product_element

##################

def text2choice(root_element):
	
	for child in root_element.children:
		try:
			if child.options['name'] == 'projectID':
				child.children = [b]
				child.save()
				return
		except:
			pass

	for child in root_element.children:
		text2choice(child)


