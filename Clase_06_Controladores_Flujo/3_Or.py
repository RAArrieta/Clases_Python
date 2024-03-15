# OR MIENTRAS AL MENOS UNA SEA TRUE ES TRUE, FALSE ES SOLO CUANDO SON FALSE

a = 200
b = 180
c = 100

if a > b or b < c:
    print("al menos uno es true")
    
if a < b or b < c:
    print("Al menos uno es true")
else:
    print("Ambos son False")