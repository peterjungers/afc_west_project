from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import csv
import sqlite3

from afc_west_records import db
from afc_west_records.models import Team, Postseason, SuperBowl


# BE CAREFUL! I left the SQLAlchemy populate tables section
# un-commented and when I ran the site and queried the database it
# re-added the data in this section. Weird. I guess this is run
# every time because it is importing "db"(?).


# # Populating Team, Postseason, and SuperBowl tables via SQLAlchemy
# engine = create_engine("sqlite:///site.db")
# Session = sessionmaker(bind=engine)
# session = Session()

# data = [
#     Team(team_name="Denver Broncos"),
#     Team(team_name="Kansas City Chiefs"),
#     Team(team_name="Las Vegas Raiders"),
#     Team(team_name="Los Angeles Chargers"),
#
#     # Denver Broncos
#     Postseason(team_id=1, year=1977, win=2, loss=1, highest_achievement="AFC Champions"),
#     Postseason(team_id=1, year=1978, win=0, loss=1, highest_achievement="AFC West Champions"),
#     Postseason(team_id=1, year=1979, win=0, loss=1, highest_achievement="AFC Wild Card Winners"),
#     Postseason(team_id=1, year=1983, win=0, loss=1, highest_achievement="AFC Wild Card Winners"),
#     Postseason(team_id=1, year=1984, win=0, loss=1, highest_achievement="AFC West Champions"),
#     Postseason(team_id=1, year=1986, win=2, loss=1, highest_achievement="AFC Champions"),
#     Postseason(team_id=1, year=1987, win=2, loss=1, highest_achievement="AFC Champions"),
#     Postseason(team_id=1, year=1989, win=2, loss=1, highest_achievement="AFC Champions"),
#     Postseason(team_id=1, year=1991, win=1, loss=1, highest_achievement="AFC West Champions"),
#     Postseason(team_id=1, year=1993, win=0, loss=1, highest_achievement="AFC Wild Card Winners"),
#     Postseason(team_id=1, year=1996, win=0, loss=1, highest_achievement="AFC West Champions"),
#     Postseason(team_id=1, year=1997, win=4, loss=0, highest_achievement="Super Bowl Champions"),
#     Postseason(team_id=1, year=1998, win=3, loss=0, highest_achievement="Super Bowl Champions"),
#     Postseason(team_id=1, year=2000, win=0, loss=1, highest_achievement="AFC Wild Card Winners"),
#     Postseason(team_id=1, year=2003, win=0, loss=1, highest_achievement="AFC Wild Card Winners"),
#     Postseason(team_id=1, year=2004, win=0, loss=1, highest_achievement="AFC Wild Card Winners"),
#     Postseason(team_id=1, year=2005, win=1, loss=1, highest_achievement="AFC West Champions"),
#     Postseason(team_id=1, year=2011, win=1, loss=1, highest_achievement="AFC West Champions"),
#     Postseason(team_id=1, year=2012, win=0, loss=1, highest_achievement="AFC West Champions"),
#     Postseason(team_id=1, year=2013, win=2, loss=1, highest_achievement="AFC Champions"),
#     Postseason(team_id=1, year=2014, win=0, loss=1, highest_achievement="AFC West Champions"),
#     Postseason(team_id=1, year=2015, win=3, loss=0, highest_achievement="Super Bowl Champions"),
#
#     SuperBowl(team_id=1, year=1977, super_bowl_number="XII", win_loss="L", score="Dallas Cowboys: 27, Denver Broncos: 10"),
#     SuperBowl(team_id=1, year=1986, super_bowl_number="XXI", win_loss="L", score="New York Giants: 39, Denver Broncos: 20"),
#     SuperBowl(team_id=1, year=1987, super_bowl_number="XXII", win_loss="L", score="Washington Redskins: 42, Denver Broncos: 10"),
#     SuperBowl(team_id=1, year=1989, super_bowl_number="XXIV", win_loss="L", score="San Francisco 49ers: 55, Denver Broncos: 10"),
#     SuperBowl(team_id=1, year=1997, super_bowl_number="XXXII", win_loss="W", score="Denver Broncos: 31, Green Bay Packers: 24"),
#     SuperBowl(team_id=1, year=1998, super_bowl_number="XXXIII", win_loss="W", score="Denver Broncos: 34, Atlanta Falcons: 19"),
#     SuperBowl(team_id=1, year=2013, super_bowl_number="XLVIII", win_loss="L", score="Seattle Seahawks: 43, Denver Broncos: 8"),
#     SuperBowl(team_id=1, year=2015, super_bowl_number="50", win_loss="W", score="Denver Broncos: 24, Carolina Panthers: 10"),
#
#
#     # Kansas City Chiefs
#     Postseason(team_id=2, year=1962, win=1, loss=0, highest_achievement="AFL Champions"),
#     Postseason(team_id=2, year=1966, win=1, loss=1, highest_achievement="AFL Champions"),
#     Postseason(team_id=2, year=1968, win=0, loss=1, highest_achievement="Lost AFL Western Division Tiebreaker"),
#     Postseason(team_id=2, year=1969, win=3, loss=0, highest_achievement="Super Bowl Champions"),
#     Postseason(team_id=2, year=1971, win=0, loss=1, highest_achievement="AFC West Champions"),
#     Postseason(team_id=2, year=1986, win=0, loss=1, highest_achievement="AFC Wild Card Winners"),
#     Postseason(team_id=2, year=1990, win=0, loss=1, highest_achievement="AFC Wild Card Winners"),
#     Postseason(team_id=2, year=1991, win=1, loss=1, highest_achievement="AFC Wild Card Winners"),
#     Postseason(team_id=2, year=1992, win=0, loss=1, highest_achievement="AFC Wild Card Winners"),
#     Postseason(team_id=2, year=1993, win=2, loss=1, highest_achievement="AFC West Champions"),
#     Postseason(team_id=2, year=1994, win=0, loss=1, highest_achievement="AFC Wild Card Winners"),
#     Postseason(team_id=2, year=1995, win=0, loss=1, highest_achievement="AFC West Champions"),
#     Postseason(team_id=2, year=1997, win=0, loss=1, highest_achievement="AFC West Champions"),
#     Postseason(team_id=2, year=2003, win=0, loss=1, highest_achievement="AFC West Champions"),
#     Postseason(team_id=2, year=2006, win=0, loss=1, highest_achievement="AFC Wild Card Winners"),
#     Postseason(team_id=2, year=2010, win=0, loss=1, highest_achievement="AFC West Champions"),
#     Postseason(team_id=2, year=2013, win=0, loss=1, highest_achievement="AFC Wild Card Winners"),
#     Postseason(team_id=2, year=2015, win=1, loss=1, highest_achievement="AFC Wild Card Winners"),
#     Postseason(team_id=2, year=2016, win=0, loss=1, highest_achievement="AFC West Champions"),
#     Postseason(team_id=2, year=2017, win=0, loss=1, highest_achievement="AFC West Champions"),
#     Postseason(team_id=2, year=1018, win=1, loss=1, highest_achievement="AFC West Champions"),
#     Postseason(team_id=2, year=2019, win=3, loss=0, highest_achievement="Super Bowl Champions"),
#     Postseason(team_id=2, year=2020, win=2, loss=1, highest_achievement="AFC Champions"),
#     Postseason(team_id=2, year=2021, win=2, loss=1, highest_achievement="AFC West Champions"),
#
#     SuperBowl(team_id=2, year=1966, super_bowl_number="I", win_loss="L", score="Green Bay Packer: 35, Kansas City Chiefs: 10"),
#     SuperBowl(team_id=2, year=1969, super_bowl_number="IV", win_loss="W", score="Kansas City Chiefs: 23, Minnesota Vikings: 7"),
#     SuperBowl(team_id=2, year=2019, super_bowl_number="LIV", win_loss="W", score="Kansas City Chiefs: 31, San Francisco 49ers: 20"),
#     SuperBowl(team_id=2, year=2020, super_bowl_number="LV", win_loss="L", score="Tampa Bay Buccaneers: 31, Kansas City Chiefs: 9"),
#
#
#     # Las Vegas Raiders
#     Postseason(team_id=3, year=1967, win=1, loss=1, highest_achievement="AFL Champions"),
#     Postseason(team_id=3, year=1968, win=1, loss=1, highest_achievement="AFL Western Division Champions"),
#     Postseason(team_id=3, year=1969, win=1, loss=1, highest_achievement="AFL Western Division Champions"),
#     Postseason(team_id=3, year=1970, win=1, loss=1, highest_achievement="AFC West Champions"),
#     Postseason(team_id=3, year=1972, win=0, loss=1, highest_achievement="AFC West Champions"),
#     Postseason(team_id=3, year=1973, win=1, loss=1, highest_achievement="AFC West Champions"),
#     Postseason(team_id=3, year=1974, win=1, loss=1, highest_achievement="AFC West Champions"),
#     Postseason(team_id=3, year=1975, win=1, loss=1, highest_achievement="AFC West Champions"),
#     Postseason(team_id=3, year=1976, win=3, loss=0, highest_achievement="Super Bowl Champions"),
#     Postseason(team_id=3, year=1977, win=1, loss=1, highest_achievement="AFC Wild Card Winners"),
#     Postseason(team_id=3, year=1980, win=4, loss=0, highest_achievement="Super Bowl Champions"),
#     Postseason(team_id=3, year=1982, win=1, loss=1, highest_achievement="First Place, altered AFC"),
#     Postseason(team_id=3, year=1983, win=3, loss=0, highest_achievement="Super Bowl Champions"),
#     Postseason(team_id=3, year=1984, win=0, loss=1, highest_achievement="AFC Wild Card Winners"),
#     Postseason(team_id=3, year=1985, win=0, loss=1, highest_achievement="AFC West Champions"),
#     Postseason(team_id=3, year=1990, win=1, loss=1, highest_achievement="AFC West Champions"),
#     Postseason(team_id=3, year=1991, win=0, loss=1, highest_achievement="AFC Wild Card Winners"),
#     Postseason(team_id=3, year=1993, win=1, loss=1, highest_achievement="AFC Wild Card Winners"),
#     Postseason(team_id=3, year=2000, win=1, loss=1, highest_achievement="AFC West Champions"),
#     Postseason(team_id=3, year=2001, win=1, loss=1, highest_achievement="AFC West Champions"),
#     Postseason(team_id=3, year=2002, win=2, loss=1, highest_achievement="AFC Champions"),
#     Postseason(team_id=3, year=2016, win=0, loss=1, highest_achievement="AFC Wild Card Winners"),
#     Postseason(team_id=3, year=2021, win=0, loss=1, highest_achievement="AFC Wild Card Winners"),
#
#     SuperBowl(team_id=3, year=1967, super_bowl_number="II", win_loss="L", score="Green Bay Packers: 33, Oakland Raiders: 14"),
#     SuperBowl(team_id=3, year=1976, super_bowl_number="XI", win_loss="W", score="Oakland Raiders: 32, Minnesota Vikings: 14"),
#     SuperBowl(team_id=3, year=1980, super_bowl_number="XV", win_loss="W", score="Oakland Raiders: 27, Philadelphia Eagles: 10"),
#     SuperBowl(team_id=3, year=1983, super_bowl_number="XVIII", win_loss="W", score="Los Angeles Raiders: 38, Washington Redskins: 9"),
#     SuperBowl(team_id=3, year=2002, super_bowl_number="XXXVII", win_loss="L", score="Tampa Bay Buccaneers: 48, Oakland Raiders: 21"),
#
#
#     # Los Angeles Chargers
#     Postseason(team_id=4, year=1960, win=0, loss=1, highest_achievement="AFL Western Division Champions"),
#     Postseason(team_id=4, year=1961, win=0, loss=1, highest_achievement="AFL Western Division Champions"),
#     Postseason(team_id=4, year=1963, win=1, loss=0, highest_achievement="AFL Champions"),
#     Postseason(team_id=4, year=1964, win=0, loss=1, highest_achievement="AFL Western Division Champions"),
#     Postseason(team_id=4, year=1965, win=0, loss=1, highest_achievement="AFL Western Division Champions"),
#     Postseason(team_id=4, year=1979, win=0, loss=1, highest_achievement="AFC West Champions"),
#     Postseason(team_id=4, year=1980, win=1, loss=1, highest_achievement="AFC West Champions"),
#     Postseason(team_id=4, year=1981, win=1, loss=1, highest_achievement="AFC West Champions"),
#     Postseason(team_id=4, year=1982, win=1, loss=1, highest_achievement="AFC Wild Card Winners"),
#     Postseason(team_id=4, year=1992, win=1, loss=1, highest_achievement="AFC West Champions"),
#     Postseason(team_id=4, year=1994, win=2, loss=1, highest_achievement="AFC Champions"),
#     Postseason(team_id=4, year=1995, win=0, loss=1, highest_achievement="AFC Wild Card Winners"),
#     Postseason(team_id=4, year=2004, win=0, loss=1, highest_achievement="AFC West Champions"),
#     Postseason(team_id=4, year=2006, win=0, loss=1, highest_achievement="AFC West Champions"),
#     Postseason(team_id=4, year=2007, win=2, loss=1, highest_achievement="AFC West Champions"),
#     Postseason(team_id=4, year=2008, win=1, loss=1, highest_achievement="AFC West Champions"),
#     Postseason(team_id=4, year=2009, win=0, loss=1, highest_achievement="AFC West Champions"),
#     Postseason(team_id=4, year=2013, win=1, loss=1, highest_achievement="AFC Wild Card Winners"),
#     Postseason(team_id=4, year=2018, win=1, loss=1, highest_achievement="AFC Wild Card Winners"),
#
#     SuperBowl(team_id=4, year=1994, super_bowl_number="XXIX", win_loss="L", score="San Francisco 49ers: 49, San Diego Chargers: 26")
# ]

