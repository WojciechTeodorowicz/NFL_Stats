"""
authors: Wojciech Teodorowicz, Sahan Ekanayake-close enough :)

This file contains all the player stats conversion and data


"""
from flask import Flask
from flask import render_template
import os.path
import json

app = Flask(__name__)

#import the json file

_player_json_file = os.path.join(os.path.dirname(__file__), 'players.json')



"""def read_players(player_file=None):
    if player_file is None:
        player_file = _player_json_file
        try:
        """
data = json.loads(open(player_file).read())
except IOError:
    return {}
        
#make player dictionary
        
players = {}
        
        #get player ID from json file = data.
        
for playerID in data:
    players[playerID] = Player_data(data[playerID])
    return players
        
class Players_Data(object):
    
    @app.route("/run")
    def __init__(self, data):
        """
            Assign all the values from the json file to new variables
            the values are birth date age weight...

        """
        
        self.player_ID = data['gsis_id']
        self.gsis_name = data.get('gsis_name', '')
        self.player_fullname = data.get('full_name', '')
        self.player_first_name = data.get('first_name', '')
        self.player_last_name = data.get('last_name', '')
        self.player_weight = data.get('weight','')
        self.player_height = data.get('height' , '')
        self.player_birth = data.get('birthdate', '')
        self.player_pro_years = data.get('years_pro', '')
        self.player_team = data.get('data', '') 
        values = [player_ID,gsis_name,player_fullname,player_first_name,player_last_name,player_weight]
        return render_template('chart.html', players=json.loads(data.text)['00-0000045'])
         
        """
        Here we will need to think of a lagorithm to analyze the data we will use python
        and html for the display with chart.js
        """

    if __name__ == "__main__":
        app.run(host='localhost')
