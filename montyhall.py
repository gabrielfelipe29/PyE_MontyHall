import random


def monty_hall(estrategia, imprimir):
    # Si estrategia es True, entonces el participante cambia de puerta. Si es false, no cambia de puerta
    # Si imprimir es True, se muestran los resultados. Si es False, no se muestran los resultados.
    # Retorna true si el participante elige la puerta correcta, false si pierde
    
    es_ganador=False
    puerta_participante=random.randint(1,3)
    puerta_auto=random.randint(1,3)    
    puerta_presentador=random.randint(1,3)
    
    # Controla que la puerta del presentador no sea la puerta ganadora y tampoco la puerta del participante
    while (puerta_presentador==puerta_participante or puerta_presentador==puerta_auto):
            puerta_presentador=random.randint(1,3)
    
    
    if estrategia is True:
        # participante elige cambiar de puerta
        # Controla que la nueva puerta no sea la misma que la anterior
        puerta_nueva_participante=random.randint(1,3)
        while (puerta_nueva_participante==puerta_participante):
            puerta_nueva_participante=random.randint(1,3)
        
        if puerta_auto == puerta_nueva_participante:
            es_ganador=True
            
        if imprimir:
            print(f"Puerta elegida por el participante: {puerta_participante}\nPuerta donde esta el auto: {puerta_auto}\nPuerta abierta por el presentador: {puerta_presentador}\nNueva puerta elegida por el participante: {puerta_nueva_participante}\nResultado: {es_ganador}")        
    else:
        # participante sigue con la misma puerta
        if puerta_auto == puerta_participante:
            es_ganador=True
        
        if imprimir:
            print(f"Puerta elegida por el participante: {puerta_participante}\nPuerta donde esta el auto: {puerta_auto}\nPuerta abierta por el presentador: {puerta_presentador}\nResultado: {es_ganador}")        
    
    return es_ganador
    
def correr_monty(cantidad_veces, estrategia, imprimir):
    veces_ganadas=0
    for i in range(0,cantidad_veces):
        resultado=monty_hall(estrategia,imprimir)
        if resultado is True:
            veces_ganadas+=1
    return veces_ganadas

#Parte 2 - Ejecutar 1000, 10000 y 100000 veces

# Ejecutar 1000 veces    
print(f"De las 1.000 veces que el participante no cambio de puerta, gano: {correr_monty(1000,False,False)}" )
print(f"De las 1.000 veces que el participante cambio de puerta, gano: {correr_monty(1000,True,False)}" )


# Ejecutar 10000 veces    
print(f"De las 10.000 veces que el participante no cambio de puerta, gano: {correr_monty(10000,False,False)}" )
print(f"De las 10.000 veces que el participante cambio de puerta, gano: {correr_monty(10000,True,False)}" )
    
    
# Ejecutar 100000 veces    
print(f"De las 100.000 veces que el participante no cambio de puerta, gano: {correr_monty(100000,False,False)}" )
print(f"De las 100.000 veces que el participante cambio de puerta, gano: {correr_monty(100000,True,False)}" )

# Ejecutar 1.000.0000
#print(f"De las 1.000.000 veces que el participante no cambio de puerta, gano: {correr_monty(1000000,False,False)}" )
#print(f"De las 1.000.000 veces que el participante cambio de puerta, gano: {correr_monty(1000000,True,False)}" )