class GameStats():
    #Track statistics for Aliens Invasion

    def __init__(self,ai_settings):
        #initilize statistics for Alien Invasion

        self.ai_settings = ai_settings
        self.reset_stats()


    
    def reset_stats(self):
        #initilze statistics that can change during the game
        self.ships_left = self.ai_settings.ship_limit