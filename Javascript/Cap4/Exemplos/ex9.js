/*from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/usuarios', methods=['GET'])
def get_usuarios():
    usuarios = [
        {
            'nome': 'John Doe',
            'idade': 30,
            'email': 'johndoe@example.com'
        },
        {
            'nome': 'Jane Smith',
            'idade': 25,
            'email': 'janesmith@example.com'
        }
    ]
    return jsonify(usuarios)

if __name__ == '__main__':
    app.run()
*/