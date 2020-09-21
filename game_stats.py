with open("alltimehighscore.txt") as file_object:
    content=file_object.readlines()
highscore1='0'
for line in content:
    highscore1+=line
class Gamestats():
    """track statistics for the game"""
    def __init__(self,ai_settings):
        """Initialize statistics"""
        self.ai_settings=ai_settings
        #high score must not be reset
        self.reset_stats()
        #start alien Invasion
        self.game_active=False
        self.high_score=int(highscore1)
    def reset_stats(self):
        self.ships_left=self.ai_settings.ship_limit
        self.score=0
        self.level=1
