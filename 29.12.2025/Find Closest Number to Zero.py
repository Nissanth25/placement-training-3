class Solution(object):
    def findClosestNumber(self, nums):
        distancia_minima = 10e5
        valor_minimo = 10e5
        for elemento in nums:
            if abs(elemento) < distancia_minima:
                valor_minimo = elemento
                distancia_minima = abs(elemento)
            elif abs(elemento) == distancia_minima:
                if elemento > valor_minimo:
                    valor_minimo = elemento
        
        return valor_minimo

