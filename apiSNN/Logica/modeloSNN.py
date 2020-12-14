from django.db import models
from django.urls import reverse
import pandas as pd
import numpy as np
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import make_column_transformer, ColumnTransformer
from sklearn.pipeline import Pipeline
from tensorflow.python.keras.models import load_model, model_from_json
from keras import backend as K
from apiSNN import models
import os
from tensorflow.python.keras.models import Sequential
import pathlib
import numpy as np
from skimage import io, transform

class modeloSNN():
    """Clase modelo SNN"""

    def cargarCNN(nombreArchivoModelo,nombreArchivoPesos):
        K.reset_uids()
        # Cargar la Arquitectura desde el archivo JSON
        with open(nombreArchivoModelo+'.json', 'r') as f:
            model = model_from_json(f.read())
        # Cargar Pesos (weights) en el nuevo modelo
        model.load_weights(nombreArchivoPesos+'.h5') 
        print("Red Neuronal Cargada desde Archivo") 
        return model
    def predecirAnimal(self,ruta1):
        #Modelo optimizado
        print('MODELO OPTIMIZADO')
        nombreArchivoModelo=r'apiSNN/Logica/arquitectura'
        nombreArchivoPesos=r'apiSNN/Logica/pesos'
        #return (str(pathlib.Path().absolute())+'\Modelos')
        self.Selectedmodel=self.cargarCNN(nombreArchivoModelo,nombreArchivoPesos) 
        print(self.Selectedmodel)
        print(self.Selectedmodel.summary())
        #self.preprocesamiento(self)
        
        pred1 = self.cargarImagen(self, ruta1)
        
        res1=self.predict(self,pred1)
        
        resultado = res1

        return resultado
    def predict(self, pred):
        resultados = self.Selectedmodel.predict(pred)[0]
        maxElement = np.amax(resultados)
        certeza = str(round(maxElement*100, 4))+'%'
        print(certeza)
        result = np.where(resultados == np.amax(resultados))
        print('Max :', maxElement)
        print('Tipo: ', result[0][0])
        
        resultado = self.resultado(result[0][0])
        return resultado, maxElement, certeza

    def cargarImagen(self, ruta):
        im = io.imread(ruta)
        im = transform.resize(im, (100, 100))
        im = np.asarray(im)
        pred = im.reshape(-1,100,100,3)
        
        return pred
    def resultado(result):
        if(result == 0):
            resultado = 'Perro '
            print(resultado)
        else:
            resultado = 'Gato '
            print(resultado)
        return resultado
        
