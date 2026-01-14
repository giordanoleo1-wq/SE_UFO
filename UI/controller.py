import flet as ft
from UI.view import View
from model.model import Model
class Controller:
    def __init__(self, view: View, model: Model):
        self._view = view
        self._model = model

    def populate_dd_year(self):
        """ Metodo per popolare i dropdown """
        # TODO


        lista_anni= self._model.get_years()
        result= []
        for a in lista_anni:
            result.append(ft.dropdown.Option(a))


        return result

    def populate_dd_shape(self, e):
        self._view.dd_shape.options.clear()
        anno= int(self._view.dd_year.value)

        lista_shapes = self._model.get_shapes(anno)

        for s in lista_shapes:
            self._view.dd_shape.options.append(ft.dropdown.Option(s))

        self._view.update()



    def handle_graph(self, e):
        """ Handler per gestire creazione del grafo """
        # TODO
        self._view.lista_visualizzazione_1.clean()


        try:
            anno= int(self._view.dd_year.value)
            shape= self._view.dd_shape.value
        except Exception as exc:
            self._view.show_alert("Inserire forma e anno validi")
            print(exc)
            return
        self._model.crea_grafo(anno, shape)
        self._view.lista_visualizzazione_1.controls.append(ft.Text(f"Numero di vertici: {self._model.G.number_of_nodes()}, Numero di archi: {self._model.G.number_of_edges()}"))

        result = self._model.calcola_peso_per_nodo()
        for n in self._model.G.nodes():
            self._view.lista_visualizzazione_1.controls.append(ft.Text(f"Nodo : {n.id}, somma pesi su archi -> {result[n]}"))

        self._view.update()

    def handle_path(self, e):
        """ Handler per gestire il problema ricorsivo di ricerca del cammino """
        # TODO
        self._view.lista_visualizzazione_2.clean()

        sequenza, peso, distanze= self._model.get_percorso_ottimo()

        self._view.lista_visualizzazione_2.controls.append(ft.Text(f"Peso cammino massimo: {peso}"))

        for i in range(len(sequenza) -1):
            n1= sequenza[i]
            n2= sequenza[i+1]

            peso= self._model.G[n1][n2]['weight']
            distanza= distanze[i]

            self._view.lista_visualizzazione_2.controls.append(ft.Text(f"{n1.id} -- {n2.id}, weight: {peso}, distance: {distanza}"))
        self._view.update()







