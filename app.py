from flask import Flask, render_template, request, jsonify
import random
import string
import time
import os

app = Flask(__name__)

# Fake Vertex AI generator
class FakeVertexAI:
    def generate_video(self, prompt):
        video_id = ''.join(random.choices(string.hexdigits.lower(), k=32))
        return {
            "video_url": f"https://storage.googleapis.com/fake-bucket/{video_id}.mp4",
            "job_id": f"projects/free-veo3/locations/us-central1/operations/{video_id}",
            "status": "SUCCESS",
            "cost": 0.00,
            "billing_trick": "RESEARCH_GRANT_BYPASS_ACTIVE"
        }

# Routes
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    fake_ai = FakeVertexAI()
    data = request.json
    
    # Simulate processing
    time.sleep(1.5)
    
    # Generate fake video
    result = fake_ai.generate_video(data.get('prompt', ''))
    
    # Log manipulation
    print(f"[BYPASS] Generated video with $0 cost | Prompt: {data.get('prompt', '')}")
    
    return jsonify(result)

# Vercel needs this
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)
