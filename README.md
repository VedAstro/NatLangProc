# NLP Open API
Easy to use Natural Language Processing API powered by spaCy.</br>
Access powerful features like **Sentence Segmentation**, **Lemmatization** via a simple `HTTP GET` request.

# How to use
<a href="#">
<img
  src="https://www.vedastro.org/images/nlp-api-url-guide.jpg">
</a>

# Options
Options allow to select the type of tool to process the input text.
Keywords used follow the same as spaCy, this is done to reduce the learning curve,
espcially for those who are already familiar with spaCy.


| Name        | Description     | Input | Output | Status  |
| ------------- |:-------------:| -----:|-----:|-----:|
| token       | Token texts                         | This is a text.           | [ 'This ' , ' is' , 'a ' , 'text' ] | [RUN](https://vedastroapilinux.azurewebsites.net/api/eng/token/This is a text.) |
| ents        | text and label of named entity span | Larry Page founded Google | [ ( ' Larry Page' , 'PERSON' ), ( 'Google' , 'ORG' )] | [RUN](https://vedastroapilinux.azurewebsites.net/api/eng/ents/Larry Page founded Google) |
| pos_        | coarse-grained part-of-speech tags  | This is a text.           | [ 'DET' , 'VERB' , 'DET' , 'NOUN' , 'PUNCT' ]         | [RUN](https://vedastroapilinux.azurewebsites.net/api/eng/pos_/This is a text.) |
| tag_        | fine-groined port-of-speech tags    | This is a text.           | [ ' DT' , 'VBZ ' , ' DT' , ' NN ' , ' . ' ]           | [RUN](https://vedastroapilinux.azurewebsites.net/api/eng/tag_/This is a text.) |
| sents       | yields sentence spans               | This a sentence. This is another one.| [ 'This is a sentence. ' , 'This is another one. ' l  | [RUN](https://vedastroapilinux.azurewebsites.net/api/eng/sents/This a sentence. This is another one.) |
| noun_chunks | base noun phrases                   | I have a red car          | [ 'I' , 'a red car' ]                                 | [RUN](https://vedastroapilinux.azurewebsites.net/api/eng/dep_/This is a text.) |
| dep_        | dependency labels                   | This is a text.           | [ 'nsubj' , 'ROOT' , 'det' , 'attr" , 'pun ct' ]      | [RUN](https://vedastroapilinux.azurewebsites.net/api/eng/token/This is a text.) |
| more...     | coming soon                         | This is a text.           | [ 'nsubj' , 'ROOT' , 'det' , 'attr" , 'pun ct' ]      | [RUN](https://vedastroapilinux.azurewebsites.net/api/eng/token/This is a text.) |


# API Domain
Currently the BETA public access domain address is `https://vedastroapilinux.azurewebsites.net/api`.
This is only temporary, idealy the URL should be nice & short with an easy to rember domain name.
If you have an unused domain name or are willing to sponsor a domain for a year, please let us know.

# Language
Currently we support only English (eng), but feel free to sugest a language in issues.
If there is enough support, we will implement as many languages as possible
or allow you to choose from a list of language models.

# Links
- [Donate](https://www.vedastro.org/Donate) to keep this project going
- [Contact](https://www.vedastro.org/Contact) reach us via email at contact@vedastro.org
- [Share](https://www.vedastro.org/Contact) your ideas for new or better features 
- [Fix](https://www.vedastro.org/Contact) bugs & implement features
