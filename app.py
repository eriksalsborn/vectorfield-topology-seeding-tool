from flask import Flask, send_file, send_from_directory
import main

app = Flask(__name__)

@app.route('/')
def index():
    return 'Web App with Python Flask!'

@app.get('/get_dayside_csv_file')
def get_csvfile():
    # run main file
    main.main()
    return send_file('C:/Dev/cloneV4/vectorfield-topology-seeding-tool/dayside_file.csv') # TODO: Replace path to folder with auto var