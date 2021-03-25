import pymongo

client = pymongo.MongoClient("mongodb+srv://rs:Ky0getsU9@jokecluster.le6wi.mongodb.net/GenJokes?retryWrites=true&w=majority")
jokeDB = client['GenJokes']

def mongoStorage(files):
    for file in files:
        try:
            if 'new' in file.name: #check whether it's checked for grammar
                stringList = file.name.split('_')
                userHandle = stringList[1] #get twitter handle

                #connect to mongoDB, initialise collection
                userCol = jokeDB["Massive Collection"]

                split = '===================='

                #append to collection
                for index, line in enumerate(file):
                    if split not in line:
                        entry = {'sentence':'{}'.format(line), 'likedUsers':["admin"], 'type':userHandle}
                        userCol.insert_one(entry)

                client.close()
                
        except:
            pass