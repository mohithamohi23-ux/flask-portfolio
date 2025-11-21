# Flask Portfolio Website 

This project is a simple portfolio website built using **Flask**, **HTML**, and **CSS**.
It includes a homepage with personal details and a working contact form that displays flash messages and prints form submissions to the terminal.

---

## 🚀 Features
- **Homepage** with name, bio, skills, and projects
- **Contact Form** with Name, Email, and Message
- **Flash Messages** for success and error
- **Styled layout** using external CSS
- **Templates** with Flask’s Jinja2 templating
- **Static files** (CSS) organized properly
- Form data displayed in the **VS Code terminal**

---

## 📂 Project Structure
```
flask-portfolio/
│ app.py
│ requirements.txt
│ README.md
│
├── templates/
│   ├── base.html
│   ├── index.html
│   └── contact.html
│
└── static/
    └── css/
        └── style.css
```

---

## 🛠 Technologies Used
- Python  
- Flask  
- HTML  
- CSS  
- Jinja2 Templates  
- VS Code  

---

## 🧠 What I Learned
While doing this project, I learned:

### ✔ Flask Basics
- How to create routes using `@app.route`
- How to run a Flask development server
- How to return templates with `render_template()`

### ✔ HTML Templating (Jinja2)
- Using `{% block %}` and `{% extends %}`
- Passing variables from Flask to HTML
- Linking static files with `url_for()`

### ✔ Contact Form Handling
- Handling GET and POST requests
- Capturing form data using `request.form`
- Displaying flash messages using `flash()`
- Printing form submissions in the terminal

### ✔ Static File Management
- Placing CSS inside the `static/` folder
- Correctly linking stylesheets in HTML

### ✔ Debugging Skills
- Fixing broken file paths
- Solving CSS not loading issues
- Restarting Flask server to apply changes

### ✔ Git & GitHub Usage
- Initializing a git repository
- Committing changes
- Pushing a project to a GitHub repository

---

## 🖼 Screenshots
Add screenshots inside your **screenshots** folder.

Example:
- `screenshots/homepage.png`
- `screenshots/contact_success.png`
- `screenshots/terminal_output.png`

To display them:

```markdown
![Homepage](screenshots/homepage.png)
![Contact Success](screenshots/contact_success.png)
![Terminal Output](screenshots/terminal_output.png)
```

---

## ▶️ How to Run the Project Locally

### 1. Clone the repository
```
git clone https://github.com/YOUR-USERNAME/flask-portfolio.git
cd flask-portfolio
```

### 2. Create a virtual environment
```
python -m venv .venv
```

### 3. Activate the environment (Windows)
```
.venv\Scripts\Activate.ps1
```

### 4. Install dependencies
```
pip install -r requirements.txt
```

### 5. Run the Flask server
```
python app.py
```

### 6. Open in browser
```
http://127.0.0.1:5000/
```
