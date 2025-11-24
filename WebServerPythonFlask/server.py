from flask import Flask, request

app = Flask(__name__)

# Home page
@app.route("/", methods=["GET", "POST"])
def home():
    # Print REQUEST details in the server console
    print("=== New Request ===")
    print("Method:", request.method)
    print("Path:", request.path)
    print("Headers:")
    for k, v in request.headers.items():
        print(f"  {k}: {v}")
    print("===================\n")

    # This is the RESPONSE body
    return "Hello from Flask Web Server!"

# Extra route to show JSON response
@app.route("/info")
def info():
    return {
        "message": "This is /info endpoint",
        "method": request.method,
        "client_ip": request.remote_addr,
    }

if __name__ == "__main__":
    # Start the server on port 5000
    app.run(host="0.0.0.0", port=5000)
