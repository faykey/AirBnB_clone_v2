#!/usr/bin/python3
"""Starts a Flask Web App listening on 0.0.0.0, port 5000

Routes:
        /: will display “Hello HBNB!”
            /hbnb: will display “HBNB”
                /c/<text>: will display “C ” followed <text>
                """
from flask import Flask

<<<<<<< HEAD
                app = Flask(__name__)


                @app.route('/', strict_slashes=False)
                def hello_hbnb():
                        """Will display 'Hello HBNB!'"""
                            return "Hello HBNB!"


                        @app.route('/hbnb', strict_slashes=False)
                        def hbnb():
                                """Will display 'HBNB'"""
                                    return "HBNB"


                                @app.route('/c/<text>', strict_slashes=False)
                                def c(text):
                                        """Will display 'C' followed by <text>"""
                                            text = text.replace("_", " ")
                                                return "C {}".format(text)


                                            if __name__ == '__main__':
                                                    app.run(host='0.0.0.0')
=======
if __name__ == '__main__':
    app = Flask(__name__)

    @app.route('/', strict_slashes=False)
    def index():
        """Display 'Hello HBNB!'
        """
        return 'Hello HBNB!'

    @app.route('/hbnb', strict_slashes=False)
    def hbnb():
        """Display 'HBNB'
        """
        return 'HBNB'

    @app.route('/c/<text>', strict_slashes=False)
    def c(text):
        """Display “C ” followed by the value of
        the text variable (replace underscore _
        symbols with a space)
        """
        return 'C ' + text.replace('_', ' ')

    app.run('0.0.0.0')
>>>>>>> 5ceb222ad8f99cf53c3c294f6a03577a774defbb
