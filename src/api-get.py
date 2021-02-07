import json

import util


def lambda_handler(event, context):
    try:
        height = float(event['queryStringParameters']['height'])
        weight = float(event['queryStringParameters']['weight'])
    except KeyError as e:
        print(e)
        return util.get_client_error_object('Bad parameter error.')
    except ValueError as e:
        print(e)
        return util.get_client_error_object('Bad parameter error.')
    
    res_body = {
            "message": "Get success!!!",
            "bmi": util.calc_bmi(height, weight),
            "healthy_weight": util.calc_healthy_weight(height, weight),
        }

    return util.get_success_object(res_body)
