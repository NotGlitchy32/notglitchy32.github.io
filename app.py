from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory storage for user data
donationAmount = 0.0
users = {}
secondsElapsed = 0

# Route to receive donations from frontend
@app.route('/donate', methods=['POST'])
def donate():
    global donationAmount, users, secondsElapsed

    data = request.json
    username = data.get('username')
    amount = float(data.get('amount', 0))

    donationAmount += amount
    if username in users:
        users[username] += amount
    else:
        users[username] = amount

    secondsElapsed += 1

    return jsonify({'message': 'Donation received successfully.'}), 200

# Route to retrieve admin panel data
@app.route('/admin', methods=['GET'])
def admin_panel():
    global donationAmount, users

    if request.args.get('secret_key') == 'your_admin_secret_key':
        return jsonify({
            'total_donation_amount': donationAmount,
            'user_donations': users
        }), 200
    else:
        return jsonify({'error': 'Unauthorized'}), 401

if __name__ == '__main__':
    app.run(debug=True)
