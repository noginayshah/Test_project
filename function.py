#def check_number():
 #   for n in range(2, 10):
  #      for x in range(2, n):
   #         if n % x == 0:
    #            print(n, x)
     #           break
      #  else:
       #     print(n, 'is a problem')

#check_number()



import math

def get_sin(and_deg):

    and_mad = math.radians(and_deg)
    result = math.sin(and_mad)
    return round(result, 3)

for ang in [30, 45, 90, 180]:
    print(get_sin(ang))



