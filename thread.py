from time import sleep
from threading import *
class Hi(Thread):
	def run(Self):
		for i in range(5):
			print('Great')
			sleep(1)
class Hello(Thread):
	def run(self):
		for i in range(5):
			print('Good')
			sleep(1)

class Greet(Thread):
	def run(self):
		for i in range(5):
			print('Nice')
			sleep(1)

a=Hi()
b=Hello()
c=Greet()
a.start()
sleep(0.2)
b.start()
sleep(0.2)
c.start()