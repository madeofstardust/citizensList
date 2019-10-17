
#class LongString, taking care of making lists etc

class LongString:
	def makingTheProperString(self, *argv):
		thisIs = ""
		for arg in argv:
			thisIs += str(arg)
			thisIs += " "
		return thisIs