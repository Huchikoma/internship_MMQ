from django.shortcuts import render,render_to_response
from django.http import HttpResponse
import json

from pymongo import MongoClient
from mgi.models import *

from bokeh.plotting import figure,output_file,show
from bokeh.embed import components
from bokeh.resources import CDN

from plotly.offline import download_plotlyjs, init_notebook_mode, plot
import plotly.graph_objs as go

import numpy as np
import pandas as pd

# Create your views here.
def allmaterial(request):
	name = request.GET['name']
	result1 = {name:[{"name":"EOS"},{"name":"2-2"},{"name":"2-3"}]}
	return HttpResponse(json.dumps(result1),content_type="application/json")	

def index(request):
	return render(request,"Myproduct.html")


def choose_1(request):
	'''
	return all kinds of testTypes(set) 
	'''
	TestTypeDocs = XMLdata.executeQueryFullResult({"content.amTestDB.amTest.partTest.testType":{"$exists":True}},{"content.amTestDB.amTest.partTest.testType":1})
	TestTypes = {}
	for testTypeDoc in TestTypeDocs:
		item = (testTypeDoc["content"]["amTestDB"]["amTest"]["partTest"]["testType"])
		TestTypes[item] = 1	
	return HttpResponse(json.dumps(TestTypes),content_type="application/json")

def query_1(request):
	'''
	return all buildIDs which statisify the testType == Tensile
	'''
	the_type = request.GET['name']
	Tensiles = XMLdata.findm("content.amTestDB.amTest.partTest.testType",the_type)
	Builds = []
	for tensile in Tensiles:
		Builds.append(tensile["content"]["amTestDB"]["amTest"]["partTest"]["buildID"])
	MaterialNameEnums = choose_2(Builds)
	return HttpResponse(json.dumps(MaterialNameEnums),content_type="application/json")

def choose_2(Builds):
	'''
		return all kinds of materialNameEnums(set)
	'''
	MaterialNameEnumDocs = XMLdata.executeQueryFullResult({"content.amBuildDB.amBuild.generalInfo.buildID":{"$in":Builds}})
	MaterialNameEnums = {}
	for materialNameEnumDoc in MaterialNameEnumDocs:
		item = (materialNameEnumDoc["content"]["amBuildDB"]["amBuild"]["generalInfo"]["materialName"]["materialNameEnum"])
		MaterialNameEnums[item] = 1	
	return MaterialNameEnums

def query_2(request):
	'''
	return all buildIDs which statisify the testType == Tensile amd materialnameEnum == IN718
	'''
# 	the_name = request.GET['name']
# 	the_type = request.GET['name2']
# 	MaterialNames = XMLdata.findm("content.amBuildDB.amBuild.generalInfo.materialName.materialNameEnum",the_name)
# 	Builds_2 = []
# 	for materialName in MaterialNames:
# 		Builds_2.append(materialName["content"]["amBuildDB"]["amBuild"]["generalInfo"]["buildID"])
#  	Tensiles = XMLdata.findm("content.amTestDB.amTest.partTest.testType",the_type)
#  	print(Tensiles)
#  	draw_data_x = []
#  	draw_data_y = []
#  	for tensile in Tensiles:
#  		if tensile["content"]["amTestDB"]["amTest"]["partTest"]["buildID"] in Builds_2:
# 			draw_data_x.append(tensile["content"]["amTestDB"]["amTest"]["partTest"]["testResults"]["tensile"]["UTS"]["value"]["nominalValue"])
# 			draw_data_y.append(tensile["content"]["amTestDB"]["amTest"]["partTest"]["testResults"]["tensile"]["YS"]["value"]["nominalValue"])
#  	p = figure()
#  	p.line(draw_data_x,draw_data_y)
#  	script,div = components(p,CDN)
#  	return render(request,'Myproduct.html',{'the_script':script,'the_div':div})

