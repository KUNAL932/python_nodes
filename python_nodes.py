Python 3.5.2 (default, Nov 12 2018, 13:43:14) 
[GCC 5.4.0 20160609] on linux
Type "copyright", "credits" or "license()" for more information.
>>> 
#class is created
>>> class Daynames:
	def __init__(self,dataval=None):
		self.dataval=dataval
		self.nextval=None

		
>>> e1=Daynames'monday'
SyntaxError: invalid syntax
>>> e1=Daynames('monday')
>>> e2=Daynames('tuesday')
>>> e3=Daynames('wednesday')
>>> e4=Daynames('thursday')
>>> 
>>> e1.nextval=e3
>>> e3.nextval=e2
>>> e2.nextval=e4
>>>
>>> thisvalue=e1
>>> 
>>> while thisvalue:
	print(thisvalue.dataval)
	thisvalue=thisvalue.nextval

	
monday
tuesday
wednesday
thursday
>>> 
