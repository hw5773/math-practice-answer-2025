from truth_table import truth_table
import time
import sys

expression = sys.argv[1]
start = time.time()
table = truth_table(expression)
end = time.time()
elapsed_time = end - start
print ("Elapsed Time: {} s".format(elapsed_time))
