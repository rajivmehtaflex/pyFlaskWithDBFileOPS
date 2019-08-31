from flask import Flask,request
import sqlite3
from FileOps.files import ping,convert_and_save
webapp=Flask(__name__)

@webapp.route("/ping")
def ping():
    print("Here")
    return "done"


@webapp.route("/SeedTables")
def SeedTables():
    try:
        TableName = request.args.get("mm")
        with sqlite3.connect("gdb.db") as conn:
            conn.execute('CREATE TABLE Details (name TEXT, addr TEXT, city TEXT, pin TEXT)')
            print ("Table created successfully")
    except expression as identifier:
        pass
    finally:
        pass

    return "done"

@webapp.route("/StoreIntoDB",methods=['GET','POST'])
def StoreIntoDB():
    if request.method == 'POST':
        # print("Done with Post==>",request.get_json()["firstName"])
        print("Done with Post==>",request.get_json()["image"])
        # with sqlite3.connect("gdb.db") as conn:
        #     conn.execute('INSERT INTO "main"."Person"("id","name") VALUES ({},"{}");'.format(request.get_json()["id"],request.get_json()["firstName"]))
    return request.get_json()

@webapp.route("/StoreIntoFS",methods=['GET','POST'])
def StoreIntoFS():
    if request.method == 'POST':
        print("Done with Post==>",request.get_json()["filename"])
        # gd = request.get_json()["image64"]
        convert_and_save(request.get_json()["image64"],request.get_json()["filename"])
        return "Done"


if __name__ =="__main__":
    webapp.run(debug=True,port=55181)
