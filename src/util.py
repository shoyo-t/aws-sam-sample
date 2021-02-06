import json

def get_success_object(body):
    response = {
        "statusCode": 200,
        "headers": {
            "Access-Control-Allow-Origin": "*"
        },
        "body": json.dumps(body),
    }
    return response

def get_client_error_object(msg):
    error_res = {
        "statusCode": 400,
        'headers': {
            'Content-Type': 'application/json',
            "Access-Control-Allow-Origin": "*"
        },
        "body": json.dumps({
            "message": msg,
        }),
    }

def calc_bmi(height, weight):
    bmi = weight / (height*height)
    return round(bmi, 2)

def calc_healthy_weight(height, weight):
    healthy_weight = (height*height) * 22
    return round(healthy_weight, 2)
