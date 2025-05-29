from flask import Flask, jsonify, request
import json

app = Flask(__name__)


@app.route("/")
def load_modules():
    with open("modules.json", "r") as f:
        return json.load(f)
app.route("/modules", methods=["GET"])
def get_modules():
    modules=load_modules()
    return jsonify(modules)
app.run(host='0.0.0.0', port=81)

def save_modules(data):
    with open("modules.json", "w") as f:
        json.dump(data, f, indent=4)
app.route("/modules", methods=["POST"])
def add_module():
    data= request.get(json)
    week= data.get("week")
    resource= data.get("resource")

    if not week or not resource:
        return jsonify({"error": "Missing week or resource"}), 400

    modules= load_modules()

    if week in modules:
        modules[week].append(resource)
    else:
        modules[week] = [resource]

    save_modules(modules)

    return jsonify({"message":f"Resource added to week {week}"}), 201
    app.run(host='0.0.0.0', port=81)
