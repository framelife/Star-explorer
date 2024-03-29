class Settings:
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 0, 0)
        #self.ship_speed_factor = 35
        #self.alien_speed_factor =10
        self.fleet_drop_speed = 30
        #self.fleet_direction = 1
        #self.bullet_speed_factor = 20
        self.bullet_width = 1200
        self.bullet_height = 7
        self.bullet_color = 60,60,60
        self.bullets_allowed = 3
        self.ship_limit = 3
        self.speedup_scale = 1.1
        self.score_scale = 1.5
        self.alien_points = 50
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.ship_speed_factor = 35
        self.alien_speed_factor =10
        self.bullet_speed_factor = 20
        self.fleet_direction = 1

    def increase_speed(self):
        self.ship_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points *self.score_scale)
        #self.fleet_direction *= self.speedup_scale

