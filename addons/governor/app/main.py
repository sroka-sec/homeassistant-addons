from flask import Flask, jsonify, request
import json
import os

CONFIG_PATH = "/data/options.json"  # Default path for Home Assistant add-on options

app = Flask(__name__)

@app.route("/")
def index():
    """Serve the web UI."""
    return app.send_static_file("web_ui/index.html")

@app.route("/config", methods=["POST"])
def save_config():
    """Save configuration from the GUI."""
    config_data = request.json
    try:
        with open(CONFIG_PATH, "w") as config_file:
            json.dump(config_data, config_file)
        return jsonify({"message": "Configuration saved successfully!"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/status", methods=["GET"])
def status():
    """Fetch statuses of configured devices."""
    # Example of retrieving saved configuration
    with open(CONFIG_PATH, "r") as config_file:
        config = json.load(config_file)
    main_meter = config.get("main_meter")
    devices = config.get("devices_to_control")
    return jsonify({"main_meter": main_meter, "devices": devices})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
