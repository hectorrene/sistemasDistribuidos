from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

palomitas = {
    1: {'name': 'mantequilla', 'precio': 50.0, 'sabor2': 'vainilla', 'tipo': 'salado'},
    2: {'name': 'caramelo', 'precio': 60.0, 'sabor2': 'chocolate', 'tipo': 'dulce'},
    3: {'name': 'cheddar', 'precio': 55.0, 'sabor2': 'queso azul', 'tipo': 'salado'},
}

class Items(Resource):
    def get(self):
        return palomitas

    def post(self):
        data = request.json
        itemId = max(palomitas.keys()) + 1
        palomitas[itemId] = {
            'name': data['name'],
            'precio': data['precio'],
            'sabor2': data['sabor2'],
            'tipo': data['tipo']
        }
        return palomitas

class Item(Resource):
    def get(self, pk):
        return palomitas.get(pk, {'message': 'No encontrado'})

    def put(self, pk):
        if pk not in palomitas:
            return {'message': 'No encontrado'}, 404
        data = request.json
        palomitas[pk].update({
            'name': data['name'],
            'precio': data['precio'],
            'sabor2': data['sabor2'],
            'tipo': data['tipo']
        })
        return palomitas

    def delete(self, pk):
        if pk in palomitas:
            del palomitas[pk]
        return palomitas

class Dulces(Resource):
    def get(self):
        return {k: v for k, v in palomitas.items() if v['tipo'] == 'dulce'}

class Saladas(Resource):
    def get(self):
        return {k: v for k, v in palomitas.items() if v['tipo'] == 'salado'}

class BorrarPorSabor(Resource):
    def delete(self, nombre):
        keys_to_delete = [k for k, v in palomitas.items() if v['name'] == nombre]
        for k in keys_to_delete:
            del palomitas[k]
        return palomitas

api.add_resource(Items, '/')
api.add_resource(Item, '/<int:pk>')
api.add_resource(Dulces, '/dulces')
api.add_resource(Saladas, '/saladas')
api.add_resource(BorrarPorSabor, '/sabor/<string:nombre>')

if __name__ == '__main__':
    app.run(debug=True)
