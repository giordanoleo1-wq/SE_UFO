import networkx as nx
from database.dao import DAO

class Model:
    def __init__(self):
        self.G= nx.Graph()
        self.lista_sightings= DAO.read_all_sightings()
        self.lista_states= DAO.read_all_states()
        self.lista_neighbors= DAO.read_all_neighbors()



        self.dic_neighbors= {}
        self.dic_states_id = {}
        self.dic_states_shapes= {}

        self.dic_sight_state= {}

    def get_years(self):
        lista_years = set()
        for s in self.lista_sightings:
            year = s.s_datetime.year
            if 1910<=year<= 2014:
                lista_years.add(year)
        return list(sorted(lista_years))

    def get_shapes(self, year):
        set_shapes = set()
        for s in self.lista_sightings:
            if s.s_datetime.year == year:
                if s.shape is not None and s.shape != "":
                    set_shapes.add(s.shape)
        return list(set_shapes)


    def crea_grafo(self, year, shape):
        self.G.clear()
        self.dic_neighbors= {}
        self.dic_states_id = {}
        self.dic_states_shapes = {}

        self.dic_sight_state = {}


        for n in self.lista_neighbors:
            if n.state1 not in self.dic_neighbors:
                self.dic_neighbors[n.state1]= set()
            self.dic_neighbors[n.state1].add(n.state2)
            if len(self.dic_neighbors[n.state1])== 0:
                self.dic_neighbors[n.state1]= set()




        for s in self.lista_states:
            if s.id not in self.dic_states_id:
                self.dic_states_id[s.id]= s

        for s in self.lista_sightings:
            state_id = s.state.upper()
            if s.s_datetime.year == year:
                if state_id not in self.dic_states_shapes:
                    self.dic_states_shapes[(state_id, year)]= set()
                self.dic_states_shapes[(state_id, year)].add(s.shape)


        for s in self.lista_states:
            self.G.add_node(s)

        lista_id_vicini= list(self.dic_neighbors.keys())
        lista_vicini= []
        for id_v in lista_id_vicini:
            s = self.dic_states_id[id_v]
            lista_vicini.append(s)

        for s in self.lista_sightings:
            if s.s_datetime.year == year:
                if s.shape== shape:
                    if s.state.upper() not in self.dic_sight_state.keys():
                        self.dic_sight_state[s.state.upper()]= 0
                    self.dic_sight_state[s.state.upper()] += 1

        for i in range(len(lista_vicini)):
            for j in range(i+1, len(lista_vicini)):
                stato1 = lista_vicini[i]
                stato2 = lista_vicini[j]

                if stato1.id in self.dic_neighbors[stato2.id] or stato2.id in self.dic_neighbors[stato1.id]:
                    if not self.G.has_edge(stato1, stato2):
                        peso= self.dic_sight_state.get(stato1.id, 0) + self.dic_sight_state.get(stato2.id, 0)
                        if peso >0:
                            self.G.add_edge(stato1, stato2, weight=peso)




    def calcola_peso_per_nodo(self):
        result= {}
        for n in self.G.nodes():
            peso= 0
            for m in self.G.nodes():
                if self.G.has_edge(n, m):
                    peso += self.G[m][n]['weight']
            result[n] = peso

        return result























