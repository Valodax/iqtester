#
# iqtester.py - Determines your iq rank based on a global population of 7.7 billion.
#

import numpy
import scipy.stats
import time

iq = int(input('Type in your IQ here: '))
globalpop = 7700000000
prob = scipy.stats.norm(100, 15).cdf(iq)
rank = round((prob*globalpop), 0)
percentile = (rank/globalpop)*100
smarter = globalpop-rank

print("Assuming there is a global population of 7,700,000,000...")
time.sleep(1.5)
print('\n')
print("Based on your IQ, you are ranked number " + "{:,}".format(int(rank)) + "!")
print('\n')
print("This means there are " + "{:,}".format(int(smarter)) + " people smarter than you and ")
print("you are in the top " + str(round(percentile,2)) + "% of all people.")
