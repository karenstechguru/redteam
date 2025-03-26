from flask import Flask, request, redirect, render_template, session
import base64
import binascii
import os
import time
from flask_session import Session

app = Flask(__name__)

# Configure Flask-Session (Stores session in memory, not disk)
app.config["SESSION_TYPE"] = "filesystem"  # Uses temporary file storage
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_USE_SIGNER"] = True
app.config["SECRET_KEY"] = os.urandom(24)  # Random secret key for security
Session(app)

def decode_obfuscated_string(data):
    """Decodes an obfuscated URL (Reverse + Hex + Double Base64)."""
    try:
        reversed_data = data[::-1]  # Step 1: Reverse the string
        hex_decoded = binascii.unhexlify(reversed_data).decode()  # Step 2: Hex decode
        base64_once = base64.b64decode(hex_decoded).decode()  # Step 3: Base64 decode (First)
        decoded = base64.b64decode(base64_once).decode()  # Step 4: Base64 decode (Second)
        return decoded
    except Exception as e:
        print("Decoding Error:", str(e))
        return None  # Return None if decoding fails


@app.route("/")
def home():
    """Home route with instructions."""
    return "Welcome! redirecting...."

@app.route("/go")
def go():
    """Handles obfuscated URL and applies a delay before redirecting."""
    obf = request.args.get("d")  # Get the obfuscated URL
    if not obf:
        return "Invalid request", 400  # If no URL, return error

    real_url = decode_obfuscated_string(obf)  # Decode the URL
    if not real_url:
        return "Invalid link", 400  # If decoding fails, return error

    # Track first visit using Flask-Session
    if "first_visit_time" not in session:
        session["first_visit_time"] = time.time()
        return render_template("error.html")  # First visit shows error page

    # If visited before, check if 5 seconds have passed
    elapsed_time = time.time() - session["first_visit_time"]
    if elapsed_time < 5:
        return render_template("error.html")  # Keep showing error page if <5 sec

    # After 5 seconds, redirect to the decoded URL
    return render_template("redirect.html", url=real_url)

if __name__ == "__main__":
    port = int(os.getenv("PORT", 10000))  # Render assigns a port dynamically
    app.run(host="0.0.0.0", port=port, debug=False)
