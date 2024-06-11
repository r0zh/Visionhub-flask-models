# FLASK SERVER
from flask import Flask, send_from_directory, request
from shap_e.util.notebooks import decode_latent_mesh
from flask_cors import CORS

# Initialize the Flask application
app = Flask(__name__)
port = "5000"
CORS(app)

@app.route('/generate', methods=['POST'])
def get_photo():
    guidance_scale = 3.0

    prompt = request.get_json()['prompt']
    batch_size = int(request.get_json()['batchSize'])
    print(prompt)
    print(batch_size)

    if(batch_size==1):
        return send_from_directory("Visionhub-flask-models/shap-e", "models1.zip")
    elif(batch_size==2):
        return send_from_directory("Visionhub-flask-models/shap-e", "models2.zip")
    elif(batch_size==3):
        return send_from_directory("Visionhub-flask-models/shap-e", "models3.zip")
    elif(batch_size==4):
        return send_from_directory("Visionhub-flask-models/shap-e", "models4.zip")

# Start the Flask server
if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)