class App:

    def __inputPaises(self):
        # permite eliminar cualquier caracter prohibido
        CARACTERES_PERMITIDOS = 'QWERTYUIOPASDFGHJKLÑZXCVBNMqwertyuiopasdfghjklñzxcvbnm, '
        self.__strPaises = input('Introduzca una lista de paises separados por comas (no se admiten vocales acentuadas):\n')
        # descarta caracteres prohibidos
        tmp = ''
        for c in self.__strPaises:
            if c in CARACTERES_PERMITIDOS:
                tmp += c

    def __sortPaises(self):
        # divide la cadena, elimina espacios marginales, capitaliza la letra
        # inicial de cada pais, elimina duplicados y vuelve a convertir en list
        self.__listPaises = list(set([
            pais.strip().capitalize() for pais in self.__strPaises.split(',')
            ]))
        # organiza en orden alfabetico
        self.__listPaises.sort()

    def __outputPaises(self):
        self.__strPaises = ''
        # vueve a unir la lista en una cadena bien formateada
        for pais in self.__listPaises:
            self.__strPaises += f'{pais}, '
        # elimina la coma y el espacio que quedan al final
        self.__strPaises = self.__strPaises[0:len(self.__strPaises)-2]
            
    def __printPaises(self):
        self.__outputPaises()
        print('***')
        print(self.__strPaises)
        print('***')

    def run(self):
        self.__inputPaises()
        self.__sortPaises()
        self.__printPaises()


if __name__ == '__main__':
    app = App()
    app.run()

# TODO: Si el pais tiene un nombre de varias palabras, capitalizarlas todas
#       Ej. republica dominicana -> Republica Dominicana

# TODO: Contemplar multiples espacios seguidos. Ej. costa   rica -> Costa Rica