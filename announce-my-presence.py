import json
import os

def lambda_handler(event, context):
    print("lambda_handler event=" + json.dumps(event))
    
    app_id = os.environ['APP_ID']
    
    if event['session']['application']['applicationId'] != app_id:
        raise ValueError("Invalid Application ID")
    
    request = event['request']
    request_type = request['type']
    session = event['session']
    
    if request_type == "LaunchRequest":
        return on_launch(request, session)
    elif request_type == "IntentRequest":
        return on_intent(request, session)
    elif request_type == 'AMAZON.PauseIntent':
        return on_stop(request, session)

def on_stop(intent_request, session):
    return {
        'version': '1.0',
        'response': {
            "directives": [
                {
                    "type": "AudioPlayer.Stop",
                }
            ],
            "shouldEndSession": True
        }
    }
    
def on_intent(intent_request, session):
    """ Called when the user specifies an intent for this skill """

    print("on_intent requestId=" + intent_request['requestId'] +
          ", sessionId=" + session['sessionId'])

    intent = intent_request['intent']
    intent_name = intent_request['intent']['name']

    # Dispatch to your skill's intent handlers
    if intent_name == "AMAZON.PauseIntent":
        return on_stop(intent, session)
    elif intent_name == "StopIntent":
        return on_stop(intent, session)
    else:
        raise ValueError("Invalid intent")    

def on_launch(launch_request, session):
    """ Called when the user launches the skill without specifying what they
    want
    """

    print("on_launch requestId=" + launch_request['requestId'] +
          ", sessionId=" + session['sessionId'])
          
    # Dispatch to your skill's launch
    return {
        'version': '1.0',
        'response': {
            "directives": [
                {
                    "type": "AudioPlayer.Play",
                    "playBehavior": "REPLACE_ALL",
                    "audioItem": {
                        "stream": {
                            "token": "12345",
                            "url": "https://s3.amazonaws.com/jygb-alexa-assets/fanfare.mp3",
                            "offsetInMilliseconds": 0
                        }
                    }
                }
            ],
            "shouldEndSession": True
        }
    }


