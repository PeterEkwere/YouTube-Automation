#!/usr/bin/python
"""
    This is the application point of entry
    Author Peter Ekwere
"""
from flask import Flask, render_template, request, jsonify, redirect
from run import like_comments
import json

app = Flask(__name__)


@app.route('/')
def index():
  return render_template('index (2).html')

@app.route('/write-urls', methods=['POST'])
def write_urls():
  try:
    # Get the request data as JSON
    data = request.get_json()

    # Validate data (optional)

    # Open urls.json in write mode
    if data:
        with open('urls.json', 'w') as f:
            json.dump(data, f, indent=2)  # Indent for readability

    return redirect('/like_comment')

  except Exception as e:
    print(f'Error writing to urls.json: {e}')
    return 'Error writing URLs!', 500


@app.route('/like_comment', methods=['GET'])
def like_comment():
  # This endpoint doesn't need any modifications.
  #print("Entered like comment endpoint successfully")
  status = like_comments()
  if status == "Done":
      return jsonify({'message': 'Script Finished Successfully'}), 200
  else:
      return jsonify({'message': 'An Error Occured Running the Script'})


if __name__ == '__main__':
  app.run(host="0.0.0.0", port=5000, debug=True)