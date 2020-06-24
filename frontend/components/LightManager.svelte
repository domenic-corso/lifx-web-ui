<script>
    import Light from './Light.svelte';
    import LightService from '../services/LightService.js';

    let lights = [];
    let refreshingLights = true;

    /**
     * Refreshes the list of lights
     */
    function refreshLights() {
        refreshingLights = true;

        // Fetch all lights
        LightService.get().then(data => {
            lights = data;
        }).finally(() => {
            refreshingLights = false;
        });
    }

    refreshLights();
</script>

<style>
    .lights__container {
        display: flex;
        padding-top: 32px;
    }
</style>

<div class="panel">
    <header class="panel__header">
        <h2 class="panel__title">Lights</h2>
        <div class="panel__options">
            <button class="optbutton" class:optbutton--spinning="{refreshingLights}" type="button" on:click={refreshLights}>
                <i class="material-icons">refresh</i>
            </button>
        </div>
    </header>
    <div class="panel__content lights__container">
        {#each lights as light}
            <Light {...light} on:lightUpdated={refreshLights} />
        {/each}
    </div>
</div>
