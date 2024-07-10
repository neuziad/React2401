from flask import Flask, jsonify, request
from flask_cors import CORS
import re

app = Flask(__name__)
CORS(app)

# Splits hex colour for processing
def get_colour(hex_colours):
    # Remove the character '#' from hex_colours
    hex_colours = hex_colours.lstrip("#")

    # Split hex_colours into 3 separate r, g, and b values
    r = hex_colours[0:2]
    g = hex_colours[2:4]
    b = hex_colours[4:6]

    return [r, g, b]

def generate_hat_colour(get_colour):
    hat_string = (
        f"8107EC38 {get_colour[0]}{get_colour[1]}\n"
        f"8107EC3A {get_colour[2]}00\n"
        f"8107EC3C {get_colour[0]}{get_colour[1]}\n"
        f"8107EC3E {get_colour[2]}00\n"
        f"8107EC40 {get_colour[0]}{get_colour[1]}\n"
        f"8107EC42 {get_colour[2]}00\n"
        f"8107EC44 {get_colour[0]}{get_colour[1]}\n"
        f"8107EC46 {get_colour[2]}00"
    )

    return hat_string

def generate_overalls_colour(get_colour):
    overalls_string = (
        f"8107EC20 {get_colour[0]}{get_colour[1]}\n"
        f"8107EC22 {get_colour[2]}00\n"
        f"8107EC24 {get_colour[0]}{get_colour[1]}\n"
        f"8107EC26 {get_colour[2]}00\n"
        f"8107EC28 {get_colour[0]}{get_colour[1]}\n"
        f"8107EC2A {get_colour[2]}00\n"
        f"8107EC2C {get_colour[0]}{get_colour[1]}\n"
        f"8107EC2E {get_colour[2]}00"
    )

    return overalls_string

def generate_gloves_colour(get_colour):
    gloves_string = (
        f"8107EC50 {get_colour[0]}{get_colour[1]}\n"
        f"8107EC52 {get_colour[2]}00\n"
        f"8107EC54 {get_colour[0]}{get_colour[1]}\n"
        f"8107EC56 {get_colour[2]}00\n"
        f"8107EC58 {get_colour[0]}{get_colour[1]}\n"
        f"8107EC5A {get_colour[2]}00\n"
        f"8107EC5C {get_colour[0]}{get_colour[1]}\n"
        f"8107EC5E {get_colour[2]}00"
    )

    return gloves_string

def generate_shoes_colour(get_colour):
    shoes_string = (
        f"8107EC68 {get_colour[0]}{get_colour[1]}\n"
        f"8107EC6A {get_colour[2]}00\n"
        f"8107EC6C {get_colour[0]}{get_colour[1]}\n"
        f"8107EC6E {get_colour[2]}00\n"
        f"8107EC70 {get_colour[0]}{get_colour[1]}\n"
        f"8107EC72 {get_colour[2]}00\n"
        f"8107EC74 {get_colour[0]}{get_colour[1]}\n"
        f"8107EC76 {get_colour[2]}00"
    )

    return shoes_string

def generate_face_colour(get_colour):
    face_string = (
        f"8107EC80 {get_colour[0]}{get_colour[1]}\n"
        f"8107EC82 {get_colour[2]}00\n"
        f"8107EC84 {get_colour[0]}{get_colour[1]}\n"
        f"8107EC86 {get_colour[2]}00\n"
        f"8107EC88 {get_colour[0]}{get_colour[1]}\n"
        f"8107EC8A {get_colour[2]}00\n"
        f"8107EC8C {get_colour[0]}{get_colour[1]}\n"
        f"8107EC8E {get_colour[2]}00"
    )

    return face_string

def generate_hair_colour(get_colour):
    hair_string = (
        f"8107EC98 {get_colour[0]}{get_colour[1]}\n"
        f"8107EC9A {get_colour[2]}00\n"
        f"8107EC9C {get_colour[0]}{get_colour[1]}\n"
        f"8107EC9E {get_colour[2]}00\n"
        f"8107ECA0 {get_colour[0]}{get_colour[1]}\n"
        f"8107ECA2 {get_colour[2]}00\n"
        f"8107ECA4 {get_colour[0]}{get_colour[1]}\n"
        f"8107ECA6 {get_colour[2]}00"
    )

    return hair_string

@app.route('/generate', methods=['POST'])
def generate():
    data = request.json
    hex_colors = data.get('hexColors', {})
    print(f"Received hex colors: {hex_colors}")

    codes = ""

    if 'hat' in hex_colors:
        hat_color = get_colour(hex_colors['hat'])
        codes += generate_hat_colour(hat_color) + "\n"

    if 'overalls' in hex_colors:
        overalls_color = get_colour(hex_colors['overalls'])
        codes += generate_overalls_colour(overalls_color) + "\n"

    if 'gloves' in hex_colors:
        gloves_color = get_colour(hex_colors['gloves'])
        codes += generate_gloves_colour(gloves_color) + "\n"

    if 'shoes' in hex_colors:
        shoes_color = get_colour(hex_colors['shoes'])
        codes += generate_shoes_colour(shoes_color) + "\n"

    if 'face' in hex_colors:
        skin_color = get_colour(hex_colors['face'])
        codes += generate_face_colour(skin_color) + "\n"

    if 'hair' in hex_colors:
        hair_color = get_colour(hex_colors['hair'])
        codes += generate_hair_colour(hair_color) + "\n"

    return jsonify({"code": codes.strip()})

if __name__ == '__main__':
    app.run(debug=True)