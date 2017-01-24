from apscheduler.scheduler import Scheduler
from pushbullet import Pushbullet
from pyquery import PyQuery as pq
import requests
# import ipdb

api_key = 'o.w5uPpJMz2LRHFovuRrbfDDacJu5DfdLf'
pb = Pushbullet(api_key)
device = pb.devices[2]

def tick():
	url = 'https://www.1337x.to/home/'
	r = requests.get(url)
	print 'Requested the site...'
	d = pq(r.text)
	for i in d('.featured-list'):
		# import ipdb; ipdb.set_trace()
		text = i.getchildren()[0].text_content().strip().lower()
		# print text
		if text == 'popular other torrents popular this week trending this week':
			# import ipdb; ipdb.set_trace()
			# print i.text_content() # we have the needed i now.
			data = i.find('div').find('table').find('tbody').getchildren()
			torrents = []
			for k in data:
				# print k.text_content().split('\n')[1]
				name = k.text_content().split('\n')[1]
				torrents.append(name)
			# import ipdb; ipdb.set_trace()
			temp = ''
			for j in torrents:
				temp = temp + j + '\n\n\n\n'
			device.push_note('Books & Related Torrents', temp)


if __name__ == '__main__':
	scheduler = Scheduler(standalone=True)
	scheduler.add_interval_job(tick, seconds=21600)
	# print('Press Ctrl+C to exit')
	try:
		scheduler.start()
	except (KeyboardInterrupt, SystemExit):
		pass