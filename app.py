from flask import Flask, request, jsonify
from flask_cors import CORS  # ✅ Add this
from pynput.keyboard import Controller
import threading
import time

####################### controller code ################

import serial
import serial.tools.list_ports

#######################################################

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

keyboard = Controller()

# Color decision logic
def get_color_decision(red, green, blue, yellow):
    all_colors = {"red": red, "green": green, "blue": blue, "yellow": yellow}
    max_color = max(all_colors, key=all_colors.get)
    max_value = all_colors[max_color]

    # Check if max is unique
    if list(all_colors.values()).count(max_value) == 1:
        return f"{max_color.capitalize()} Max"

    # Almost equal checks (±10)
    pairs = [
        ("red", "green"),
        ("red", "blue"),
        ("red", "yellow"),
        ("green", "blue"),
        ("green", "yellow"),
        ("blue", "yellow")
    ]

    for a, b in pairs:
        if abs(all_colors[a] - all_colors[b]) <= 10 and all_colors[a] != all_colors[b]:
            return f"{a.capitalize()} and {b.capitalize()} almost equal"

    # All zeros
    if all(v == 0 for v in all_colors.values()):
        return "White"

    # Fallback
    for a, b in pairs:
        if abs(all_colors[a] - all_colors[b]) <= 15:
            return "Play default video"

    return "Home screen"

# Map decisions to keys
decision_to_key = {
    "Red Max": 'r',
    "Green Max": 'g',
    "Blue Max": 'b',
    "Yellow Max": 'y',
    "Red and Green almost equal": 'a',
    "Red and Blue almost equal": 'd',
    "Red and Yellow almost equal": 'f',
    "Green and Blue almost equal": 'h',
    "Green and Yellow almost equal": 'j',
    "Blue and Yellow almost equal": 'k',
    "White": 'w',
    "Play default video": 'v',
    "Home screen": 'z'
}

# Press a key
def press_key(key_char):
    keyboard.press(key_char)
    keyboard.release(key_char)
    
########################## controller code ####################

# HEX Commands to send
HEX_ON = bytes.fromhex('A1 B2 C3 D4')
HEX_OFF = bytes.fromhex('D4 C3 B2 A1')

# Baud rate (match with your ESP32 sketch)
BAUD_RATE = 115200

# Auto-detect ESP32 COM port
def detect_esp32_port():
    ports = serial.tools.list_ports.comports()
    for port in ports:
        desc = port.description.lower()
        if "ch340" in desc or "cp210" in desc or "silicon" in desc or "usb serial" in desc:
            return port.device
    return None


# Send command and receive response
def send_command(port, baud, command_bytes):
    try:
        with serial.Serial(port, baud, timeout=2) as ser:
            ser.reset_input_buffer()
            ser.write(command_bytes)
            response = ser.readline().decode().strip()
            return response
    except Exception as e:
        return f"Error: {e}"
    
def Send_payload(data , CMD):

    payload = [0,0,0,0,0]

    payload[0] = 0x81
    payload[1] = 0x05
    payload[2] = CMD
    payload[3] = data
    payload[4] = 0x80

    return payload

# Button actions
def turn_on(selected_port):
    # response = send_command(port, BAUD_RATE, HEX_ON)
    response = send_command(selected_port, BAUD_RATE, Send_payload(0x0A,0x03))
    print(Send_payload(0x0A,0x03))

def turn_off(selected_port):
    # response = send_command(port, BAUD_RATE, HEX_OFF)
    response = send_command(selected_port, BAUD_RATE, Send_payload(0x0A,0x01))
    print(Send_payload(0x0A,0x01))



##############################################################

# API route
@app.route('/', methods=['POST'])
def handle_colors():
    print("📩 API hit: POST /")
    data = request.json

    # breakpoint()
    try:
        red = int(data['red']['value'])
        green = int(data['green']['value'])
        blue = int(data['blue']['value'])
        yellow = int(data['yellow']['value'])
    except (KeyError, ValueError, TypeError):
        print("❌ Invalid input:", data)
        return jsonify({"error": "Invalid input"}), 400
    
    # send com

    decision = get_color_decision(red, green, blue, yellow)
    
    ####################### controller code #########################
    
    # Step: 1 : select the port
    selected_port = detect_esp32_port()
    
    if selected_port:
        print(F"port {selected_port} selected for controller data communication")
        # Step: 2 : turn on
        turn_on(selected_port)
        
        # step: 3 : Turn off
        turn_off(selected_port)
    else:
        print("No port selected for controller data communication")
    
    
    ################################################################ 
    
    key_char = decision_to_key.get(decision)

    if key_char and decision != "Home screen":
        def press_and_return_home():
            press_key(key_char)
            print(f"✔ Pressed: {key_char} for '{decision}'")
            time.sleep(10)
            home_key = decision_to_key["Home screen"]
            press_key(home_key)
            print(f"✔ Returned to Home screen with key: {home_key}")

        threading.Thread(target=press_and_return_home).start()
        return jsonify({"decision": decision, "pressed": key_char, "followup": "Home screen"})

    elif key_char == 'z':
        press_key('z')
        print("✔ Pressed: Home screen directly")
        return jsonify({"decision": decision, "pressed": 'z'})

    else:
        print(f"⚠️ No matching key for decision: {decision}")
        return jsonify({"decision": decision, "pressed": None})

if __name__ == '__main__':
    app.run(port=3000)