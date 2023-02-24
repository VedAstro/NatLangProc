import json
import azure.functions as func
import spacy
import pathlib



app = func.FunctionApp()

@app.function_name(name="main")
@app.route(route="{language}/{option}/{inputText}", auth_level=func.AuthLevel.ANONYMOUS) #todo implement language choice
def main(req: func.HttpRequest) -> func.HttpResponse:

    #get data from caller URL
    inputText = "" # empty detect fail
    try:
        language = req.route_params.get('language')
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
    jsonReturn = ""
    match option:
        case "token":
            sentenceList = [token.text for token in nlpDoc]   
        case "ents":
            sentenceList = [(ent.text, ent.label_) for ent in nlpDoc.ents]    
        case "pos_":
            sentenceList = [token.pos_ for token in nlpDoc]
        case "tag_":
            sentenceList = [token.tag_ for token in nlpDoc]
        case "sents":
            sentenceList = [sent.text for sent in nlpDoc.sents]
        case "noun_chunks":
            sentenceList = [chunk.text for chunk in nlpDoc.noun_chunks]
        case "dep_":
            sentenceList = [token.dep_ for token in nlpDoc]


    #convert to JSON for easy consumption before sending to caller
    returnJson = json.dumps(sentenceList, indent=4)
    return func.HttpResponse(returnJson, headers={"content-type": "application/json"})


# loads spacy model from local extracted source, done so to run in azure func
def get_spacy_path():     
    current_path = pathlib.Path(__file__).parent    
    return str(current_path / 'en_core_web_sm-3.5.0') #todo change to full model or model choice
