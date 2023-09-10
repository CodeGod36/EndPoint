from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/endpoint', methods=['GET'])
def get_data():
    # Get query parameters
    param1 = request.args.get('param1')
    param2 = request.args.get('param2')

    # Perform some logic to generate a response JSON
    response_data = {
        "param1": param1,
        "param2": param2,
        "result": f"You provided param1={param1} and param2={param2}."
    }

    return jsonify(response_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
