import json

import util


def lambda_handler(event, context):
    try:
        body = json.loads(event['body'])
        height = float(body['height'])
        weight = float(body['weight'])
        comment = body['comment']
    except KeyError as e:
        print(e)
        return get_client_error_object('Bad parameter error.')
    except ValueError as e:
        print(e)
        return get_client_error_object('Bad parameter error.')

    res_body = {
            "message": "Post success!!!",
            "bmi": util.calc_bmi(height, weight),
            "healthy_weight": util.calc_healthy_weight(height, weight),
            "your_comment": comment
        }
    
    return util.get_success_object(res_body)
