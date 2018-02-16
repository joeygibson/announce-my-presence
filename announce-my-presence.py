import json
import os

def lambda_handler(event, context):
    if os.environ['DEBUG'] == "true":
        print("lambda_handler event=" + json.dumps(event))
    
    app_id = os.environ['APP_ID']
    
    session = event.get('session')
    
    # if 'session' is None:
    #     print("NO SESSION! APP_ID: " + app_id)
    # else:
    #     if event['session']['application']['applicationId'] != app_id:
    #         raise ValueError("Invalid Application ID")
    
    request = event['request']
    request_type = request['type']
    
    if request_type == "LaunchRequest":
        return on_launch(request, session)
    elif request_type == "IntentRequest":
        return on_intent(request, session)
    
def stop():
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
    if intent_name == "AnnounceIntent" or intent_name == 'AMAZON.ResumeIntent' or intent_name == 'AMAZON.NextIntent':
        return play()  
    elif intent_name == "StopIntent" or intent_name == "AMAZON.CancelIntent" or intent_name == "AMAZON.PauseIntent":
        return stop()
    else:
        raise ValueError("Invalid intent")    

def on_launch(launch_request, session):
    """ Called when the user launches the skill without specifying what they
    want
    """

    print("on_launch requestId=" + launch_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    
    return play()      
    
def play():
    fanfare_url = os.environ['FANFARE_URL']
    
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
                            "url": f"{fanfare_url}",
                            "offsetInMilliseconds": 0
                        }
                    }
                }
            ],
            "shouldEndSession": True
        }
    }
