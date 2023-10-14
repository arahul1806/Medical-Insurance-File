import json

import pickle

import numpy as np

import config


class MedicalInsurance():
    
    def __init__ (self, age, sex, bmi, children, smoker, region):
        self.age = age
        self.sex = sex
        self.bmi = bmi
        self.children = children
        self.smoker = smoker
        self.region = 'region_' + region
        
    def load_model(self):
        with open(config.MODEL_FILE_PATH, 'rb') as f:
            self.model = pickle.load(f)
            
        with open(config.JSON_FILE_PATH, 'r') as f:
            self.data = json.load(f)
            
    def get_predict_charges(self):
        
        self.load_model()
        
        test_array = np.zeros(len(self.data['columns']))
        
        test_array[0] = self.age  
        test_array[1] = self.data["sex"][self.sex]
        test_array[2] = self.bmi
        test_array[3] = self.children
        test_array[4] = self.data["smoker"][self.smoker]
        region_index = self.data['columns'].index(self.region)
        test_array[region_index] = 1
        
        print('TESTING ARRAY >>', test_array)
        
        predict_charges = self.model.predict([test_array])
        
        return predict_charges
    
    if __name__ == '__main__':
        
        # age = 25.0   
        # sex = 'male'
        # bmi = 28.3
        # children = 1
        # smoker = 'yes'
        # region = 'southeast'
        
        med_ins = MedicalInsurance(age, sex, bmi, children, smoker, region)
        med_ins.get_predict_charges()
        
        