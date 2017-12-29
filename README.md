# announce-my-presence

AWS Lambda function for the Announce My Presence Alexa skill

## Requirements

* Python 3
* An MP3, or other sound file that is compatible with the [Alexa Audio API](https://developer.amazon.com/blogs/post/Tx1DSINBM8LUNHY/New-Alexa-Skills-Kit-ASK-Feature-Audio-Streaming-in-Alexa-Skills)

## Environment Variables
The skill uses three environment variables, and they all must be set. They are

* `APP_ID` - This is the application ID of the skill that will be calling this function. Without this, 
it could be called by anyone's skill.
* `DEBUG` - If set to `true`, then the JSON of each request is logged
* `FANFARE_URL` - This is the URL of the sound to play for the fanfare.

