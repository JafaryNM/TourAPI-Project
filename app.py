
from flask import Flask, request, json

app =Flask(__name__)

transports=[]

@app.route('/')

def index():
    return {
        'response':'Sasa Upo Nyumbani'
    }

@app.route('/home')
def home():
    return {
        'response': 'nipo hapa karibu'
    }
    

@app.route('/register-transport' , methods=['POST'])

def register():
    
    ############# Return JSON DATA FROM RESPONSE #############
    
    transport_data=request.get_json()
    if transport_data:
        transports.append(transport_data)  
 
        return{
            'response':'Data is success added'
        }
     
    return{
        'response':'Transport data should not be empty'
    }
    
    
@app.route('/get_all_transports')

def get_all_transport():
    
    ########## APPLING SOME FILTER PARAMETERS ################
    
    r_body=request.get_json()
    
    if r_body and r_body.get('place'):
        place=r_body.get('place')
        f_transports=[transport for transport in transports if transport.get('place')==place]
        return {
            "Transports":f_transports
        }
    
    return{
        
        'Transports':transports
    }
    




    
    
    
    
    
    
        
if __name__=='__main__':
    
    app.run(debug=True)
    
    
    
    
    
    