from flask import Flask, request 
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

palomitas = {
    1:{'name':'mantequilla'},
    2:{'name':'caramelo'},
    3:{'name':'cheddar'},
}

class Items(Resource):
    def get(self):
        return palomitas
    
    def post(self):
        data = request.json
        itemId = len(palomitas.keys()) + 1
        palomitas[itemId] = {'name':data['name']}
        return palomitas
    
class Item(Resource):
    def get(self, pk):
        return palomitas[pk]
    
    def put(self, pk):
        data = request.json
        palomitas[pk]['name'] = data['name']
        return palomitas
    
    def delete(self,pk):
        del palomitas[pk]
        return palomitas
    
api.add_resource(Items, '/')
api.add_resource(Item, '/<int:pk>')

if __name__ == '__main__':
    app.run(debug=True)