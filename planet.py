import ephem
import datetime

def planet(args):
	print('User call /planet command for {}'.format(args))
	# if args == "Mars":
	#  	print (ephem.constellation(ephem.Mars(datetime.datetime.now().strftime('%Y/%m/%d'))))
# 	# elif args[0] == "Venus":
# 	# 	response = (ephem.constellation(ephem.Venus(datetime.datetime.now().strftime('%Y/%m/%d'))))
# 	# elif args[0] == "Moon":
# 	# 	response = (ephem.constellation(ephem.Moon(datetime.datetime.now().strftime('%Y/%m/%d'))))
# 	# else:
# 	# 	response = "Can't find this planet. Use Mars, Venus or Moon"		
# 	# update.message.reply_text(response)
	
	method_to_call = getattr(ephem, args)
	return ephem.constellation(method_to_call(datetime.datetime.now().strftime('%Y/%m/%d')))

def main():
	# print('HEllo!')
	print(planet('Mars'))

if __name__ == '__main__':
	main()