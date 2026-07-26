 import os
from flask import Flask, send_from_directory, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.get_json()
    query = data.get('query', '').lower().strip()

    if not query:
        return jsonify({"score": 0, "explanation": "לא התקבל נושא"}), 400

    # לוגיקה בסיסית לדירוג מדעיות בבריאות הנפש
    scientific_keywords = [
        'cbt', 'cognitive behavioral', 'rct', 'randomized', 'meta-analysis',
        'systematic review', 'evidence-based', 'dsm', 'icd', 'clinical trial',
        'peer-reviewed', 'pubmed', 'apa', 'nice guidelines', 'efficacy',
        'depression', 'anxiety', 'ptsd', 'ocd', 'bipolar'
    ]

    pseudo_keywords = [
        'manifest', 'law of attraction', 'toxic positivity', 'vibes',
        'heal yourself', 'just think positive', 'energy healing',
        'crystal', 'chakra', 'quantum healing'
    ]

    score = 40  # נקודת התחלה ניטרלית
    reasons = []

    for word in scientific_keywords:
        if word in query:
            score += 12
            reasons.append(f"נמצא מונח מדעי: {word}")

    for word in pseudo_keywords:
        if word in query:
            score -= 18
            reasons.append(f"נמצא מונח לא מדעי: {word}")

    score = max(0, min(100, score))

    if score >= 75:
        level = "גבוהה – מבוסס מחקר"
    elif score >= 45:
        level = "בינונית – מעורב"
    else:
        level = "נמוכה – לא מבוסס מדעית"

    explanation = f"רמת מדעיות: {level}. " + (" | ".join(reasons) if reasons else "לא זוהו מונחים חזקים.")

    return jsonify({
        "score": score,
        "explanation": explanation
    })

@app.route('/health')
def health():
    return jsonify({"status": "healthy", "focus": "mental-health scientific rating"})

if __name__ == '__main__':
    print("[+] VidAI running on http://0.0.0.0:5002")
    app.run(host='0.0.0.0', port=5002, debug=False)
