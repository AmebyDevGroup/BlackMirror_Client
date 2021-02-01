import Vue from 'vue'
import App from './App.vue'
import Echo from 'laravel-echo';
import * as SerialNumber from '../public/sn.json';

window.Pusher = require('pusher-js');
window.io = require('socket.io-client');

let eventCounter = 0;
let activeSections = 0;
let module_inactive = false;
let ENABLE_CAMERA = false;
let wasThere = false;
const SerialNum = SerialNumber.default.SN;

const handleLoading = (ev) => {
	const data = Object.values(ev.data);
	activeSections = [...data].filter(elem => elem === true).length;
	if (activeSections === 0) module_inactive = true;
};

console.log('serial', SerialNum);

const echo = new Echo({
	broadcaster: 'socket.io',
	key: "023a905bee315629c3157500199f5065",
	host: 'https://ws.myblackmirror.pl',
	auth: {
		headers: {
			'Authorization': `SN ${SerialNum}`,
		},
	},
});

setTimeout(() => {
	const isConnected = echo.connector.socket.connected;
	if (!isConnected) window.Vue.$root.$emit('connectionError', isConnected);
}, 5000)

echo.join(`mirror.${SerialNum}`)
	.listen('Message', (e) => {
		console.log(e);
		if (e.type === "config") {
			handleLoading(e);
			ENABLE_CAMERA = e.data.camera;
		}
		window.Vue.$root.$emit(`${e.type}Change`, e.data);
		eventCounter++;
		if (eventCounter === activeSections || module_inactive || wasThere) {
			if (eventCounter === activeSections) wasThere = true;

			setTimeout(() => {
				window.Vue.$root.$emit('loading', false);
				window.Vue.$root.$emit('connectionError', echo.connector.socket.connected);
				window.Vue.$root.$emit('hideSaver', echo.connector.socket.connected);

				if (ENABLE_CAMERA) {
					window.Vue.$root.$emit('forceSaverDisable', false);
					window.Vue.$root.$emit('screenSaver', true);
				} else {
					window.Vue.$root.$emit('forceSaverDisable', true);
				}
			}, 500)
		}
	});

Vue.config.productionTip = false;

window.Vue = new Vue({
	render: h => h(App),
}).$mount('#app');
