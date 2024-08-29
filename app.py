from flask import Flask, render_template, request
import google.generativeai as palm
import os

# Configure the API key for Google PaLM
api = "AIzaSyD4FLlHsBs4L8F5W1V7_jnyXZR46f4iUX4"
palm.configure(api_key=api)

# Define the model to use (Gemini 1.5)
model = {"model": "gemini-1.5-flash"}

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")

@app.route("/ai_agent", methods=["GET", "POST"])
def ai_agent():
    return render_template("ai_agent.html")

@app.route("/ai_agent_reply", methods=["GET", "POST"])
def ai_agent_reply():
    q = request.form.get("q")
    response = palm.chat(model=model["model"], messages=[{"role": "user", "content": q}])
    r = response['candidates'][0]['content']
    return render_template("ai_agent_reply.html", r=r)

@app.route("/prediction", methods=["GET", "POST"])
def prediction():
    return render_template("index.html")

if __name__ == "__main__":
    app.run()

