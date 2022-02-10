from flask import Blueprint, abort, jsonify, request
from web_scraping.service.scraping_service import colhendo_dados

web_scraping = Blueprint('web_scraping', __name__)


@web_scraping.route('/web_scraping', methods=['POST'])
def scraping_data():
    """
    
    Args:
        
    Returns:
       
    """

    dados = []

    if not request.is_json:
        abort(400)

    for value in request.json:
        dados.append(value)

    try:

        colhendo_dados(request.json['url'])

        response = "Sucesso"

        return jsonify(response), 200
    except ValueError:
        return abort(401)