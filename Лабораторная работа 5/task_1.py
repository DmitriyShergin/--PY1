from pprint import pprint

pprint([{'dec': i,
         'bin': bin(i),
         'oct': oct(i),
         'hex': hex(i)} for i in range(16)])
