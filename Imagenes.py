import binascii

class Imagen():
    def __init__(self,imagePath):
        self.direccionImagen = imagePath

    def aBinaria(self):
        with open (self.direccionImagen,"rb") as file:
            self.codigoImagenBinaria = file.read()
        return self.codigoImagenBinaria
    
    def aHexaDecimal(self):
        self.aBinaria()
        self.codigoImagenHexadecimal = binascii.hexlify(self.codigoImagenBinaria)
        return self.codigoImagenHexadecimal

    def aHexaDecimalStr(self):
        self.aHexaDecimal()
        self.codigoImagenHexadecimalStr = str(self.codigoImagenHexadecimal)
        self.codigoImagenHexadecimalStr = self.codigoImagenHexadecimalStr[2:len(self.codigoImagenHexadecimalStr)-1]
        return self.codigoImagenHexadecimalStr

class ImagenHexaDecimalStr():
    def __init__(self,codigoHexaDecimalStr):
        self.codigoHexaDecimalStr = codigoHexaDecimalStr
    
    def aBinaria(self):
        self.codigoImagenBinaria = binascii.unhexlify(self.codigoHexaDecimalStr)
        return self.codigoImagenBinaria

    def aImagen(self,direccionAGuardarImagen):
        self.aBinaria()
        with open(direccionAGuardarImagen,"wb") as file:
            file.write(self.codigoImagenBinaria)
            file.close()

from io import open
imagenVia = Imagen("RecursosGraficos\\Calle.png")
imagenViaBin = imagenVia.aHexaDecimalStr()
archivo = open("archivotexto.txt","w")
archivo.write(imagenViaBin)
archivo.close()
