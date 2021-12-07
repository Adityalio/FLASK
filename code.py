from flask import Flask,jsonify,request
app=Flask(__name__)
tasks = [
    {
        
        'Contact':"8979027181",
        'Name':"Raju",
        'done': False,
        'id': 1
    },
    {
        'Contact':"9927513302",
        'Name':"Rahul",
        'done': False,
        'id': 2
    }
]
@app.route("/")
def helloworld():
    return "hello world"

@app.route("/getdata")
def getdata():
    return jsonify({
    "data":tasks    
    })


if(__name__=="__main__"):
    app.run()


    