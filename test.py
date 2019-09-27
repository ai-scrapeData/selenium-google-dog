import pymongo

myclient = pymongo.MongoClient('mongodb://heroku_3lsf2k6l:acj9qbdfmvd8j2ub1ek7nc8ac1@ds023523.mlab.com:23523/heroku_3lsf2k6l')
mydb = myclient['heroku_3lsf2k6l']
mycol = mydb["comment"]

mydict = { "name": "John", "address": "Highway 37" }

x = mycol.insert_one(mydict)

print(x)
