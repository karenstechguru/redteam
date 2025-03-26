import base64
import binascii

def encode_url(real_url):
    """Encodes a URL using Double Base64 -> Hex -> Reverse."""
    # First Base64 Encode
    base64_encoded_1 = base64.b64encode(real_url.encode()).decode()
    
    # Second Base64 Encode (Extra Layer)
    base64_encoded_2 = base64.b64encode(base64_encoded_1.encode()).decode()
    
    # Convert to Hex
    hex_encoded = binascii.hexlify(base64_encoded_2.encode()).decode()
    
    # Reverse the string
    obfuscated = hex_encoded[::-1]
    
    return obfuscated

# Example usage
real_url = "http://google.com"
obfuscated_string = encode_url(real_url)

# Generate the redirect link
redirect_link = f"https://redteam-u6uk.onrender.com/go?d={obfuscated_string}"

print("Generated Redirect Link:", redirect_link)
