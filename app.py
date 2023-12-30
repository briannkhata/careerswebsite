from flask import Flask, jsonify, render_template

app = Flask(__name__)

jobs = [
    {
        "title": "Software Engineer",
        "company": "TechCo",
        "location": "City A",
        "salary": 90000,
    },
    {
        "title": "Data Analyst",
        "company": "DataCorp",
        "location": "City B",
        "salary": 75000,
    },
    {
        "title": "UX Designer",
        "company": "DesignWorks",
        "location": "City C",
        "salary": 80000,
    },
    {
        "title": "Marketing Specialist",
        "company": "AdvertiseCo",
        "location": "City D",
        "salary": 70000,
    },
    {
        "title": "Financial Analyst",
        "company": "FinanceCorp",
        "location": "City E",
        "salary": 85000,
    },
    {
        "title": "Graphic Designer",
        "company": "CreativeDesign",
        "location": "City F",
        "salary": 65000,
    },
    {
        "title": "Project Manager",
        "company": "ProjectCo",
        "location": "City G",
        "salary": 95000,
    },
    {
        "title": "Sales Representative",
        "company": "SalesCorp",
        "location": "City H",
        "salary": 75000,
    },
    {
        "title": "Customer Support Specialist",
        "company": "SupportCo",
        "location": "City I",
        "salary": 60000,
    },
    {
        "title": "Network Administrator",
        "company": "NetworkTech",
        "location": "City J",
        "salary": 85000,
    },
    {
        "title": "HR Manager",
        "company": "HRWorks",
        "location": "City K",
        "salary": 90000,
    },
    {
        "title": "Content Writer",
        "company": "ContentCo",
        "location": "City L",
        "salary": 70000,
    },
    {
        "title": "Software Tester",
        "company": "TestingTech",
        "location": "City M",
        "salary": 80000,
    },
    {
        "title": "Event Coordinator",
        "company": "EventCo",
        "location": "City N",
        "salary": 70000,
    },
    {
        "title": "Legal Counsel",
        "company": "LegalFirm",
        "location": "City O",
        "salary": 100000,
    },
]


@app.route('/')
def hello():
    return render_template("home.html",jobs=jobs)

@app.route('/api/jobs')
def list_jobs():
    return jsonify(jobs)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True,use_reloader=True)