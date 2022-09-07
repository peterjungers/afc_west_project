"""
This module contains all models for app.
"""

from afc_west_records import db


class Team(db.Model):
    team_id = db.Column(db.Integer, primary_key=True)
    team_name = db.Column(db.String)

    def __repr__(self):
        return (f"Team({self.team_name})")


class RegularSeason(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    team_id = db.Column(db.Integer, db.ForeignKey("team.team_id"),
                        nullable=False)
    year = db.Column(db.Integer)
    place = db.Column(db.String)
    win = db.Column(db.Integer)
    loss = db.Column(db.Integer)
    tie = db.Column(db.Integer)

    def __repr__(self):
        return (f"""RegularSeason(
                {self.team_id},
                {self.year},
                {self.place},
                {self.win},
                {self.loss},
                {self.tie})""")


class Postseason(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    team_id = db.Column(db.Integer, db.ForeignKey("team.team_id"),
                        nullable=False)
    year = db.Column(db.Integer)
    win = db.Column(db.Integer)
    loss = db.Column(db.Integer)
    highest_achievement = db.Column(db.String)

    def __repr__(self):
        return (f"""Postseason(
                {self.team_id},
                {self.year},
                {self.win},
                {self.loss},
                {self.highest_achievement})""")


class SuperBowl(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    team_id = db.Column(db.Integer, db.ForeignKey("team.team_id"),
                        nullable=False)
    year = db.Column(db.Integer)
    super_bowl_number = db.Column(db.String)
    win_loss = db.Column(db.String)
    score = db.Column(db.String)

    def __repr__(self):
        return (f"""SuperBowl(
                {self.team_id},
                {self.year},
                {self.super_bowl_number},
                {self.win_loss},
                {self.score})""")
