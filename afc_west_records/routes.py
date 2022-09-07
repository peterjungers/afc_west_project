"""
This module contains all routes for app, as well as a helper function
common to all team routes used to render team templates.
"""


from flask import render_template, url_for

from afc_west_records import app
from afc_west_records.models import RegularSeason, Postseason, SuperBowl
from afc_west_records import searches


@app.route("/")
@app.route("/index")
def index():
    return render_template(
        "index.html",
        heading="AFC West",
        image=url_for("static", filename="images/afc_logo.png")
    )


# Common template for all teams
def get_team_template(team_id, address, title, heading, image,
                      afc_west, afl_western, afc, afl, sb):
    template = render_template(
        address,
        title=title,
        heading=heading,
        image=image,
        reg_headers=searches.get_reg_headers(team_id),
        post_headers=searches.get_post_headers(team_id),
        sb_headers=searches.get_sb_headers(team_id),
        reg_data=searches.get_reg_data(team_id),
        post_data=searches.get_post_data(team_id),
        sb_data=searches.get_sb_data(team_id),
        reg_totals=searches.get_reg_totals(team_id),
        post_totals=searches.get_post_totals(team_id),
        combined_totals=searches.get_combined_totals(
            searches.get_reg_totals(team_id),
            searches.get_post_totals(team_id)),
        afc_west_count=afc_west,
        afl_western_count=afl_western,
        afc_count=afc,
        afl_count=afl,
        sb_count=sb,
        sb_totals=searches.get_sb_totals(team_id)
    )

    return template


@app.route("/denver_broncos")
def denver_broncos():
    team_id = 1
    address = "denver_broncos.html"
    title = "AFC West Records — Denver Broncos"
    heading = "Denver Broncos"
    image = url_for("static", filename="images/denver_broncos_logo.png")
    # Variables hard-coded for now; new "achievements" table can be made
    afc_west = 15
    afl_western= 0
    afc = 8
    afl = 0
    sb = 3

    template = get_team_template(team_id, address, title, heading, image,
                                 afc_west, afl_western, afc, afl, sb)
    return template


@app.route("/kansas_city_chiefs")
def kansas_city_chiefs():
    team_id = 2
    address = "kansas_city_chiefs.html"
    title = "AFC West Records — Kansas City Chiefs"
    heading = "Kansas City Chiefs"
    image = url_for("static", filename="images/kansas_city_chiefs_logo.png")
    # Variables hard-coded for now; new "achievements" table can be made
    afc_west = 12
    afl_western= 2
    afc = 2
    afl = 3
    sb = 2

    template = get_team_template(team_id, address, title, heading, image,
                                 afc_west, afl_western, afc, afl, sb)
    return template


@app.route("/las_vegas_raiders")
def las_vegas_raiders():
    team_id = 3
    address = "las_vegas_raiders.html"
    title = "AFC West Records — Las Vegas Raiders"
    heading = "Las Vegas Raiders"
    image = url_for("static", filename="images/las_vegas_raiders_logo.png")
    # Variables hard-coded for now; new "achievements" table can be made
    afc_west = 12
    afl_western= 3
    afc = 4
    afl = 1
    sb = 3

    template = get_team_template(team_id, address, title, heading, image,
                                 afc_west, afl_western, afc, afl, sb)
    return template


@app.route("/los_angeles_chargers")
def los_angeles_chargers():
    team_id = 4
    address = "los_angeles_chargers.html"
    title = "AFC West Records — Los Angeles Chargers"
    heading = "Los Angeles Chargers"
    image = url_for("static", filename="images/los_angeles_chargers_logo.png")
    # Variables hard-coded for now; new "achievements" table can be made
    afc_west = 10
    afl_western= 5
    afc = 1
    afl = 1
    sb = 0

    template = get_team_template(team_id, address, title, heading, image,
                                 afc_west, afl_western, afc, afl, sb)
    return template
