from functools import reduce

class App:

    def __inputNumeros(self):
        self.__listaNumeros = input('Introduzca una lista de numeros enteros separados por espacios:\n')
        # limpia de caracteres invalidos la cadena
        tmp = ''
        for n in self.__listaNumeros:
            if n in '0123456789 ':
                tmp += n
        # separa cada numero y convierte cada uno de str a int
        self.__listaNumeros = [int(n) for n in tmp.split()]

    def __sumarImpares(self):
        numerosImpares = filter(lambda x: x % 2 == 1, self.__listaNumeros)
        # reduce no puede recibir un iterable vacio, asi que evitamos el error
        # NOTA IMPORTANTE: usar if para verificar la variable numerosImpares
        # obliga a hacer una conversión a list, agotando el generador
        # y produciendo un error lógico. Solucion: usar la excepcion
        try:
            self.__totalSuma = reduce(lambda x, y: x + y, numerosImpares)
        except TypeError:
            self.__totalSuma = 0
    
    def run(self):
        self.__inputNumeros()
        self.__sumarImpares()
        print('***')
        print(f'La suma de todos los numeros impares introducidos es: {self.__totalSuma}')
        print('***')


if __name__ == '__main__':
    app = App()
    app.run()