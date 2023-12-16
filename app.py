from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS=[
  {
    'id':1,
    'title':'Frontend developer',
    'location':'Toronto, Canada',
    'salary':'$60k - $80k'
  },
  {
    'id':2,
    'title':'Backend developer',
    'location':'Surabaya, Indonesia',
    'salary':'$80k - $120k',
  },
  {
    'id':3,
    'title': 'Data scientist',
    'location': 'Tokyo, Japan',
    'salary': '$100k - $140k',
  },
  {
    'id':4,
    'title': 'ML engineer',
    'location': 'Remote',
    'salary': '$70k - $90k',
  }
]


@app.route("/")
def hello_world():
  return render_template('home.html',jobs=JOBS,company_name="pH") # Shows the home webpage

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
