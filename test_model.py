from model.model import Model
model = Model()

#print(model.get_years())

#print(model.get_shapes(2010))

model.crea_grafo(1999, "triangle")
#print(model.dic_neighbors["AL"])
#print(model.dic_states_id["GA"])
print(model.calcola_peso_per_nodo())
#print(len(model.G.nodes()))
#print(len(model.G.edges()))
