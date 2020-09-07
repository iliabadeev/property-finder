# PropertyFinder
Artificial Intelligence capable of automated valuation of real estate objects. 


## Content
The project consists of 3 main parts:
- Research (pipelines and modules): [backend/research/](backend/research/)
- BackEnd (API): [backend/](backend/)
- FrontEnd (Dash): [frontend/](frontend/)  

*Research part was merged into backend to resolve problems with models dumping and loading.*  

## Research 
Consists of several main files:  
- Loading: [backend/research/loading.ipynb](backend/research/loading.ipynb)
    - Main goal: load, optimize data, create data structures
- Preprocessing: [backend/research/preprocessing.ipynb](backend/research/preprocessing.ipynb)
    - Main goal: create pipeline to clean and generate features from the data structure, dump the pipeline
- Model_AVM: [backend/research/model_avm.ipynb](backend/research/model_avm.ipynb)
    - Main goal: create model to predict prices, dump the model
- Model_Transacted: [backend/research/model_transacted.ipynb](backend/research/model_transacted.ipynb)
    - Main goal: create model to predict transaction in 1 month, dump the model  
    
    
All related code is in the folder: [backend/research/core](backend/research/core)

## Backend

Structure of the API is designed in the following folders:  
- Server (controller) responsible for routs [backend/server.py](backend/server.py)  
- Endpoints responsible for logic [backend/api/](backend/api/)  
- Data structures (models) are in [backend/core/](backend/core)  

**How to run**:  
`$ cd backend`  
`$ chmod +x docker/run.sh`  
`$ ./docker/run.sh`  
*!Keep the terminal open!*  

**Requests Examples**:  
Health: http://0.0.0.0:5000/  
Prediction AVM: http://0.0.0.0:5000/api/v1/model/avm/predict?valid_from=2018-10-31+22%3A00%3A27&valid_to=2018-11-07+05%3A01%3A46&offer_type=1&bedrooms=2&bathrooms=3&sqft=839&cheques=3&price=75000&transacted=0&location_path=Dubai%2CBusiness+Bay&latitude=25.187400817871094&longitude=55.26380157470703  
Prediction Transacted: http://0.0.0.0:5000/api/v1/model/transacted/predict?valid_from=2018-10-31+22%3A00%3A27&valid_to=2018-11-07+05%3A01%3A46&offer_type=1&bedrooms=2&bathrooms=3&sqft=839&cheques=3&price=75000&transacted=0&location_path=Dubai%2CBusiness+Bay&latitude=25.187400817871094&longitude=55.26380157470703  
Properties: http://0.0.0.0:5000/api/v1/property/all  
Property: http://0.0.0.0:5000/api/v1/property/2338015   
Locations: http://0.0.0.0:5000/api/v1/location/all    
Location: http://0.0.0.0:5000/api/v1/location/42  

## Frontend
Structure:  
- [frontend/assets](frontend/assets) contains css.
- [frontend/connection](frontend/connection) contains connection to the BackEnd.
- [frontend/view](frontend/view) contains all layouts.

**How to run**:  
`$ python wsgi.py`  
*If you use venv - there is requirements.txt*
*!Keep the terminal open!*  

Service: http://0.0.0.0:8050/
     
