from flask import Flask, request, jsonify # type: ignore
import torch # type: ignore
from transformers import AutoTokenizer, GPT2LMHeadModel
from typing import Set
from flask_cors import CORS # type: ignore
import time
app = Flask(__name__)
CORS(app)

# Load model and tokenizer once on startup
model_path = r"Backend\GPT2"
model = GPT2LMHeadModel.from_pretrained(model_path, local_files_only=True)
tokenizer = AutoTokenizer.from_pretrained("gpt2", local_files_only=False)

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

@app.route("/generate-passwords", methods=["POST"])
def generate_passwords():
    data = request.json

    required_fields = ["Uname", "Byear", "Fav", "City", "Hobby"]
    if not all(field in data for field in required_fields):
        return jsonify({"error": "Missing required fields."}), 400

    input_text = f"{data['Uname']}|{data['Byear']}|{data['Fav']}|{data['City']}|{data['Hobby']}|"
    inputs = tokenizer(input_text, return_tensors="pt").to(device)
    chunksize = data.get("Chunksize", 100)
    
    start_time  = time.time()
    results: Set[str] = set()
    for _ in range(chunksize):
        outputs = model.generate(
            **inputs,
            max_new_tokens=10,
            do_sample=True,
            top_k=50,
            top_p=0.96,
            temperature=0.65,
            num_return_sequences=3,
            pad_token_id=tokenizer.eos_token_id
        )

        for output in outputs:
            text = tokenizer.decode(output, skip_special_tokens=True)
            parts = text.rsplit("|", 1)
            if len(parts) > 1:
                pw = parts[1].strip()
                if 4 <= len(pw) <= 16:
                    results.add(pw)
                    
    end_time = time.time()
    time_taken = round(end_time - start_time, 2)
    return jsonify({"results": sorted(results),
                    "time_taken_seconds": time_taken})

if __name__ == "__main__":
    app.run(host="192.168.1.197", port=8000)