# def query_3(request):
	# strain_values = XMLdata.executeQueryFullResult({ "_id" : ObjectId("5b8e12d1e3c04a1ddb262482")},{"content.amRawTestDataDB.rawTestData.rawStrainControlledFatigue.totalStrain.value":1})[0]["content"]["amRawTestDataDB"]["rawTestData"]["rawStrainControlledFatigue"]
	# x_strain = []
	# for strain_value in strain_values:
	# 	x_strain.append(strain_value["totalStrain"]["value"])
	# stress_values = XMLdata.executeQueryFullResult({ "_id" : ObjectId("5b8e12d1e3c04a1ddb262482")},{"content.amRawTestDataDB.rawTestData.rawStrainControlledFatigue.totalStress.value":1})[0]["content"]["amRawTestDataDB"]["rawTestData"]["rawStrainControlledFatigue"]
	# y_stress = []
	# for stress_value in stress_values:
	# 	y_stress.append(stress_value["totalStress"]["value"])

	# print(x_strain,y_stress)

	# p = figure()
	# p.line(x_strain,y_stress)
 # 	script,div = components(p,CDN)
 	
 # 	return render(request,'Myproduct.html',{'the_script':script,'the_div':div})

 # def query4():
	docs1 = XMLdata.executeQueryFullResult({"content.amTestDB":{"$exists":True}},{"content.amTestDB.amTest.partTest.testResults.density.bulkDensity.bulkDensityValue.value.nominalValue":1})
	#print docs1[0]
	#test
	#for i in range(len(docs1)):
	#	print len(docs1)
	#	print docs1[i]
	#	print "\h"
	#
	Z = []
	#print type(docs1)
	for doc in docs1:
		if 	doc.has_key('content') == True:
			if "amTestDB" in doc["content"]:
				if "amTest" in doc["content"]["amTestDB"]:
					if "partTest" in doc["content"]["amTestDB"]["amTest"]:
						if "testResults" in doc["content"]["amTestDB"]["amTest"]["partTest"]:
							if "density" in doc["content"]["amTestDB"]["amTest"]["partTest"]["testResults"]:
								if "bulkDensity" in doc["content"]["amTestDB"]["amTest"]["partTest"]["testResults"]["density"]:
									if "bulkDensityValue" in doc["content"]["amTestDB"]["amTest"]["partTest"]["testResults"]["density"]["bulkDensity"]:
										if "value" in doc["content"]["amTestDB"]["amTest"]["partTest"]["testResults"]["density"]["bulkDensity"]["bulkDensityValue"]:
											if "nominalValue" in doc["content"]["amTestDB"]["amTest"]["partTest"]["testResults"]["density"]["bulkDensity"]["bulkDensityValue"]["value"]:
												print doc["content"]["amTestDB"]["amTest"]["partTest"]["testResults"]["density"]["bulkDensity"]["bulkDensityValue"]["value"]["nominalValue"]
												Z.append(doc["content"]["amTestDB"]["amTest"]["partTest"]["testResults"]["density"]["bulkDensity"]["bulkDensityValue"]["value"]["nominalValue"])
											else:
												print"9"
										else:
											print"8"
									else:
										print"7"
								else:
									print"6"
							else:
								print"5"
						else:
							print"4"					
					else:
						print"3"
				else:
					print"2"
			else:
				print"1"
		else :
			print "0"
			
		
	
	buildids = XMLdata.executeQueryFullResult({"content.amTestDB":{"$exists":True}},{"content.amTestDB.amTest.partTest.buildID":1})
	
	#print buildids[0]
	IDs = []
	for buildid in buildids:
		if buildid.has_key('content') == True:
			if "amTestDB" in buildid["content"]:
				if "amTest" in buildid["content"]["amTestDB"]:
					if "partTest" in buildid["content"]["amTestDB"]["amTest"]:
						if "buildID" in buildid["content"]["amTestDB"]["amTest"]["partTest"]:
							print buildid["content"]["amTestDB"]["amTest"]["partTest"]["buildID"]
							IDs.append(buildid["content"]["amTestDB"]["amTest"]["partTest"]["buildID"])
						else:
							print"4"
					else:
						print"3"	
				else:
					print"2"
			else:
				print"1"		
		else:
			print"0"		

	X = []
	Y = []
	for ID in IDs:
		docs2 = XMLdata.executeQueryFullResult({"content.amBuildDB.amBuild.generalInfo.buildID": ID})
		for doc in docs2:
			X.append(doc["content"]["amBuildDB"]["amBuild"]["amProcesses"]["inProcess"]["amProcessPlans"]["amProcessPlan"]["QbeamProcessPlan"]["scanSpeed"]["value"]["nominalValue"])
			Y.append(doc["content"]["amBuildDB"]["amBuild"]["amProcesses"]["inProcess"]["amProcessPlans"]["amProcessPlan"]["QbeamProcessPlan"]["beamCurrent"]["value"]["nominalValue"])
	

	return HttpResponse(json.dumps({'X':X,'Y':Y,'Z':Z}))