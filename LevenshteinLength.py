#Introducir las palabras, para las cuales se quiere medir su distancia de edicion.
#Como word1 y word2 del llamado a la funcion "distancia"


def distancia(word1,word2):
  #se genera el diccionacio para la comparacion (una tabla)
  d = dict()

  #se asignan los valores de la primera palabra 'world1' (1er.columna)
  for i in range(len(word1)+1):
     d[i]=dict()
     d[i][0]=i

  #se asignan los valores de la segunda palabra 'world2' (1er.fila)
  for i in range(len(word2)+1):
     d[0][i] = i

  #se hace la comparación caracter por caracter
  for i in range(1, len(word1)+1):
     for j in range(1, len(word2)+1):
        d[i][j] = min(d[i][j-1]+1, d[i-1][j]+1, d[i-1][j-1]+(not word1[i-1] == word2[j-1]))

  #imprime el valor de la distancia minima de edicion
  print (d[len(word1)][len(word2)])


distancia('canino','felino')    
