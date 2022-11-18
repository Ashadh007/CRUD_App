from flask import Flask,jsonify
from flask_cors import CORS
import pymongo

conn_str ='mongodb+srv://ashadh:abcd1234@cluster0.tuwifdn.mongodb.net/?retryWrites=true&w=majority'
app = Flask(__name__)
client = pymongo.MongoClient(conn_str)

Database = client.get_database('mydb1')

Collections = Database.get_collection('mycol1')

@app.route('/insert/<name>/<id>/', methods=['POST'])
def insertData(name, id):
    res = {
        'Name': name,
        'ID': id
    }
    query = Collections.insert_one(res)
    return "Data Stored."

@app.route('/find/', methods=['GET'])
def findAll():
    res = Collections.find()
    op = {}
    i = 0
    for x in res:
        op[i] = x
        op[i].pop('_id')
        i += 1
    return jsonify(op)

@app.route('/update/<key>/<value>/<element>/<updateValue>/', methods=['PUT'])
def updateData(key, value, element, updateValue):
    presval = {key: value}
    updatedval = {element: updateValue}
    res = Collections.update_one(presval, {'$set': updatedval})
    if res.acknowledged:
        return "Update Successful"
    else:
        return "Update Unsuccessful"

@app.route('/del/<name>/<id>/', methods=['DELETE'])
def delData(name, id):
    res = {
        'Name': name,
        'ID': id
    }
    query = Collections.delete_one(res)
    return "Data deleted."

if __name__ == '__main__':
	app.run(debug=True)