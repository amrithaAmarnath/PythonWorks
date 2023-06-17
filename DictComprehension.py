"""Dictionary comprehension"""

def dollar_to_rupee():
# create a dictionary
   price= {'Laptop':10,'mobile':5,'watch':3,'keyboard':1}
   """ multiply the price and convert_to_rupee
   convert_to_rupee= one dollar convert to Indian rupee
   """
   convert_to_rupee = 81.38
   n_price={i:j*convert_to_rupee for i,j in price.items()}
   return n_price
rc=dollar_to_rupee()
print(rc)