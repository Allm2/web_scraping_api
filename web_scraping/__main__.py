import logging
import os

from web_scraping import application

def start_server():
    port = int(os.environ.get('PORT', 9000))
    logging.getLogger('web_scraping.__main__').info(
        f'Web scraping API - metasearch anuncios  {port}.')
    application.run(host='0.0.0.0', port=port)


if __name__ == '__main__':
    start_server()