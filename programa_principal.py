# Chama as funções colaborativas e roda elas em sequência
import time
from programa1 import function1
from programa2 import function2
from programa3 import function3
from programa4 import function4

texto  = function1()
texto2 = function2(texto)
texto3 = function3(texto2)
texto4 = function4(texto3)

for paragrafo in texto4:
  print(paragrafo)
  time.sleep(5)
  
print('É ISSO. FIM')
