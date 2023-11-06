

class CookingTutorial:
    """
    Represents a cooking tutorial.
    """
    
    def __init__(self, title, description, video_url):
        self.title = title
        self.description = description
        self.video_url = video_url
    
    def start_live_demo(self):
        """
        Initiates a live cooking demonstration.
        """
        # code for starting live cooking demos goes here.

class CookingTutorialResponse:
    """
    Represents the response from a cooking tutorial.
    """
    
    def __init__(self, success, message):
        self.success = success
        self.message = message
