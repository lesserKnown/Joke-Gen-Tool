import requests
import json
import logging

api_key = "6ae0c3a0-afdc-4532-a810-82ded0054236"
split = '===================='

def checkGrammar(text):

    newText = ""
    startIndex = 0
    
    url = "http://services.gingersoftware.com/Ginger/correct/json/GingerTheText?lang=US&clientVersion=2.0&apiKey={}&text={}".format(api_key, text)

    response = requests.get(url)
    result = response.json()

    if  not result['LightGingerTheTextResult']:
        #print('Good grammar.')
        return text

    else:
        for line in result['LightGingerTheTextResult']:
            from_index = line['From'] #start index of mistake
            to_index = line['To'] #end index of mistake
            replacement = line['Suggestions'][0]['Text'] #replacement provided for mistake
            newText+=text[startIndex:from_index]+replacement 
            startIndex = to_index + 1
        
        newText+=text[startIndex:]
        return newText

def gingerMain(files):
    #Check grammar of input text. Then, output curated text and log files.
    for file in files:
        try:
            output = open("{}_new.txt".format(file.name[:-4]), "a")
            #print("File created.")
            logging.basicConfig(filename='{}_error.log'.format(file.name[:-4]), level= logging.INFO, format= '%(asctime)s %(message)s', datefmt='%d/%m/%Y %I:%M:%S %p',filemode='a')
        
            for index, line in enumerate(file):
                if(line == split):
                    print(split) #decrease processing time, skip checking for split text
                else:
                    try:
                        newText = checkGrammar(line)
                        output.write(newText)
                        print(newText)
                    except:
                        #print("Error during reading. Index = {}. Line = {}.".format(index, line))
                        #need to save to a log
                        logging.info("Error during reading. Index = {}. Line = {}.".format(index, line))
                        pass
            print("End of check.")
            output.close()
        except:
            pass






