export default class LightService {
    /**
     * @typedef {Object} Light
     * @property {string} macAddress - The MAC address of the light
     * @property {string} name - The name of the light
     * @property {boolean} power - Indicates if the light is currently on
     */
    /**
     * Gets all lights.
     * 
     * @returns {Promise<Light[]>}
     */
    static async get() {
        const response = await fetch('/lights');
        
        return await response.json();
    }

    /**
     * Updates the state of a given light.
     * 
     * @param {string} macAddress The MAC address identifying the light to updat
     * @param {boolean} power If given, the light's power will be updated to reflect
     * @returns {Promise<Light>}
     */
    static async update(macAddress, power) {
        const body = {};

        if (power !== undefined) {
            body.power = power
        }

        const response = await fetch(`/lights/${ encodeURIComponent(macAddress) }`, {
            method: 'post',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(body)
        });

        return await response.json();
    }
}
