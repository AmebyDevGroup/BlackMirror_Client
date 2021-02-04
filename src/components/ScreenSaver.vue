<template>
	<div class="screen-saver" :class="{'active': show}"></div>
</template>

<script>
	export default {
		name: 'ScreenSaver',
		data: function () {
			return {
				show: false,
        forceHide: false,
				counter: 20,
				timer: null,
			}
		},
		mounted() {
			this.$root.$on('showScreenSaver', this.showScreenSaver);
		},
		methods: {
      showScreenSaver(show) {
        this.show = show
      },
		},
	}
</script>

<style lang="less">
	.screen-saver {
		position: fixed;
		top: 0;
		right: 0;
		left: 0;
		bottom: 0;
		z-index: 100;
		background: black;
		width: 100vw;
		height: 100vh;
		opacity: 0;
		visibility: hidden;
		transition: 1s ease all;

		&.active {
			opacity: 1;
			visibility: visible;
		}
	}
</style>
