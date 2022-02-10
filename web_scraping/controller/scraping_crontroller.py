from flask import Blueprint, abort, jsonify, request

# from web_scraping.service.classification_service import ClassificationService

web_scraping = Blueprint('web_scraping', __name__)


@web_scraping.route('/web_scraping', methods=['GET'])
def scraping_data():
    """
    
    Args:
        
    Returns:
       
    """
    # service = ClassificationService()
    dados = []

    # if not request.is_json:
    #     abort(400)
    #
    # for value in request.json:
    #     dados.append(value)

    try:
        response = "Sucesso"
        return jsonify(response), 200
    except ValueError:
        return abort(401)