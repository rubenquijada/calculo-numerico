#!/usr/bin/env python3

import numpy as np 

def Valor_intermedio(f,a,b):
	return f(a)*f(b)<0


if __name__ == '__main__':
	f= lambda x :x**2-4
	a=0
	b=5
	x=np.arange(f,a,x)
	pr
	print(Valor_intermedio(f,a,x))
	print(x)
	
	
#!/usr/bin/env python3

import numpy as np 

def Valor_intermedio(f,a,b):
	return f(a)*f(b)<0


if __name__ == '__main__':
	f= lambda x :x**2-4
	a=0
	b=5
  
for x in range (5):
  y = Valor_intermedio(f,a,x)
  """print(y)
  print(x,f(x),y)"""
  if y=="true":
    break
print(a,x)
print(f(a),f(x))
