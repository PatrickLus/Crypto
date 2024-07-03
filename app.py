from flask import Flask, render_template, request, redirect, url_for, flash
from encrypt_decrypt import generate_key, encrypt_message, decrypt_message
from otp_sms import send_otp_via_sms, send_encrypted_message_via_sms
from database import init_db, save_message, get_messages

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Initialize the database
init_db()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/encrypt', methods=['POST'])
def encrypt():
    sender = request.form['sender']
    message = request.form['message']
    receiver = request.form['receiver']

    if not sender or not message or not receiver:
        flash('All fields are required!')
        return redirect(url_for('index'))

    key = generate_key()
    encrypted_message = encrypt_message(message, key)
    otp = key.hex()
    send_otp_via_sms(receiver, otp)
    send_encrypted_message_via_sms(receiver, encrypted_message)
    save_message(sender, receiver, message, encrypted_message, otp)
    flash('Message encrypted and sent successfully!')
    return redirect(url_for('index'))

@app.route('/decrypt', methods=['POST'])
def decrypt():
    encrypted_message = request.form['encrypted_message']
    otp = request.form['otp']

    if not encrypted_message or not otp:
        flash('All fields are required!')
        return redirect(url_for('index'))

    key = bytes.fromhex(otp)
    decrypted_message = decrypt_message(encrypted_message, key)
    flash(f'Decrypted message: {decrypted_message}')
    return redirect(url_for('index'))

@app.route('/messages')
def messages():
    messages = get_messages()
    return render_template('messages.html', messages=messages)

if __name__ == '__main__':
    app.run(debug=True)
