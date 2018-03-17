class HighScoreTable:
    
    def __init__(self, limit):
        self.limit = limit
        self.scores = []
    
    def update(self, score):
        
        if len(self.scores) > 0:
        	min_value = min(self.scores)

        if self.limit == len(self.scores) and min_value < score:
        	self.scores.remove(min(self.scores))
        	self.scores.append(score)
        	self.scores.sort(reverse=True)

        if self.limit > len(self.scores):
        	self.scores.append(score)
        	self.scores.sort(reverse=True)
    
    def reset(self):
        self.scores.clear()