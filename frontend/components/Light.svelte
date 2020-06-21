<script>
    export let macAddress, name, power;

    import { createEventDispatcher } from 'svelte';
    import LightService from '../services/LightService.js';

    const dispatch = createEventDispatcher();

    function handlePowerClick() {
        power = !power;

        LightService.update(macAddress, power).then(() => {
            dispatch('lightUpdated');
        });
    }
</script>

<style>
    .light {
        border: 0.1rem solid #dddddd;
        border-radius: 0.3rem;
        display: flex;
        cursor: default;
    }

    .light__left,
    .light__right {
        padding: 1rem;
    }

    .light__right {
        display: flex;
        align-items: center;
        justify-content: center;
    }

    .light__name {
        font-weight: 500;
        margin-bottom: 0.5rem;
    }

    .light__mac {
        font-style: italic;
        font-size: 0.8rem;
        color: #999999;
    }

    .light__power {
        width: 3rem;
        height: 3rem;
        display: flex;
        align-items: center;
        justify-content: center;
        background: none;
        border-radius: 50%;
        outline: none;
        cursor: pointer;
        color: #dddddd;
        border: 0.1rem solid #dddddd;
        transition: all 0.1s;
    }

    .light__power--on {
        color: #00592e;
        border-color: #00592e;
        background: #f7fffb;
    }

    .light__power > i {
        font-size: 1.5rem;
        color: inherit;
    }
</style>

<div class="light">
    <div class="light__left">
        <div class="light__name">{name}</div>
        <div class="light__mac">{macAddress}</div>
    </div>
    <div class="light__right">
        <button type="button" class="light__power" class:light__power--on="{power}" on:click={handlePowerClick}>
            <i class="material-icons">power_settings_new</i>
        </button>
    </div>
</div>
