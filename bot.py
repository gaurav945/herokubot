from apscheduler.scheduler import Scheduler
from pushbullet import Pushbullet
from datetime import datetime

api_key = 'o.w5uPpJMz2LRHFovuRrbfDDacJu5DfdLf'
pb = Pushbullet(api_key)
device = pb.devices[2]

def tick():
	text = 'Tick! : %s' % datetime.now()
	device.push_note('this is the time now', text)
	print text


if __name__ == '__main__':
	scheduler = Scheduler(standalone=True)
	scheduler.add_interval_job(tick, seconds=3600)
	# print('Press Ctrl+C to exit')
	try:
		scheduler.start()
	except (KeyboardInterrupt, SystemExit):
		pass