"""
Batch prediction helper (CLI).

Usage
-----
python -m src.models.predict --input sample.json --model models/model.pkl
"""
import argparse
import json
import joblib

def main(input_path: str, model_path: str = "models/model.pkl") -> None:
    model = joblib.load(model_path)
    with open(input_path) as f:
        payload = json.load(f)
    values = payload.get("values", [])
    pred = model.predict([values])[0]
    print(json.dumps({"prediction": float(pred)}))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--model", default="models/model.pkl")
    args = parser.parse_args()
    main(args.input, args.model)

