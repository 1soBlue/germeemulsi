# A very simple Flask Hello World app for you to get started with...

from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)
# Required for session storage
app.config['SECRET_KEY'] = "language-switching"

#default language is English
DEFAULT_LANG = "en"

@app.route("/")
def index():
    # Get language from URL parameter or session
    lang = request.args.get("lang") or session.get("lang", DEFAULT_LANG)

    session["lang"] = lang

    return render_template("index.html", lang=lang)

@app.route("/switch_lang/<language>")
def switch_language(language):
    # Switch the website language and redirect to home
    session["lang"] = language
    return redirect(url_for("index", lang=language))

if __name__ == "__main__":
    app.run(debug=True)