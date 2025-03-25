import base64
import binascii

def encode_url(real_url):
    # Encode in Base64
    base64_encoded = base64.b64encode(real_url.encode()).decode()
    
    # Convert to Hex
    hex_encoded = binascii.hexlify(base64_encoded.encode()).decode()
    
    # Reverse the string
    obfuscated = hex_encoded[::-1]
    
    return obfuscated

# Example usage
real_url = "http://google.com"
obfuscated_string = encode_url(real_url)

# Generate a disguised tracking-style link
tracking_id = "track-" + obfuscated_string[:10]  # Fake tracking ID
redirect_link = f"http://127.0.0.1:5000/go?track={tracking_id}&d={obfuscated_string}"

print("Generated Redirect Link:", redirect_link)