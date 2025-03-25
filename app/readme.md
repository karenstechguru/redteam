# Time-Based Redirect with Obfuscation

This project creates a **time-delayed redirect** that initially returns a **404 error** and requires a **manual refresh** before decoding and redirecting after **6 seconds**.

## 🔥 Features:
- **Fake 404 error page** on first visit.
- **Manual refresh triggers decoding.**
- **6-second delay before redirection.**
- **Obfuscates URLs (Base64 + Hex + Reverse).**
- **Looks like a tracking link for stealth.**

## 🚀 How to Use
### 1️⃣ Run Locally:
```bash
python app/app.py
```
### 2️⃣ Generate an Obfuscated Link:
```bash
python app/encoder.py
```
- Enter the real URL you want to hide.
- Copy the generated obfuscated link.

### 3️⃣ Test the Generated Link:
- Open the link in a browser.
- **First visit:** Shows a **404 error page**.
- **Manual refresh:** Decodes and loads a waiting page.
- **After 6 seconds:** Automatically redirects to the real URL.

## 📌 Directory Structure
```
/your_project/
│── app/
│   ├── app.py         # Main Flask App
│   ├── encoder.py     # URL Obfuscation Script
│   ├── templates/
│   │   ├── error.html      # Fake 404 Page
│   │   ├── loading.html    # Wait 6s before redirect
│   │   ├── redirect.html   # Final redirect page
│── Procfile           # Railway deployment instruction
│── runtime.txt        # Python version
│── requirements.txt   # Python dependencies
│── README.md          # Documentation
```

## 🚀 Deployment
1️⃣ **Push to GitHub:**
```bash
git add .
git commit -m "Initial commit"
git push origin main
```

2️⃣ **Deploy on Railway:**
- Connect your GitHub repo to Railway.
- Deploy the project.
- Get your hosted URL for sharing obfuscated links.

🚀 **Now your obfuscation-based redirect is live!**

#----> CREATED BY TechGirlNerd <-----