import json, utm

def lambda_handler(event, context):
    # parse query string parameter
    lat, lon = float(event['queryStringParameters']['lat']), float(event['queryStringParameters']['lon'])

    # convert to utm
    u = utm.from_latlon(lat, lon)
    
    # format api response
    body = {'UTM_X': u[0], 'UTM_Y': u[1], 'UTM_Zone': u[2] }
    response = { 'statusCode': 200, 'headers': { 'Content-Type': 'application/json' }, 'body': json.dumps(body) }

    return response