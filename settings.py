class  Settings():

    """ a class for storing all settings for alien invasion """

    def __init__(self):
        """Initialize the game stats changing settings"""
        #screen settintgs
        self.screen_width = 1400
        self.screen_height = 750
        self.screenbackground_colour=(230,230,230)
        #ship settings
        self.ship_limit=2
        #bullet settings
        self.bullet_width=3
        self.bullet_height=15
        self.bullet_colour=(255,0,0)
        self.boss_bullet_width=3
        self.boss_bullet_height=15
        self.boss_bullet_colour=(0,0,255)
        self.bullets_allowed=10
        #how quickly the game speeds up
        self.speedup_scale=1.1
        #how quickly the alien score increases
        self.score_scale=1.5
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """settings at the time of initiation """
        self.ship_speed_factor=2
        self.bullet_speed_factor=1.5
        self.alien_speed_factor=1.5
        self.alien_drop_speed=10
        self.boss_alien_speed_factor=3
        #fleet direction equals to 1 means right and -1 means left
        self.fleet_direction=1

        #scoring
        self.alien_score=25
        self.boss_alien_score=5000

    def increase_speed(self):
        """increase speed of settings and alien score values"""
        self.ship_speed_factor*=self.speedup_scale
        self.bullet_speed_factor*=self.speedup_scale
        self.alien_speed_factor*=self.speedup_scale
        self.alien_score=int(self.alien_score*self.score_scale)