#
# session.add_all(data)
# session.commit()
# session.close()
# engine.dispose()


# # Populating RegularSeason table with data from csv files
# connection = sqlite3.connect("site.db")
# cursor = connection.cursor()
#
#
# all_data = []
#
# denver_broncos_data = []
# with open("denver_broncos_reg.csv", newline="") as file:
#     for row in csv.reader(file):
#         denver_broncos_data.append(row)
#     all_data.append(denver_broncos_data)
#
# kansas_city_chiefs_data = []
# with open("kansas_city_chiefs_reg.csv", newline="") as file:
#     for row in csv.reader(file):
#         kansas_city_chiefs_data.append(row)
#     all_data.append(kansas_city_chiefs_data)
#
# las_vegas_raiders_data = []
# with open("las_vegas_raiders_reg.csv", newline="") as file:
#     for row in csv.reader(file):
#         las_vegas_raiders_data.append(row)
#     all_data.append(las_vegas_raiders_data)
#
# los_angeles_chargers_data = []
# with open("los_angeles_chargers_reg.csv", newline="") as file:
#     for row in csv.reader(file):
#         los_angeles_chargers_data.append(row)
#     all_data.append(los_angeles_chargers_data)
#
#
# query = (
#     """
#     INSERT INTO regular_season (
#     team_id,
#     year,
#     place,
#     win,
#     loss,
#     tie)
#     VALUES (?, ?, ?, ?, ?, ?);
#     """
# )
#
# for team_data in all_data:
#     cursor.executemany(query, team_data)
#     connection.commit()

# # Delete all rows in a table
# session.query(Team).delete()
# session.commit()

# # Delete a row by id
# SuperBowl.query.filter_by(id=36).delete()
# db.session.commit()

# Update data
# update = Postseason.query.get(43)
# update.year = "2018"
# db.session.commit()

# count = Postseason.query.filter_by(highest_achievement="hi").all()
# print(count)
# count[0].highest_achievement = "First Place, altered AFC"
# db.session.commit()
