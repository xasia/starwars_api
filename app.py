from flask import Flask, jsonify, request

app = Flask(__name__)

starfighters = [
    {
        "id": 1,
        "name": "T-68B X-Wing",
        "manufacturer": "Incom Corporation",
        "length": 13.4,
        "width": 11.76,
        "mass": 10000,
        "lasers": 4,
        "rockets": 2,
        "max_speed": 1050
    }
]

@app.route('/starfighters', methods=['GET'])
def get_starfighters():
    return jsonify(starfighters)

@app.route('/starfighters', methods=['POST'])
def add_starfighter():
    new_fighter = request.get_json()
    starfighters.append(new_fighter)
    return jsonify(starfighters), 201

@app.route('/starfighters/<int:id>', methods=['PUT'])
def update_starfighter(id):
    updated_fighter = request.get_json()
    for f in starfighters:
        if f['id'] == id:
            f.update(updated_fighter)
            return jsonify(starfighters)
    return {"error": "Not found"}, 404

@app.route('/starfighters/<int:id>', methods=['DELETE'])
def delete_starfighter(id):
    global starfighters
    starfighters = [f for f in starfighters if f['id'] != id]
    return '', 201

if __name__ == '__main__':
    app.run(debug=True)
