from flask import Flask, render_template, request, redirect, url_for
import requests
import json

app = Flask(__name__)

DEFAULTSR = "wholesomememes"

def get_meme(sr):
    url = "https://meme-api.com/gimme/" + sr
    response = json.loads(requests.request("GET", url).text)
    if "preview" not in response:
        return None
    meme_large = response["preview"][-2]
    subreddit = response["subreddit"]
    return meme_large,subreddit

@app.route("/", methods=["GET","POST"])
def index():
    sr = DEFAULTSR
    if (request.method == "POST"):
        sr = request.form.get("inputSub") or DEFAULTSR
    else:
        sr = request.args.get("sr") or DEFAULTSR
    result = get_meme(sr)
    if result is None:
        return redirect(url_for("index",sr=DEFAULTSR))
    meme_pic, subreddit = result
    return render_template("meme_index.html", meme_pic=meme_pic, subreddit=subreddit)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
