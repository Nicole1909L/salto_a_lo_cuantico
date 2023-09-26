import numpy as np
def matriz_accion(m,v):
        if len(m[0]) == len(v):
            mat = np.array(m)
            vect = np.array(v)
            result = np.array(np.dot(mat,vect))
            return (result)
        else:
            return ("No cumple requerimientos") 
def sim_canicas(dinamica,estado_inicial,clicks):
    dinamica = np.array(dinamica)
    estado_inicial = np.array(estado_inicial)
    cont = 0
    estado_final = 0
    while cont < clicks:
          estado_final = matriz_accion(dinamica, estado_inicial)
          cont += 1
    return estado_final

