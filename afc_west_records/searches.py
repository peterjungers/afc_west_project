"""
This module handles all searches to "models.py", returns results to
"routes.py"

Contents:
1. Get table headers
2. Get table data
3. Get summed data totals
"""

from sqlalchemy import func

from afc_west_records.models import RegularSeason, Postseason, SuperBowl


# ****************************************************************************
# 1. Get table headers

def get_reg_headers(team_id):
    header = ("Year", "Place", "W", "L", "T")
    return header


def get_post_headers(team_id):
    header = ("Year", "W", "L", "Highest Achievement")
    return header


def get_sb_headers(team_id):
    header = ("Year", "Number", "Result", "Score")
    return header


# ****************************************************************************
# 2. Get table data

def get_reg_data(team_id):
    reg_data = (RegularSeason.query
                .with_entities(RegularSeason.year,
                               RegularSeason.place,
                               RegularSeason.win,
                               RegularSeason.loss,
                               RegularSeason.tie)
                .filter_by(team_id=team_id)
                .order_by(RegularSeason.year.desc())
    )

    return reg_data


def get_post_data(team_id):
    post_data = (Postseason.query
                 .with_entities(Postseason.year,
                                Postseason.win,
                                Postseason.loss,
                                Postseason.highest_achievement)
                 .filter_by(team_id=team_id)
                 .order_by(Postseason.year.desc())
    )

    return post_data


def get_sb_data(team_id):
    sb_data = (SuperBowl.query
               .with_entities(SuperBowl.year,
                              SuperBowl.super_bowl_number,
                              SuperBowl.win_loss,
                              SuperBowl.score)
               .filter_by(team_id=team_id)
               .order_by(SuperBowl.year.desc())
    )

    return sb_data


# ****************************************************************************
# 3. Get summed data totals

def get_reg_totals(team_id):
    """
    Queries return a single value within a tuple within a list, hence
    they are sent to "isolate_value()" to get just the value
    :return "reg_totals": the three isolated values within a new list
    """
    reg_win_sum = (RegularSeason.query
                   .with_entities(func.sum(RegularSeason.win))
                   .filter_by(team_id=team_id).all()
    )
    total_win = isolate_value(reg_win_sum)

    reg_loss_sum = (RegularSeason.query
                    .with_entities(func.sum(RegularSeason.loss))
                    .filter_by(team_id=team_id).all()
    )
    total_loss = isolate_value(reg_loss_sum)

    reg_tie_sum = (RegularSeason.query
                   .with_entities(func.sum(RegularSeason.tie))
                   .filter_by(team_id=team_id).all()
    )
    total_tie = isolate_value(reg_tie_sum)

    reg_totals = [total_win, total_loss, total_tie]

    return reg_totals


def get_post_totals(team_id):
    """
    Queries return a single value within a tuple within a list, hence
    they are sent to "isolate_value()" to get just the value
    :return "post_totals": the two isolated values within a new list
    """
    post_win_sum = (Postseason.query
                    .with_entities(func.sum(Postseason.win))
                    .filter_by(team_id=team_id).all()
    )
    total_win = isolate_value(post_win_sum)

    post_loss_sum = (Postseason.query
                     .with_entities(func.sum(Postseason.loss))
                     .filter_by(team_id=team_id).all()
    )
    total_loss = isolate_value(post_loss_sum)

    post_totals = [total_win, total_loss]

    return post_totals


def isolate_value(value):
    """
    :parameter "value": a value within a tuple within a list
    :return "second_pop_value": the isolated value
    """
    first_pop, first_pop_value = value[:-1], value[-1]
    second_pop, second_pop_value = first_pop_value[:-1], first_pop_value[-1]

    return second_pop_value


def get_combined_totals(reg_totals, post_totals):
    win = reg_totals[0] + post_totals[0]
    loss = reg_totals[1] + post_totals[1]
    tie = reg_totals[2]
    combined_totals = [win, loss, tie]

    return combined_totals


def get_sb_totals(team_id):
    sb_win_sum = (SuperBowl.query
                  .filter_by(team_id=team_id)
                  .filter(SuperBowl.win_loss.like("W"))
                  .count()
    )
    total_win = sb_win_sum

    sb_loss_sum = (SuperBowl.query
                  .filter_by(team_id=team_id)
                  .filter(SuperBowl.win_loss.like("L"))
                  .count()
    )
    total_loss = sb_loss_sum

    sb_totals = [total_win, total_loss]

    return sb_totals
