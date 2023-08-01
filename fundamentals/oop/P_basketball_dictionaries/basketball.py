class Player:
    # BONUS PART 1
    player_list = []

    # CHALLENGE 1
    def __init__(self, player):
        self.name = player["name"]
        self.age = player["age"]
        self.position = player["position"]
        self.team = player["team"]

    # BONUS PART 2
    @classmethod
    def get_teams(cls, team_list):
        for player in team_list:
            cls.player_list.append(Player(player))

    # DISPLAY BONUS LIST
    @classmethod
    def display_player_list(cls):
        for player in cls.player_list:
            print(
                f"<Name: {player.name}\nAge: {player.age}\nPosition: {player.position}\nTeam: {player.team}>"
            )


kevin = {
    "name": "Kevin Durant",
    "age": 34,
    "position": "small forward",
    "team": "Brooklyn Nets",
}
jason = {
    "name": "Jason Tatum",
    "age": 24,
    "position": "small forward",
    "team": "Boston Celtics",
}
kyrie = {
    "name": "Kyrie Irving",
    "age": 32,
    "position": "Point Guard",
    "team": "Brooklyn Nets",
}

# CHALLENGE 2
player_kevin = Player(kevin)
player_jason = Player(jason)
player_kyrie = Player(kyrie)

players = [
    {
        "name": "Kevin Durant",
        "age": 34,
        "position": "small forward",
        "team": "Brooklyn Nets",
    },
    {
        "name": "Jason Tatum",
        "age": 24,
        "position": "small forward",
        "team": "Boston Celtics",
    },
    {
        "name": "Kyrie Irving",
        "age": 32,
        "position": "Point Guard",
        "team": "Brooklyn Nets",
    },
    {
        "name": "Damian Lillard",
        "age": 33,
        "position": "Point Guard",
        "team": "Portland Trailblazers",
    },
    {
        "name": "Joel Embiid",
        "age": 32,
        "position": "Power Foward",
        "team": "Philidelphia 76ers",
    },
    {
        "name": "DeMar DeRozan",
        "age": 32,
        "position": "Shooting Guard",
        "team": "Chicago Bulls",
    },
]

# CHALLENGE 3
new_team = []
for player in players:
    new_team.append(Player(player))

# BONUS PART 3
Player.get_teams(players)

# DISPLAY BONUS LIST
Player.display_player_list()
