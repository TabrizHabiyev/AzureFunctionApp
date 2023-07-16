from model1 import model1_prediction
from model2 import model2_prediction
from model3 import model3_prediction
from model4 import model4_prediction

import json
import azure.functions as func

def main(req: func.HttpRequest) -> func.HttpResponse:
    data = req.get_json()

    if req.route_params.get('model') == 'model1':
        result = model1_prediction(data)
    elif req.route_params.get('model') == 'model2':
        result = model2_prediction(data)
    elif req.route_params.get('model') == 'model3':
        result = model3_prediction(data)
    elif req.route_params.get('model') == 'model4':
        result = model4_prediction(data)
    else:
        return func.HttpResponse("Invalid model specified", status_code=400)

    return func.HttpResponse(json.dumps(result), mimetype='application/json')
