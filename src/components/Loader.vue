<template>
	<div class="loader__wrapper" v-if="loading">
		<div class="loader">
			<div></div>
			<div></div>
			<div></div>
			<div></div>
			<div></div>
			<div></div>
			<div></div>
			<div></div>
		</div>
    <span v-if="systemLabel" class="loader__info">
      Trwa przetwarzanie aktualizacji.<br>
      Nie wyłączaj lustra.
    </span>
	</div>
</template>

<script>
	export default {
		name: 'Loader',
		data: function () {
			return {
				loading: true,
				systemLabel: false,
			}
		},
		mounted() {
			this.$root.$on('loading', this.handleLoader);
			this.$root.$on('systemUpdate', this.systemUpdate);
		},
		methods: {
			handleLoader(bool) {
				this.loading = bool;
			},
      systemUpdate(bool) {
        this.loading = bool;
        this.systemLabel = bool;
      }
		},
	}
</script>

<style lang="less">
	.loader {
		display: inline-block;
		position: relative;
		width: 80px;
		height: 80px;

		&__wrapper {
			position: fixed;
			top: 50%;
			left: 50%;
			transform: translate(-50%, -50%);
			background: black;
			width: 100%;
			height: 100%;
			display: flex;
			justify-content: center;
			align-items: center;
      flex-direction: column;
		}

    &__info {
      font-size: 26px;
      display: block;
      margin-top: 35px;
      text-align: center;
    }

		@keyframes lds-roller {
			0% {
				transform: rotate(0deg);
			}
			100% {
				transform: rotate(360deg);
			}
		}

		div {
			animation: lds-roller 1.2s cubic-bezier(0.5, 0, 0.5, 1) infinite;
			transform-origin: 40px 40px;

			&:after {
				content: " ";
				display: block;
				position: absolute;
				width: 7px;
				height: 7px;
				border-radius: 50%;
				background: #fff;
				margin: -4px 0 0 -4px;
			}

			&:nth-child(1) {
				animation-delay: -0.036s;

				&:after {
					top: 63px;
					left: 63px;
				}
			}

			&:nth-child(2) {
				animation-delay: -0.072s;

				&:after {
					top: 68px;
					left: 56px;
				}
			}

			&:nth-child(3) {
				animation-delay: -0.108s;

				&:after {
					top: 71px;
					left: 48px;
				}
			}

			&:nth-child(4) {
				animation-delay: -0.144s;

				&:after {
					top: 72px;
					left: 40px;
				}
			}

			&:nth-child(5) {
				animation-delay: -0.18s;

				&:after {
					top: 71px;
					left: 32px;
				}
			}

			&:nth-child(6) {
				animation-delay: -0.216s;

				&:after {
					top: 68px;
					left: 24px;
				}
			}

			&:nth-child(7) {
				animation-delay: -0.252s;

				&:after {
					top: 63px;
					left: 17px;
				}
			}

			&:nth-child(8) {
				animation-delay: -0.288s;

				&:after {
					top: 56px;
					left: 12px;
				}
			}
		}
	}
</style>
