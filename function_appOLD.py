import azure.functions as func
import logging
import spacy
import pathlib
import json


app = func.FunctionApp()

# Learn more at aka.ms/pythonprogrammingmodel

# Get started by running the following code to create a function using a HTTP trigger.

@app.function_name(name="HttpTrigger1")
@app.route(route="hello", auth_level=func.AuthLevel.ANONYMOUS)
def test_function(req: func.HttpRequest) -> func.HttpResponse:

    logging.info('Python HTTP trigger function processed a request.')

    print(get_spacy_path())
    nlp = spacy.load(get_spacy_path())

    #nlp = spacy.load("en_core_web_sm")
    searchKeyword = nlp("money")

    searchText1 = nlp(
            "Rheumatic and similar troubles, quarrels, danger of enteric fever, dysentery, troubles to relatives, loss of money"
			"by thefts or wasteful expenses, failures, acquisition of wealth"
			"in the form of gold and gems, royal favour leading to prosperity,"
			"contraction and transmission of bilious and other"
			"diseases, mental worries, danger from fire, ill-health, loss of"
			"reputation, sorrow.")
            
    searchText2 = nlp("Winning favour from superiors, increase in business, fresh"
			"enterprises, troubles through women, eye troubles, many"
			"relatives and friends, indulgence in idle pastimes, jaundice"
			"and kindred ailments, new clothes and ornaments, will be"
			"happy, healthy, good meals, respect among relatives.")
 

    threshold = 0.1

    #sentsList = searchText1.sents

    arrayToken = [token for token in searchText1] 
    arraySimilarity = [token.similarity(searchKeyword) for token in searchText1] 
    arraySimilarity2 = [print(token, token.similarity(searchKeyword)) for token in searchText1] 

    #dictionary = {'a':34, 'b':61, 'c':82}
    
    # jsonString = json.dumps(arraySimilarity, indent=4)
    # print(jsonString)

    # for x in array:
    #     print(x)

    # matched_words = []
    # for token in searchText1:
    #     print(token, token.similarity(searchKeyword))
    #     if token.similarity(searchText1) > threshold:
    #         matched_words.append(token)

    # print(f"\nMatched words: {matched_words}")

    return func.HttpResponse(f"{arrayToken}/n/n{arraySimilarity}/n/n{arraySimilarity2}")
    
    #printing environment variables
     
    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )
    
    # loads spacy model from local extracted source, done to run in azure func
def get_spacy_path():     
    current_path = pathlib.Path(__file__).parent    
    return str(current_path / 'en_core_web_sm-3.5.0')
