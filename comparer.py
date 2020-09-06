import sys
---------------
if lineArray[0].find('accept') > 0:
                                print("Accepted traffic")
                                cleanDir = open('results/clean_'+time_log+'.clean', 'w')
                                cleanDir.write(lineArray[0]) # only URI + timestamp
                                cleanDir.close