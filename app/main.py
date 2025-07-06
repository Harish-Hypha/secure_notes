from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from secret_loader import get_db_credentials

app = Flask(__name__)

creds = get_db_credentials()
db_url = f"postgresql://{creds['username']}:{creds['password']}@{creds['host']}:{creds['port']}/{creds['database']}"

app.config['SQLALCHEMY_DATABASE_URI'] = db_url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(255), nullable=False)

with app.app_context():
    db.create_all()
    
@app.route("/")
def home():
    return jsonify({"message": "Welcome to Secure Notes API"})

@app.route("/health", methods=["GET"])
def health_check():
    return jsonify({"status": "ok"}), 200

@app.route("/notes", methods=["GET"])
def get_notes():
    return jsonify(notes), 200

@app.route("/notes", methods=["POST"])
def add_note():
    data = request.get_json()
    if not data or "title" not in data or "content" not in data:
        return jsonify({"error": "Missing fields"}), 400
    note = {
        "id": len(notes) + 1,
        "title": data["title"],
        "content": data["content"]
    }
    notes.append(note)
    return jsonify(note), 201

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
