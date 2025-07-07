

# # # from collections import Counter

# # # input_list = [1, 2, 2, 5, 8, 4, 4, 8]

# # # counter = Counter(input_list)

# # # result = dict(counter)

# # # # print(len(set(input_list)))

# # # a = [1, 3, 5, 6, 3, 5, 6, 1]

# # # uniques = set(a)
# # # result = 1
# # # for item in uniques:
# # #     result *= item
    
# # # print(result)




# # def convert_to_hex(input_array):
    
# #     hex_array = [hex(num) for num in input_array]
        
# #     return hex_array

# # result = convert_to_hex([10, 20, 30, 40])
# # print(result)



# import tkinter as tk
# from tkinter import ttk, messagebox
# import serial
# import serial.tools.list_ports

# # HEX Commands to send
# HEX_ON = bytes.fromhex('A1 B2 C3 D4')
# HEX_OFF = bytes.fromhex('D4 C3 B2 A1')

# # Baud rate (match with your ESP32 sketch)
# BAUD_RATE = 115200


# def Send_payload(data , CMD):

#     payload = [0,0,0,0,0]

#     payload[0] = 0x81
#     payload[1] = 0x05
#     payload[2] = CMD
#     payload[3] = data
#     payload[4] = 0x80

#     return payload

# # Auto-detect ESP32 COM port
# def detect_esp32_port():
#     ports = serial.tools.list_ports.comports()
#     for port in ports:
#         desc = port.description.lower()
#         if "ch340" in desc or "cp210" in desc or "silicon" in desc or "usb serial" in desc:
#             return port.device
#     return None

# # List all ports for manual selection
# def list_serial_ports():
#     return [port.device for port in serial.tools.list_ports.comports()]

# # Send command and receive response
# def send_command(port, baud, command_bytes):
#     try:
#         with serial.Serial(port, baud, timeout=2) as ser:
#             ser.reset_input_buffer()
#             ser.write(command_bytes)
#             response = ser.readline().decode().strip()
#             return response
#     except Exception as e:
#         return f"Error: {e}"

# # GUI Application
# def create_gui():
#     root = tk.Tk()
#     root.title("ESP32 UART Controller")
#     root.geometry("400x350")
#     root.resizable(False, False)

#     selected_port = tk.StringVar()

#     # Auto-detect ESP32 port
#     auto_detected = detect_esp32_port()
#     if auto_detected:
#         selected_port.set(auto_detected)
#     else:
#         selected_port.set("Select COM Port")

#     tk.Label(root, text="ESP32 COM Port", font=("Arial", 12)).pack(pady=10)

#     port_menu = ttk.Combobox(root, textvariable=selected_port, values=list_serial_ports(), state="readonly")
#     port_menu.pack()

#     status_label = tk.Label(root, text="Device is OFF", font=("Arial", 16), fg="red")
#     status_label.pack(pady=20)

#     response_label = tk.Label(root, text="Waiting for response...", font=("Arial", 10), fg="blue")
#     response_label.pack(pady=10)

#     # Button actions
#     def turn_on():
#         port = selected_port.get()
#         if "COM" not in port:
#             messagebox.showwarning("Select Port", "Please select a valid COM port.")
#             return
#         status_label.config(text="Device is ON", fg="green")
#         # response = send_command(port, BAUD_RATE, HEX_ON)
#         response = send_command(port, BAUD_RATE, Send_payload(0x0A,0x03))
#         print(Send_payload(0x0A,0x03))
#         response_label.config(text=f"ESP32 says: {response}")

#     def turn_off():
#         port = selected_port.get()
#         if "COM" not in port:
#             messagebox.showwarning("Select Port", "Please select a valid COM port.")
#             return
#         status_label.config(text="Device is OFF", fg="red")
#         # response = send_command(port, BAUD_RATE, HEX_OFF)
#         response = send_command(port, BAUD_RATE, Send_payload(0x0A,0x01))
#         print(Send_payload(0x0A,0x01))
#         response_label.config(text=f"ESP32 says: {response}")

#     # Buttons
#     tk.Button(root, text="Turn ON", command=turn_on, bg="green", fg="white", width=15, height=2).pack(pady=5)
#     tk.Button(root, text="Turn OFF", command=turn_off, bg="red", fg="white", width=15, height=2).pack(pady=5)

#     # Refresh COM ports
#     def refresh_ports():
#         port_menu["values"] = list_serial_ports()
#         auto = detect_esp32_port()
#         if auto:
#             selected_port.set(auto)

#     tk.Button(root, text="Refresh Ports", command=refresh_ports).pack(pady=10)

#     root.mainloop()

# if __name__ == "__main__":
#     create_gui()
    
    
    
