import os
from flask import Flask, request
from ask_sdk_core.skill_builder import SkillBuilder
from flask_ask_sdk.skill_adapter import SkillAdapter

from handlers import (
    LaunchRequestHandler,
    GeneralHelpIntentHandler,
    OfficeTimingsIntentHandler,
    MeetingRoomAvailabilityIntentHandler,
    PrintSupportIntentHandler,
    CafeteriaTimingIntentHandler,
    LeavePolicyIntentHandler,
    ITSupportIntentHandler,
    HelpIntentHandler,
    CancelOrStopIntentHandler,
    FallbackIntentHandler,
    SessionEndedRequestHandler,
    IntentReflectorHandler,
    CatchAllExceptionHandler
)

app = Flask(__name__)

sb = SkillBuilder()

sb.add_request_handler(LaunchRequestHandler())
sb.add_request_handler(GeneralHelpIntentHandler())
sb.add_request_handler(OfficeTimingsIntentHandler())
sb.add_request_handler(MeetingRoomAvailabilityIntentHandler())
sb.add_request_handler(PrintSupportIntentHandler())
sb.add_request_handler(CafeteriaTimingIntentHandler())
sb.add_request_handler(LeavePolicyIntentHandler())
sb.add_request_handler(ITSupportIntentHandler())
sb.add_request_handler(HelpIntentHandler())
sb.add_request_handler(CancelOrStopIntentHandler())
sb.add_request_handler(FallbackIntentHandler())
sb.add_request_handler(SessionEndedRequestHandler())
sb.add_request_handler(IntentReflectorHandler()) 

sb.add_exception_handler(CatchAllExceptionHandler())

skill_adapter = SkillAdapter(skill=sb.create(), skill_id='amzn1.ask.skill.33f67054-8a8c-4320-9189-ebc54dac339d', app=app)


@app.route("/alexa", methods=["POST"])
def alexa_endpoint():
    return skill_adapter.dispatch_request()

if __name__ == "__main__":
    # app.run(debug=True, port=5000)
    app.run(debug=False, host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))