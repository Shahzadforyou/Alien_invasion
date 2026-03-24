class Setting():
    #A class to Store seeting for game
    def __init__(self):
        self.width = 1200
        self.length = 700
        # self.bg_color = (230,230,230)
        self.bg_color = (10, 10, 30)      
        self.gradient_bottom = (0, 0, 0)
        self.ship_speed = 1.5
        #Bullet Settings
        self.bullet_speed = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (0, 255, 0)
        self.bullet_allowed = 1
