from flask import Flask, request, jsonify
import os

app = Flask(__name__)

# Prosta baza danych w pamięci
notes = []

@app.route('/notes', methods=['POST'])
def create_note():
    data = request.get_json()
    notes.append(data)
    return jsonify(data), 201

@app.route('/notes', methods=['GET'])
def get_notes():
    return jsonify(notes), 200

@app.route('/notes/<int:index>', methods=['PUT'])
def update_note(index):
    data = request.get_json()
    if 0 <= index < len(notes):
        notes[index] = data
        return jsonify(data), 200
    return jsonify({'error': 'Not found'}), 404

@app.route('/notes/<int:index>', methods=['DELETE'])
def delete_note(index):
    if 0 <= index < len(notes):
        removed_note = notes.pop(index)
        return jsonify(removed_note), 200
    return jsonify({'error': 'Not found'}), 404

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)