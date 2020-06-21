from lifxlan import Light

def light_to_dict(light: Light):
    return {
        'name': light.get_label(),
        'power': bool(light.get_power()),
        'color': light.get_color(),
        'macAddress': light.get_mac_addr()
    }
