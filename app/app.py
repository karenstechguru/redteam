from flask import Flask, request, redirect, render_template
import base64
import binascii
import time

app = Flask(__name__)

# Temporary storage for tracking visits (resets when app restarts)
visit_tracker = {}

def decode_obfuscated_string(data):
    try:
        reversed_data = data[::-1]  # Reverse back
        hex_decoded = binascii.unhexlify(reversed_data).decode()  # Convert Hex to text
        decoded = base64.b64decode(hex_decoded).decode()  # Decode Base64
        return decoded
    except:
        return None

@app.route("/go")
def go():
    obf = request.args.get("d")

    if not obf:
        return "Missing parameter", 400

    # Check if this obfuscated link has been visited before
    if obf not in visit_tracker:
        visit_tracker[obf] = True  # Mark it as visited
        return render_template("error.html"), 404  # Show error page first

    real_url = decode_obfuscated_string(obf)

    if real_url:
        return render_template("loading.html", real_url=real_url)  # Redirects after 5 sec
    else:
        return "Invalid link", 400

if __name__ == "__main__":
    app.run(debug=True)
