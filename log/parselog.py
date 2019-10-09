# See all types
# View histgram
# Get a log
import re
class Errors():
	def __init__ (self,type,exception,message,rows):
		self.type=type
		self.exception=exception
		self.message=message
		self.rows=rows
		
ls_errors=[]
		
f = open("server.log",encoding="utf-8")
in_current=0
in_total=0
for l in f.readlines():
    #if (l.__contains__("WARN") or l.__contains__("ERROR")) and (not l.__contains__("Authentication") and not l.__contains__("XA")):
	if isFirstLine(l):
		in_current=0
		# get type, Exception, msg
		# ls_errors.append(Errors(type,exception,message,rows))
    else:
		in_current+=1
	in_total+=1

		


# "2019-07-19T14:55:11+0800 WARN  [com.lombardrisk.batch.reader.CsvFileReader] (Batch Thread - 9)
# Exception occurred when CsvFileReader read record:This value .00 is not a number:
# java.lang.IllegalArgumentException:
# This value .00 is not a number"


def isFirstLine(line):
	pattern = re.compile(r'20\d\d-\d\d-\d\d \d\d:\d\d:\d\d,\d\d\d')
	match = pattern.match(line)
	if match:
		return True #match.group()
	return False #"not match"
	
#print(isFirstLine("2019-09-19 11:05:01,972 INFO  [com.lombardrisk.ocelot.expression.core.engine.StandardScriptEngine] (default task-75) failed to parse comment expression E_9170_M_SUBT2122_BS-A6 should not be negative.: com.lombardrisk.ocelot.expression.exception.ExpressionParseException: Expression parse error"))