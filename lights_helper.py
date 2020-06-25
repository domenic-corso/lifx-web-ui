from lifxlan import Light
from colorsys import hsv_to_rgb

def light_to_dict(light: Light) -> dict:
    result = {
        'name': light.get_label(),
        'power': bool(light.get_power()),
        'supportsColor': light.supports_color(),
        'macAddress': light.get_mac_addr()
    }

    if light.supports_color():
        result['color'] = get_light_color(light)

    return result

def get_light_color(light: Light) -> dict:
    color = light.get_color()
    
    # Grab HSBK values
    hsbk_dict = {
        'hue': round((color[0] / 65535) * 100),
        'saturation': round((color[1] / 65535) * 100),
        'brightness': round((color[2] / 65535) * 100),
        'kelvin': round(((color[3] - 2500) / 6500) * 100)
    }

    # Convert LIFX HSBK to RGB
    rgb_tuple = hsv_to_rgb(hsbk_dict['hue'] / 100, hsbk_dict['brightness'] / 100, hsbk_dict['saturation'] / 100)

    return {
        'hsbk': hsbk_dict,
        'rgb': {
            'red': round(rgb_tuple[0] * 255),
            'green': round(rgb_tuple[1] * 255),
            'blue': round(rgb_tuple[2] * 255),
        }
    }
