
#using decode:
print(b'Easy \xE2\x9C\x85'.decode("utf-8"))

import codecs  
byteData = b'Lets eat a \xf0\x9f\x8d\x95!'  
codecs.decode(byteData, 'UTF-8')  

#Learn about this more..
#Learn eval() and exec()