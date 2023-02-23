import azure.functions as func
import logging
import spacy

app = func.FunctionApp()

# Learn more at aka.ms/pythonprogrammingmodel

# Get started by running the following code to create a function using a HTTP trigger.

@app.function_name(name="HttpTrigger1")
@app.route(route="hello", auth_level=func.AuthLevel.ANONYMOUS)
def test_function(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    nlp = spacy.load("en_core_web_lg")
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


    threshold = 0.0

    matched_words = []
    for token in searchText1:
        print(token, token.similarity(searchKeyword))
        if token.similarity(searchText1) > threshold:
            matched_words.append(token)

    print(f"\nMatched words: {matched_words}")

    return func.HttpResponse(f"{matched_words}")
    
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