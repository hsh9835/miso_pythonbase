from flask import Blueprint

from app import bpName

bp = Blueprint(bpName(__file__), __name__)


@bp.route('/axiosTest', methods=['POST'])
def axiosTest():
    return {'id':'axios 작동 잘 되고 있습니다.'}
