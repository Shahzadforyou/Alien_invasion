class Setting():
    #A class to Store seeting for game
    def __init__(self):
        self.width = 1200
        self.length = 700
        self.screen_height = self.length
        self.screen_width = self.width
        # self.bg_color = (230,230,230)
        self.bg_color = (10, 10, 30)      
        self.gradient_bottom = (60, 10, 0)
        self.ship_speed = 1.5
        #Bullet Settings
        self.bullet_speed = 1.6
        self.bullet_width = 30
        self.bullet_height = 15
        self.bullet_color = (0, 255, 0)
        self.bullet_allowed = 10
        #alien setting
        self.alien_speed_factor = 1
        self.fleet_direction = 1
        self.fleet_drop_speed = 10

        self.ship_limit = 3

