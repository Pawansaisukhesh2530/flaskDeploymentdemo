from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Flask Demo Application!"

@app.route('/about')
def about():
    return "This is a simple Flask application"

@app.route('/courses')
def courses():
    return "Courses offered: BCA, BSc, MCA, MSc"

@app.route("/contact")
def contact():
    return "Email: cs@example.com"

@app.route("/profile")
def profile():
    return """
    <h1>Student Profile</h1>
    <p><strong>Name:</strong> Sukhesh</p>
    <p><strong>Age:</strong> 20</p>
    <p><strong>Email:</strong> sukhesh@example.com</p>
    <p><strong>Phone:</strong> +91 98765 43210</p>
    """

@app.route("/subjects")
def subjects():
    return """
    <h1>Student Subjects</h1>
    <ul>
        <li>Python Programming</li>
        <li>Database Management Systems</li>
        <li>Web Development</li>
        <li>Computer Networks</li>
        <li>Data Structures</li>
    </ul>
    """

if __name__ == "__main__":
    app.run(debug=True)