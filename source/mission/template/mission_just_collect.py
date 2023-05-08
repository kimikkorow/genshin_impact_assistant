from source.mission.mission_template import MissionExecutor

class MissionJustCollect(MissionExecutor):
    def __init__(self, filename, name):
        super().__init__(is_CFCF=True,is_PUO=True,is_TMCF=True)
        self.filename = filename
        self.setName(name)
    
    def exec_mission(self):
        self.start_pickup()# SweatFlower167910289922 SweatFlowerV2P120230507180640i0 
        self.move_along(self.filename, is_tp=True, is_precise_arrival=False)
        self.stop_pickup()
        # self.collect(MODE="AUTO",pickup_points=[[71, -2205],[65,-2230]])