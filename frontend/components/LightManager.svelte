<script>
    import Light from './Light.svelte';
    import LightService from '../services/LightService.js';

    let lights = [];

    /**
     * Refreshes the list of lights
     */
    function refreshLights() {
        // Fetch all lights
        LightService.get().then(data => {
            lights = data;
        });
    }

    /**
     * Handles cases where a light has been updated.
     */
    function handleLightUpdated() {
        refreshLights();
    }

    refreshLights();
</script>

<style>
    .lights {
        display: flex;
    }
</style>

<h2>Lights</h2>

<div class="lights">
    {#each lights as light}
        <Light {...light} on:lightUpdated={handleLightUpdated} />
    {/each}
</div>
