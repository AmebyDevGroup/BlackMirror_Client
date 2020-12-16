import * as faceapi from 'face-api.js';

export default class CameraService {
	constructor(enableDetection = true) {
		window.enableDetection = enableDetection;
		this.handleFaceRecognition();
		if (!window.enableDetection) {
			if (window.video) {
				window.video.pause();
				window.video.src = "";
				window.video.srcObject.getTracks()[0].stop();
				window.video.removeEventListener('play', () => {})
				clearInterval(window.updateInterval);
				window.updateInterval = null;
			}
		}
	}

	startVideo() {
		if (navigator.getUserMedia && window.enableDetection) {
			navigator.getUserMedia({ video: true }, this.handleSrc, this.handleError);
		}
	}

	handleSrc(stream) {
		window.video = document.querySelector("#videoElement");
		window.video.srcObject = stream;

		window.video.addEventListener('play', () => {
			if (window.updateInterval == null) {
				window.updateInterval = setInterval(async () => {
					if (!window.enableDetection) {
						window.video.pause();
						window.video.src = "";
						window.video.srcObject.getTracks()[0].stop();
						window.video.removeEventListener('play', () => {})
						clearInterval(window.updateInterval);
						window.updateInterval = null;
					}

					const detections = await faceapi.detectAllFaces(window.video, new faceapi.TinyFaceDetectorOptions()).withFaceLandmarks().withFaceExpressions();

					if (detections.length === 0) {
						console.log('nie wykryto');
						window.Vue.$root.$emit('screenSaver', false);
						return;
					}

					if (detections[0].detection.score >= 0.75) {
						console.log('wykryto', detections[0].detection.score);
						window.Vue.$root.$emit('screenSaver', detections[0].detection.score);
					}
				}, 5000);
			}
		})
	}

	handleError(error) {
		console.log('error', error);
	}

	handleFaceRecognition() {
		Promise.all([
			faceapi.nets.tinyFaceDetector.loadFromUri('/models'),
			faceapi.nets.faceLandmark68Net.loadFromUri('/models'),
			faceapi.nets.faceRecognitionNet.loadFromUri('/models'),
			faceapi.nets.faceExpressionNet.loadFromUri('/models')
		]).then(() => {
			this.startVideo();
		});
	}
}
