from flask import Flask, request, jsonify
import os

app = Flask(__name__)

# Placeholder storage for user donations
users = {}

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/donate', methods=['POST'])
def donate():
    global users

    data = request.json
    username = data.get('username')
    donation_amount = float(data.get('donationAmount'))

    if username:
        if username not in users:
            users[username] = 0.0
        users[username] += donation_amount

        return jsonify({'message': f'Donation of ${donation_amount} received for {username}.'}), 200
    else:
        return jsonify({'error': 'Username not provided.'}), 400

@app.route('/admin/user_donations', methods=['GET'])
def user_donations():
    global users
    return jsonify(users), 200

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 4000))  # Read the PORT environment variable or default to 4000
    app.run(debug=True, host='0.0.0.0', port=port)
