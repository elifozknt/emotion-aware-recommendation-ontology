from pyshacl import validate
from rdflib import Graph

data_graph = Graph()
data_graph.parse("ontology_v2 (4).ttl", format="turtle")

shacl_graph = Graph()
shacl_graph.parse("shapes.ttl", format="turtle")

conforms, results_graph, results_text = validate(
    data_graph,
    shacl_graph=shacl_graph,
    inference="rdfs",
    debug=False
)

print("Conforms:", conforms)
print(results_text)