import './css/main.scss';
import LightManager from './components/LightManager.svelte'

const app = new LightManager({
    target: document.querySelector("#app")
});