# from flask import Flask, request, jsonify
# from flask_cors import CORS  # ✅ Add this
# from pynput.keyboard import Controller
# import threading
# import time

# app = Flask(__name__)
# CORS(app, resources={r"/*": {"origins": "*"}})

# keyboard = Controller()

# # Color decision logic
# def get_color_decision(red, green, blue, yellow):
#     all_colors = {"red": red, "green": green, "blue": blue, "yellow": yellow}
#     max_color = max(all_colors, key=all_colors.get)
#     max_value = all_colors[max_color]

#     # Check if max is unique
#     if list(all_colors.values()).count(max_value) == 1:
#         return f"{max_color.capitalize()} Max"

#     # Almost equal checks (±10)
#     pairs = [
#         ("red", "green"),
#         ("red", "blue"),
#         ("red", "yellow"),
#         ("green", "blue"),
#         ("green", "yellow"),
#         ("blue", "yellow")
#     ]

#     for a, b in pairs:
#         if abs(all_colors[a] - all_colors[b]) <= 10 and all_colors[a] != all_colors[b]:
#             return f"{a.capitalize()} and {b.capitalize()} almost equal"

#     # All zeros
#     if all(v == 0 for v in all_colors.values()):
#         return "White"

#     # Fallback
#     for a, b in pairs:
#         if abs(all_colors[a] - all_colors[b]) <= 15:
#             return "Play default video"

#     return "Home screen"

# # Map decisions to keys
# decision_to_key = {
#     "Red Max": 'r',
#     "Green Max": 'g',
#     "Blue Max": 'b',
#     "Yellow Max": 'y',
#     "Red and Green almost equal": 'a',
#     "Red and Blue almost equal": 'd',
#     "Red and Yellow almost equal": 'f',
#     "Green and Blue almost equal": 'h',
#     "Green and Yellow almost equal": 'j',
#     "Blue and Yellow almost equal": 'k',
#     "White": 'w',
#     "Play default video": 'v',
#     "Home screen": 'z'
# }

# # Press a key
# def press_key(key_char):
#     keyboard.press(key_char)
#     keyboard.release(key_char)

# # API route
# @app.route('/', methods=['POST'])
# def handle_colors():
#     print("📩 API hit: POST /")
#     data = request.json


#     try:
#         red = int(data['red']['value'])
#         green = int(data['green']['value'])
#         blue = int(data['blue']['value'])
#         yellow = int(data['yellow']['value'])
#     except (KeyError, ValueError, TypeError):
#         print("❌ Invalid input:", data)
#         return jsonify({"error": "Invalid input"}), 400

#     decision = get_color_decision(red, green, blue, yellow)
#     key_char = decision_to_key.get(decision)

#     if key_char and decision != "Home screen":
#         def press_and_return_home():
#             press_key(key_char)
#             print(f"✔ Pressed: {key_char} for '{decision}'")
#             time.sleep(10)
#             home_key = decision_to_key["Home screen"]
#             press_key(home_key)
#             print(f"✔ Returned to Home screen with key: {home_key}")

#         threading.Thread(target=press_and_return_home).start()
#         return jsonify({"decision": decision, "pressed": key_char, "followup": "Home screen"})

#     elif key_char == 'z':
#         press_key('z')
#         print("✔ Pressed: Home screen directly")
#         return jsonify({"decision": decision, "pressed": 'z'})

#     else:
#         print(f"⚠️ No matching key for decision: {decision}")
#         return jsonify({"decision": decision, "pressed": None})

# if __name__ == '__main__':
#     app.run(port=3000)


from collections import defaultdict


listA = [
    "Sparsh,Aishwarya,Abhay,Rohit",
    "Aishwarya,Amit,Jainisha",
    "Rohit,Suman,Animesh",
    "Pallav,Sparsh"
]

tree = defaultdict(list)    # dict to store parent and children (defaults to a list) 
all_children = set()

# Expected dictionary tree
# {
#     'Sparsh': ['Aishwarya', 'Abhay', 'Rohit'], 
#     'Aishwarya': ['Amit', 'Jainisha'], 
#     'Rohit': ['Suman', 'Animesh'], 
#     'Pallav': ['Sparsh']
# }

for entry in listA:
    members = entry.split(',')
    parent = members[0]
    children = members[1:]
    tree[parent].extend(children)
    all_children.update(children)


all_parents = set(tree.keys())  # get parents set from tree dict keys
roots = list(all_parents - all_children)  # There could be multiple roots

# Recursive function to print tree
def print_tree(node, level=0):
    print("----" * level + node)
    for child in tree.get(node, []):
        print_tree(child, level + 1)

# Print from each root
for root in roots:
    print_tree(root)
    