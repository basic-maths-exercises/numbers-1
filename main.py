import numpy as np

def numberOfThousands( N ) :
  # Your code goes here
  return np.floor( N / 1000 )

# This calls the function you have written to check if it works
print( numberOfThousands(3260) )
