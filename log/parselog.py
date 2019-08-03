f = open("server.log",encoding="utf-8")
i=0
for l in f.readlines():
    #if (l.__contains__("WARN") or l.__contains__("ERROR")) and (not l.__contains__("Authentication") and not l.__contains__("XA")):
    if (l.__contains__("CsvFileReader") and l.__contains__("WARN")) or i>0:
        i=i+1
        if i>20:
            i=0
            break
        print(l)

# "2019-07-19T14:55:11+0800 WARN  [com.lombardrisk.batch.reader.CsvFileReader] (Batch Thread - 9)
# Exception occurred when CsvFileReader read record:This value .00 is not a number:
# java.lang.IllegalArgumentException:
# This value .00 is not a number"
