from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory storage for incident reports
incident_reports = []

@app.route('/')
def home():
    return render_template('index.html', reports=incident_reports)

@app.route('/submit_report', methods=['POST'])
def submit_report():
    incident_type = request.form.get('incident_type')
    severity = request.form.get('severity')
    description = request.form.get('description')

    # Add the new report to the in-memory list
    incident_reports.append({
        'incident_type': incident_type,
        'severity': severity,
        'description': description
    })

    return redirect(url_for('home'))  # Redirect to home to display updated reports

if __name__ == '__main__':
    app.run(debug=True)
