from flask import Flask, request, json
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
import datetime




app =Flask(__name__)

db=SQLAlchemy(app)
migrate=Migrate(app, db,render_as_batch=True)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///twende.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True


class Transport(db.Model):
    
    id=db.Column(db.Integer, primary_key=True)
    transport_type=db.Column(db.String(120), nullable=False)
    rent_fee=db.Column(db.String(120), nullable=False)
    location=db.Column(db.String(120),nullable=False)
    phone=db.Column(db.String(20), nullable=False)
    created_date=db.Column(db.DateTime, default=datetime.datetime.now)
    
    
    def __repr__(self):
        
        return f"Transport {self.id}:  {self.rent_fee}"



@app.route('/register-transport', methods=['POST'])

def register_transport():
    
    transport_data=request.get_json()
    try:
         my_transports=Transport(
        transport_type= transport_data.get('transport_type'),
        rent_fee=transport_data.get('rent_fee'),
        location=transport_data.get('location'),
        phone=transport_data.get('phone'),
        created_date=transport_data.get('created_date')
    )
         db.session.add(my_transports)
         db.session.commit()
         return{
             
             'response':{
                 'transport_id':my_transports.id,
                'transport_type':my_transports.transport_type,
                'rent_fee':my_transports.rent_fee,
                'phone':my_transports.phone,
                'message':'Transport Registered Successfully'
                
                
                
             }
             
         }

    except Exception as bug:
        print(bug)
        
        return {
            
            'response':"Transport registration fail"
        }
        
    
   
@app.route('/register_all_transports', methods=['GET'])

def get_all_transport():
    
    all_transport=Transport.query.all()
    cleaned_list=[]
    for transport in all_transport:
        transport_dict={
            "id":transport.id,
            "phone":transport.phone,
            "location":transport.location,
            "transport_type":transport.transport_type,
            "rent_fee":transport.rent_fee,
            "register_date":transport.created_date
            
        }
        
        cleaned_list.append(transport_dict)
    
    
    return{
        "Transports":cleaned_list
    }



    
    
        
if __name__=='__main__':
    
    app.run(debug=True)
    
    
    
    
    
    