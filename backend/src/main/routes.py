from flask import Blueprint, jsonify, request
from backend.src.auth.models import User, Card
from scraper.scraper import scrape_tcgplayer

bp = Blueprint('main', __name__)

@bp.route('/api/card-values')
def card_values():
    # Dummy data for demonstration
    labels = ['January', 'February', 'March', 'April', 'May', 'June', 'July']
    values = [65, 59, 80, 81, 56, 55, 40]
    return jsonify({'labels': labels, 'values': values})

@bp.route('/api/search')
def search():
    query = request.args.get('query')
    # Here, call your scraper function and return the results
    results = scrape_tcgplayer(query)
    return jsonify({'results': results})
