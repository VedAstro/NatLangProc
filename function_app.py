import json
import azure.functions as func
import spacy
import pathlib
# importing the requests library
import requests
import xml.etree.ElementTree as ET

app = func.FunctionApp()

@app.function_name(name="main")
@app.route(route="{language}/{option}/{inputText}", auth_level=func.AuthLevel.ANONYMOUS) #todo implement language choice
def main(req: func.HttpRequest) -> func.HttpResponse:

    # log the call
    # sending get request and saving the response as response object
    logRequest(req)

    #get data from caller URL
    inputText = "" # empty detect fail
    try:
        language = req.route_params.get('language') # todo for future implementation
        option = req.route_params.get('option')
        inputText = req.route_params.get('inputText')
    except ValueError:
        pass

    # load spacy model
    spacyLocalPath = get_spacy_path()
    nlp = spacy.load(spacyLocalPath)

    # do the processing
    nlpDoc = nlp(inputText)

    # extract requested data
    match option:
        case "token":
            dataList = [token.text for token in nlpDoc]   
        case "ents":
            dataList = [(ent.text, ent.label_) for ent in nlpDoc.ents]    
        case "pos_":
            dataList = [token.pos_ for token in nlpDoc]
        case "tag_":
            dataList = [token.tag_ for token in nlpDoc]
        case "sents":
            dataList = [sent.text for sent in nlpDoc.sents]
        case "noun_chunks":
            dataList = [chunk.text for chunk in nlpDoc.noun_chunks]
        case "dep_":
            dataList = [token.dep_ for token in nlpDoc]


    #convert to JSON for easy consumption before sending to caller
    returnJson = json.dumps(dataList, indent=4)
    return func.HttpResponse(returnJson, headers={"content-type": "application/json"})


def logRequest(req: func.HttpRequest):
    
    # get data from request
    headerList = [(header, req.headers.get(header)) for header in req.headers]
    #paramList = [(param, req.params.get(param)) for param in req.params]
    #routeParamsList = [(rParam, req.params.get(rParam)) for rParam in req.route_params]

    # format data to be logged in main list via API
    visitorXml = ET.Element('Visitor')
    dataXml = ET.SubElement(visitorXml, 'Data')
    for header in headerList:
        propName = header[0]
        propVal = header[1]
        propXml = ET.SubElement(dataXml,propName )
        propXml.text = propVal

    # convert to string
    xmlStr = ET.tostring(visitorXml, method='xml')    

    # send to API
    url = 'https://vedastroapi.azurewebsites.net/api/addvisitor'
    ignoreResult = requests.post(url, data = xmlStr)
    print(ignoreResult)

    

# loads spacy model from local extracted source, done so to run in azure func
def get_spacy_path():     
    current_path = pathlib.Path(__file__).parent    
    return str(current_path / 'en_core_web_sm-3.5.0') #todo change to full model or model choice
