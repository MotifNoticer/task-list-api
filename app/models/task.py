from app import db

class Task(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(120), nullable=False)
    completed_at = db.Column(db.DateTime, nullable=True, default=None)
    goal_id = db.Column(db.Integer, db.ForeignKey('goal.goal_id'), nullable=True)
    goal = db.relationship("Goal", back_populates="tasks")

    @classmethod
    def from_dict(cls, task_data):
    
        new_task = Task(
        title=task_data["title"],
        description=task_data["description"]
        )
        
        return new_task

    def to_dict(self):
        task_to_dict = {
                'id': self.id,
                'title': self.title,
                'description': self.description,
                'is_complete': bool(self.completed_at)
            }
        
        if self.goal_id:
            task_to_dict["goal_id"] = self.goal_id
        
        return task_to_dict
