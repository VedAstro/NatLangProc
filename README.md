# NLP Open API
Easy to use Natural Language Processing API powered by spaCy.</br>
Access powerful features like **Sentence Segmentation** & **Lemmatization**</br>
via a simple `HTTP GET` request.

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
| token       | Token texts                         | This is a text.           | [ 'This ' , ' is' , 'a ' , 'text' ] | <a target="_blank" href="https://vedastroapilinux.azurewebsites.net/api/eng/token/This is a text.">RUN</a> |
| ents        | text and label of named entity span | Larry Page founded Google | [ ( ' Larry Page' , 'PERSON' ), ( 'Google' , 'ORG' )] |<a target="_blank" href="https://vedastroapilinux.azurewebsites.net/api/eng/ents/Larry Page founded Google">RUN</a> |
| pos_        | coarse-grained part-of-speech tags  | This is a text.           | [ 'DET' , 'VERB' , 'DET' , 'NOUN' , 'PUNCT' ]         | <a target="_blank" href="https://vedastroapilinux.azurewebsites.net/api/eng/pos_/This is a text.">RUN</a> |
| tag_        | fine-groined port-of-speech tags    | This is a text.           | [ ' DT' , 'VBZ ' , ' DT' , ' NN ' , ' . ' ]           | <a target="_blank" href="https://vedastroapilinux.azurewebsites.net/api/eng/tag_/This is a text.">RUN</a> |
| sents       | yields sentence spans               | This a sentence. This is another one. | [ 'This is a sentence. ' , 'This is another one. ' l  | <a target="_blank" href="https://vedastroapilinux.azurewebsites.net/api/eng/sents/This a sentence. This is another one.">RUN</a> |
| noun_chunks | base noun phrases                   | I have a red car          | [ 'I' , 'a red car' ]                                 | <a target="_blank" href="https://vedastroapilinux.azurewebsites.net/api/eng/noun_chunks/I have a red car">RUN</a> |
| dep_        | dependency labels                   | This is a text.           | [ 'nsubj' , 'ROOT' , 'det' , 'attr" , 'pun ct' ]      | <a target="_blank" href="https://vedastroapilinux.azurewebsites.net/api/eng/dep_/This is a text.">RUN</a> |
| more...     | coming soon                         | This is a text.           | ....      | <a target="_blank" href="https://vedastroapilinux.azurewebsites.net/api/eng/dep_/This is a text.">RUN</a>  |


# API Domain
Currently the BETA public access domain address is `https://vedastroapilinux.azurewebsites.net/api`.
This is only temporary, idealy the URL should be nice & short with an easy to remember domain name.
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
