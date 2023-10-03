import os
import openai
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__, static_url_path='/static', static_folder='static')

openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        
        user_input_type = request.form.get("user_input_type")
        user_input_subject = request.form.get("user_input_subject")

        generated_text = generate_poetry(user_input_type, user_input_subject)

        return render_template("index.html", generated_text=generated_text)

    return render_template("index.html")

def generate_poetry(user_input_type, user_input_subject):
    try:
        prompt = f"Write a {user_input_type} about {user_input_subject}. please write <br/> at the end of each line"

        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=prompt,
            max_tokens=200
        )

        generated_text = response.choices[0].text.strip()
        generated_text_split = generated_text.split("<br>")
        

        return generated_text
    except Exception as e:
        
        return str(e)


if __name__ == "__main__":
    app.run(debug=True)
