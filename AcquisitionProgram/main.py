import cv2
from pylsl import StreamInlet, resolve_stream
import pandas as pd
import random

DatosBEO, DatosLCH, DatosRCH, DatosLDF, DatosLPF, DatosRDF, DatosRPF, DatosDescanso = [], [], [], [], [], [], [], []
BEO, LCH, RCH, LDF, LPF, RDF, RPF, Descanso = "1", "2", "3", "4", "5", "6", "7", "8"
beo, lch, rch, ldf, lpf, rdf, rpf, des = 1, 1, 1, 1, 1, 1, 1, 1
ide = 0


def mainlch():
    name = "S"+Subject+"R"+str(Run)+Tipo+LCH
    im = cv2.imread('D:../Imagenes/LCH.jpg')
    cv2.namedWindow('Image', cv2.WINDOW_NORMAL)
    cv2.setWindowProperty('Image', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    cv2.imshow("Image", im)
    cv2.waitKey(10)
    inlet = StreamInlet(streams[0])
    while True:
        sample, t = inlet.pull_sample()
        DatosLCH.append(sample)
        if len(DatosLCH) == 500:
            cv2.waitKey(1)
            df = pd.DataFrame(DatosLCH)
            df.to_csv("D:../Recoleccion/" + name + "_" +
                      str(lch) + '.csv')
            DatosLCH.clear()
            break


def mainrch():
    name = "S"+Subject+"R"+str(Run)+Tipo+RCH
    im = cv2.imread('D:../Imagenes/RCH.jpg')
    cv2.namedWindow('Image', cv2.WINDOW_NORMAL)
    cv2.setWindowProperty('Image', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    cv2.imshow("Image", im)
    cv2.waitKey(10)
    inlet = StreamInlet(streams[0])
    while True:
        sample, t = inlet.pull_sample()
        DatosRCH.append(sample)
        if len(DatosRCH) == 500:
            cv2.waitKey(1)
            df = pd.DataFrame(DatosRCH)
            df.to_csv("D:../Recoleccion/" + name+"_" +
                      str(rch) + '.csv')
            DatosRCH.clear()
            break


def mainldf():
    name = "S"+Subject+"R"+str(Run)+Tipo+LDF
    im = cv2.imread('D:../Imagenes/LDF.jpg')
    cv2.namedWindow('Image', cv2.WINDOW_NORMAL)
    cv2.setWindowProperty('Image', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    cv2.imshow("Image", im)
    cv2.waitKey(10)
    inlet = StreamInlet(streams[0])
    while True:
        sample, t = inlet.pull_sample()
        DatosLDF.append(sample)
        if len(DatosLDF) == 500:
            cv2.waitKey(1)
            df = pd.DataFrame(DatosLDF)
            df.to_csv("D:../Recoleccion/" + name+"_" +
                      str(ldf) + '.csv')
            DatosLDF.clear()
            break


def mainlpf():
    name = "S"+Subject+"R"+str(Run)+Tipo+LPF
    im = cv2.imread('D../Imagenes/LPF.jpg')
    cv2.namedWindow('Image', cv2.WINDOW_NORMAL)
    cv2.setWindowProperty('Image', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    cv2.imshow("Image", im)
    cv2.waitKey(10)
    inlet = StreamInlet(streams[0])
    while True:
        sample, t = inlet.pull_sample()
        DatosLPF.append(sample)
        if len(DatosLPF) == 500:
            cv2.waitKey(1)
            df = pd.DataFrame(DatosLPF)
            df.to_csv("D:../Recoleccion/" + name + "_" +
                      str(lpf) + '.csv')
            DatosLPF.clear()
            break


def mainrdf():
    name = "S"+Subject+"R"+str(Run)+Tipo+RDF
    im = cv2.imread('D../Imagenes/RDF.jpg')
    cv2.namedWindow('Image', cv2.WINDOW_NORMAL)
    cv2.setWindowProperty('Image', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    cv2.imshow("Image", im)
    cv2.waitKey(10)
    inlet = StreamInlet(streams[0])
    while True:
        sample, t = inlet.pull_sample()
        DatosRDF.append(sample)
        if len(DatosRDF) == 500:
            cv2.waitKey(1)
            df = pd.DataFrame(DatosRDF)
            df.to_csv("D../Recoleccion/" + name + "_" +
                      str(rdf) + '.csv')
            DatosRDF.clear()
            break


def mainrpf():
    name = "S"+Subject+"R"+str(Run)+Tipo+RPF
    im = cv2.imread('D:../Imagenes/RPF.jpg')
    cv2.namedWindow('Image', cv2.WINDOW_NORMAL)
    cv2.setWindowProperty('Image', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    cv2.imshow("Image", im)
    cv2.waitKey(10)
    inlet = StreamInlet(streams[0])
    while True:
        sample, t = inlet.pull_sample()
        DatosRPF.append(sample)
        if len(DatosRPF) == 500:
            cv2.waitKey(1)
            df = pd.DataFrame(DatosRPF)
            df.to_csv("D:../Recoleccion/" + name + "_" +
                      str(rpf) + '.csv')
            DatosRPF.clear()
            break


def mainbeo():
    name = "S"+Subject+"R"+str(Run)+Tipo+BEO
    im = cv2.imread('D:../Imagenes/Baseline.jpg')
    cv2.namedWindow('Image', cv2.WINDOW_NORMAL)
    cv2.setWindowProperty('Image', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    cv2.imshow("Image", im)
    cv2.waitKey(10)
    inlet = StreamInlet(streams[0])
    while True:
        sample, t = inlet.pull_sample()
        DatosBEO.append(sample)
        if len(DatosBEO) == 500:
            cv2.waitKey(1)
            df = pd.DataFrame(DatosBEO)
            df.to_csv("D:../Recoleccion/" + name + "_" +
                      str(beo) + '.csv')
            DatosBEO.clear()
            break


def descanso():
    name = "S"+Subject+"R"+str(Run)+Tipo+Descanso+"_"+ide
    img = cv2.imread('D:../Imagenes/Descanso.jpg')
    cv2.namedWindow('Image', cv2.WINDOW_NORMAL)
    cv2.setWindowProperty('Image', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    cv2.imshow('Image', img)
    cv2.waitKey(10)
    inlet = StreamInlet(streams[0])
    while True:
        sample, t = inlet.pull_sample()
        DatosDescanso.append(sample)
        if len(DatosDescanso) == 500:
            cv2.waitKey(1)
            df = pd.DataFrame(DatosDescanso)
            df.to_csv("D../Recoleccion/" + name + "_" +
                      str(des) + '.csv')
            DatosDescanso.clear()
            break


operaciones = {'1': mainlch, '2': mainrch, '3': mainldf, '4': mainlpf, '5': mainrdf, '6': mainrpf}

Subject = input('Ingresar identificación del sujeto: ')
Tipo = input('Ingresar el tipo de experimento a realizar (M/I/O): ')   # Tipos posibles M , I , O
Run = int(input('Ingresar el número de serie: '))

print("looking for an EEG stream...")
streams = resolve_stream('type', 'EEG')
# inlet = StreamInlet(streams[0])

valores = 0

while __name__ == '__main__':
    # descanso()
    mainbeo()
    des = beo
    beo += 1
    ide = BEO
    descanso()

    while valores != 30:
        valores = lch + rch + ldf + lpf + rdf + rpf - 6
        print(valores)
        opcion = str(random.randint(1, 6))
        if opcion == '1' and lch != 6:
            operaciones[opcion]()
            des = lch
            lch += 1
            ide = LCH
            descanso()

        elif opcion == '2' and rch != 6:
            operaciones[opcion]()
            des = rch
            rch += 1
            ide = RCH
            descanso()

        elif opcion == '3' and ldf != 6:
            operaciones[opcion]()
            des = ldf
            ldf += 1
            ide = LDF
            descanso()

        elif opcion == '4' and lpf != 6:
            operaciones[opcion]()
            des = lpf
            lpf += 1
            ide = LPF
            descanso()

        elif opcion == '5' and rdf != 6:
            operaciones[opcion]()
            des = rdf
            rdf += 1
            ide = RDF
            descanso()

        elif opcion == '6' and rpf != 6:
            operaciones[opcion]()
            des = rpf
            rpf += 1
            ide = RPF
            descanso()

    valores, lch, rch, ldf, lpf, rdf, rpf = 1, 1, 1, 1, 1, 1, 1
    continuar = input("Desea continuar (S/N) :")
    if continuar == 'N' or continuar == 'n':
        break
    else:
        Run += 1

