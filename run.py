# ****************************************************************************
# Author:           Peter Jungers
# Program name:     AFC West Records
# Version:	        1.0
# Date:             September 2022
# Description:      Website that lists records for teams in the NFL's
#                   AFC West division.
# Notes:            This project served as an introduction to using Flask
#                   to create a website.
# Main resource     Corey Schafer's excellent Flask tutorial at
#                   https://www.youtube.com/playlist?list=PL-osiE80TeTs4UjLw5MM6OjgkjFeUxCYH
# ****************************************************************************

"""
This module runs the app.
"""

from afc_west_records import app


if __name__ == "__main__":
    app.run(debug=True)
