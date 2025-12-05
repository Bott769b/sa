from flask import Flask, request, jsonify
import vertex_exploit_fixed as ve
import os

app = Flask(__name__)
vertex = ve.VertexBypassFixed()

@app.route('/')
def index():
    return "🚀 Veo3 Bypass Active - Valid Library ID Format"

@app.route('/api/generate', methods=['POST'])
def generate():
    data = request.json
    result = vertex.generate_video(data.get('prompt', ''))
    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
