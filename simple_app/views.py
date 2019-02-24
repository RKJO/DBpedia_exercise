from django.shortcuts import render

# Create your views here.
from rdflib import Graph, URIRef, RDF
uri = URIRef('http://dbpedia.org/resource/Kazik_Staszewski')
person = URIRef('http://dbpedia.org/ontology/Person')

g = Graph()
g.parse(uri)
print(g.parse(uri))

# for obj in g.objects(subject=uri, predicate=RDF.type):
#     if obj == person:
#         print(uri, "is a", person, obj)