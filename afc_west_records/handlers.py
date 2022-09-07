"""
This module contains error handlers.
"""

from flask import render_template

from afc_west_records import app


@app.errorhandler(404)
def error_404(error):
    return render_template("errors/404.html",
                           title="AFC West Records — Error 404",
                           heading="Page not found"
                           ), 404


@app.errorhandler(500)
def error_500(error):
    return render_template("errors/500.html",
                           title="AFC West Records — Error 500",
                           heading="Page not found"
                           ), 500
