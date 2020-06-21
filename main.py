from lifxlan import LifxLAN, Light
from flask import Flask, jsonify, request, abort, render_template
import jsonschema
from lights_helper import light_to_dict

app = Flask(__name__,
    static_url_path='/static',
    static_folder='static'
)

lifx = LifxLAN()

# Cache all lights at start up
# TODO: Refresh this cache every few minutes
all_lights = lifx.get_lights()

@app.route('/lights')
def get_lights():
    # Convert lights list to friendlier objects
    lights = list(map(light_to_dict, all_lights))

    return jsonify(lights)

@app.route('/lights/<mac_addr>', methods=['POST'])
def change_light(mac_addr):
    filtered = list(filter(lambda light: light.get_mac_addr() == mac_addr, all_lights))

    # No light found with given MAC address - 404
    if len(filtered) is 0:
        return jsonify({
            'message': 'Device not found.'
        }), 404

    # Get light with given MAC address
    light = filtered[0]

    # Find out what we need to change
    body = request.json

    # Define schema for update
    schema = {
        'type': 'object',
        'properties': {
            'power': { 'type': 'boolean' }
        }
    }

    # Ensure schema is valid
    try:
        jsonschema.validate(request.json, schema)
    except Exception as err:
        return jsonify({
            'message': 'Invalid request body'
        }), 400

    # Handle power change
    if 'power' in request.json:
        light.set_power(request.json['power'])

    return light_to_dict(light)

@app.route('/')
def root():
    return render_template('index.html')
