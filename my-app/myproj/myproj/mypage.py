
from django.http import HttpResponse
import pymongo

def index(req):
	appdb = pymongo.MongoClient('db').appdb
	data = appdb.app_collection1.find_one()
	resp = "Our first record is: " + str(data)
	return HttpResponse(resp)