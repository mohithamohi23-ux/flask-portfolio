from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "change-this-to-a-random-string"

@app.route("/")
def index():
    person = {
        "name": "Your Name",
        "title": "Developer",
        "bio": "Short bio about you.",
        "skills": ["Python", "Flask", "HTML", "CSS"],
        "projects": [
            {"title": "Project One", "desc": "Short description", "link": "#"},
            {"title": "Project Two", "desc": "Short description", "link": "#"}
        ]
    }
    return render_template("index.html", person=person)

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip()
        message = request.form.get("message", "").strip()
        print("Contact submission:",name,email,message)

        if not name or not email or not message:
            flash("Please fill in all fields.", "error")
            return redirect(url_for("contact"))

        # For this task we simply print the message to the console.
        print("Contact submission:", name, email, message)

        flash("Thanks — your message was sent!", "success")
        return redirect(url_for("contact"))

    return render_template("contact.html", person=None)
    
if __name__ == "__main__":
    app.run(debug=True)
