#This code is for python 3.
import time, random
from threading import Lock, Event, Thread


mutex = Lock()

#Interval in seconds
haircutDurationMin = 5 #minimum time for a customers haircut
haircutDurationMax = 25 #maximum time for a customers haircut
CustIntMin = 3 #minimum interval of new customers going into the shop
CustIntMax = 10 #maximum interval between of new customers going into


class BarberShop:
	waitingCustomers = [] 

	def __init__(self, barber, Seats):
		self.barber = barber
		self.Seats = Seats
		print ('1 barber will be working today.')
		print ('Barber Shop is initilized with {} customer chairs'.format(Seats))
		print ('The intervals at which customers eneter the shop is between {} and {}'.format(CustIntMin,CustIntMax))
		print('The maximum length of a haircut is {}, while the minimum is {}'.format(haircutDurationMin,haircutDurationMax))
		print ('******************************************')
		print('')
		print('WHEN BUSINESS GETS ROLLING')
		print('')
		print('******************************************')

	def BarbersOpens(self):
		print ('Barbershop opens')
		Thread1 = Thread(target = self.barberStartsWork)
		Thread1.start()
		
	
	def barberStartsWork(self):
		while True:
			mutex.acquire() #changes state to locked

			if len(self.waitingCustomers) > 0:
				c = self.waitingCustomers[0]
				del self.waitingCustomers[0]
				mutex.release() #changes state to unlocked
				self.barber.cut(c)
			else:
				mutex.release() #unlocked
				print('barber goes asleep')
				barber.sleep()
				print ('Barber wakes up')
				

	def CustomerEnters(self, customer):
		mutex.acquire() #locked
		print ('{} entered the barbers'.format(customer.name))

		if len(self.waitingCustomers) == self.Seats:
			print ('Theres no room in the waiting area, {} is leaving.'.format(customer.name))
			mutex.release() #unlocked
		else:
			print ('{} sat down in the waiting room'.format(customer.name))	
			self.waitingCustomers.append(c)	
			mutex.release() #unlcoked
			barber.Awaken()

class Customer:
	def __init__(self, name):
		self.name = name

class Barber:
	barberWorkingEvent = Event()

	def sleep(self):
		self.barberWorkingEvent.wait() #blocks barberWorking Event until set to true with 'set()'

	def Awaken(self):
		self.barberWorkingEvent.set() #set to true and therefore barber is working

	def cut(self, customer):
		self.barberWorkingEvent.clear() #Event is set to false
		print ('{} is getting their haircut'.format(customer.name))

		TrimTime = random.randrange(haircutDurationMin, haircutDurationMax+1)
		time.sleep(TrimTime)
		print ('{} is finished getting there haircut'.format(customer.name))


if __name__ == '__main__':
	haircutees = []
	haircutees.append(Customer('Conor'))
	haircutees.append(Customer('Sam'))
	haircutees.append(Customer('Charlie'))
	haircutees.append(Customer('Liam'))
	haircutees.append(Customer('Keith'))
	haircutees.append(Customer('Mark'))
	haircutees.append(Customer('Al'))
	haircutees.append(Customer('Jon'))
	haircutees.append(Customer('Cian'))
	haircutees.append(Customer('Stephen'))
	haircutees.append(Customer('Richard'))
	haircutees.append(Customer('Peter'))
	haircutees.append(Customer('Cian'))
	haircutees.append(Customer('Jake'))
	haircutees.append(Customer('Tom'))
	haircutees.append(Customer('Shane'))
	haircutees.append(Customer('Kevin'))

	barber = Barber()

	barberShop = BarberShop(barber, Seats= 10)
	barberShop.BarbersOpens()

	for i in haircutees:
		c = haircutees.pop()	
		
		barberShop.CustomerEnters(c)
		Interval = random.randrange(CustIntMin,CustIntMax)
		time.sleep(Interval)