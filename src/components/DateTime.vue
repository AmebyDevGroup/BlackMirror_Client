<template>
	<transition name="fade" v-if="show">
		<div class="time" v-if="!prerender">
			<div class="time__wrapper">
				<span class="time__item" v-if="dateTime !== null">{{ dateTime }}</span>
				<span class="time__item time__item--british" v-if="isBritishTime">{{ cuttedTime }}</span>
			</div>
			<div class="time__date">{{ date }}</div>
		</div>
	</transition>
</template>

<script>
const moment = require('moment-timezone');

export default {
		name: 'DateTime',
		data: function () {
			return {
			  show: false,
			  dateTime: null,
				date: null,
				weekday: null,
				prerender: true,
        format: 'HH:mm',
        timezone: 'Europe/Warsaw',
        isBritishTime: false,
        cuttedTime: '',
			}
		},
		mounted() {
			this.handleTimer();
			this.$root.$on('loading', this.handlePrerender);
			this.$root.$on('timeChange', this.getTimeData);
      this.$root.$on('configChange', this.handleConfig);
		},
		methods: {
			handlePrerender(bool) {
				this.prerender = bool;
			},
      handleConfig(event) {
        this.show = event.time;
      },
      getTimeData(data) {
			  this.format = data.time_format;
			  this.timezone = data.timezone;
			  this.isBritishTime = data.isBritishTime;
      },
			handleTimer() {
				setInterval(() => {
				  const now = new Date();
				  this.dateTime = moment().tz(`${this.timezone}`).format(`${this.format}`);
          if (this.isBritishTime) {
				    this.cuttedTime = this.dateTime.substr(-3);
				    this.dateTime = this.dateTime.slice(0, -3);
          }
					this.date = now.toLocaleString('PL-pl', {weekday: 'long', month: 'long', day: 'numeric'});
				}, 1000);
			}
		},
		computed: {
			hours() {
				return this.hoursValue < 10 ? `0${this.hoursValue}` : this.hoursValue;
			},
			minutes() {
				return this.minutesValue < 10 ? `0${this.minutesValue}` : this.minutesValue;
			},
		}
	}
</script>

<style lang="less">
	.time {
		&__item {
			font-weight: 700;
			font-size: 130px;
			line-height: 1;
			letter-spacing: 2px;

      &--british {
        position: absolute;
        font-size: 60px;
        right: -115px;
        top: 10px;
      }
		}

		&__wrapper {
			display: flex;
      position: relative;
		}

		&__date {
			text-transform: capitalize;
			font-size: 34px;
		}
	}
</style>


