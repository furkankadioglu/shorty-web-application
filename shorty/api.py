from shorty.Engines.ShortLinkEngine import ShortLinkEngine
from flask import Blueprint, jsonify, request
import requests
import validators

api = Blueprint('api', __name__)

@api.route('/shortlinks', methods=['POST'])
def create_shortlink():
    engine = ShortLinkEngine()
    requestData = request.json
    if "url" not in requestData:
        return jsonify({
            "success": False, 
            "details": [
                "url parameter is missing"
            ]
        }), 400

    url = requestData["url"]


    if validators.url(url) == False:
        return jsonify({
            "success": False, 
            "details": [
                "url should be an url, like https://google.com"
            ]
        }), 400

    if "provider" in requestData:
        provider = requestData["provider"]
    else:
        provider = None

    try:
        return engine.shortLink(url, provider)
    except requests.exceptions.ReadTimeout:
        return jsonify({"success": False, "details": ["3rd party service time out issue"]}), 408
    except:
        return jsonify({"success": False}), 500
