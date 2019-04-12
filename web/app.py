from bottle import route, run, template, request, view, response

from card_validator.validator import get_issuer


@route('/hello/<name>')
def index(name):
    return template('<b>Hello {{name}}</b>!', name=name)


@route('/')
@view('index')
def the_real_index():
    return {
        "message": request.query.get('message', 'there was no message')
    }


@route('/validate')
def validate():
    card_number = request.query.get('cardNumber', '').strip()

    if card_number:

        try:
            issuer = get_issuer(card_number)
        except ValueError:
            response.status = 400
            return {"result": "This is not a valid credit card.", "cardNumber": card_number}

        return {"issuer": issuer, "result": "It is a {} card".format(issuer)}

    response.status = 400
    return {"detail": "The cardNumber is required as a query parameter."}


run(host='localhost', port=8000)

