# NLP Open API
Easy to use Natural Language Processing" API powered by spaCy.</br>
Access powerful features like **Sentence Segmentation**, **Lemmatization** via `HTTP GET` request 

<a href="#">
<img
  src="https://www.vedastro.org/images/nlp-api-url-guide.jpg">
</a>

# OPTIONS
The option keywords used follow spaCy, this is done to reduce the learning curve,
espcially for those who are already familiar with spaCy


| Name        | Description     | Input | Output | Status  |
| ------------- |:-------------:| -----:|-----:|-----:|
| token       | Token texts                         | This is a text.           | [ 'This ' , ' is' , 'a ' , 'text' ] | BETA |
| ents        | text and label of named entity span | Larry Page founded Google | [ ( ' Larry Page' , 'PERSON' ), ( 'Google' , 'ORG' )] | BETA |
| pos_        | coarse-grained part-of-speech tags  | This is a text.           | [ 'DET' , 'VERB' , 'DET' , 'NOUN' , 'PUNCT' ]         | BETA |
| tag_        | fine-groined port-of-speech tags    | This is a text.           | [ ' DT' , 'VBZ ' , ' DT' , ' NN ' , ' . ' ]           | BETA |
| sents       | yields sentence spans               | This a sentence. This is another one.| [ 'This is a sentence. ' , 'This is another one. ' l  | BETA |
| noun_chunks | base noun phrases                   | I have a red car          | [ 'I' , 'a red car' ]                                 | BETA |
| dep_        | dependency labels                   | This is a text.           | [ 'nsubj' , 'ROOT' , 'det' , 'attr" , 'pun ct' ]      | BETA |
| more...     | coming soon                         | This is a text.           | [ 'nsubj' , 'ROOT' , 'det' , 'attr" , 'pun ct' ]      | BETA |


# API DOMAIN
Currently the work-in-progress public access domain is `https://vedastroapilinux.azurewebsites.net/api`.
We hope to make this URL nice & short with a easy to rember domain name.
If you can please donate a domain.

# LANGUAGE
Currently we support only English, but feel free to sugest a language in issues.
If there is enough support, we will implement as many languages as possible.