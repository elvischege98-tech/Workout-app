from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates

db = SQLAlchemy()

class Exercise(db.Model):
    __tablename__ = 'exercises'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(100), nullable=False)
    equipment_needed = db.Column(db.Boolean, nullable=False)

    workout_exercises = db.relationship(
    "WorkoutExercise",
    back_populates="exercise",
    cascade="all, delete-orphan"
)    

@validates('name')
def validate_name(self, key, name):
    if not name:
        raise ValueError("Exercise name cannot be empty.")
    return name    

class Workout(db.Model):
    __tablename__ = "workouts"

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    duration_minutes = db.Column(db.Integer, nullable=False)
    notes = db.Column(db.Text)

    ___table_args__ = (
        db.CheckConstraint(duration_minutes > 0, name='check_duration_positive'),
    )

    workout_exercises = db.relationship(
        "WorkoutExercise",
        back_populates="workout",
        cascade="all, delete-orphan"
    )

@validates('duration_minutes')
def validate_duration_minutes(self, key, duration_minutes):
    if duration_minutes <= 0:
        raise ValueError("Workout duration must be a positive integer.")
    return duration_minutes    

class WorkoutExercise(db.Model):
    __tablename__ = 'workout_exercises'

    id = db.Column(db.Integer, primary_key=True)
    workout_id = db.Column(db.Integer, db.ForeignKey('workouts.id'), nullable=False)
    reps= db.Column(db.Integer)
    exercise_id = db.Column(db.Integer, db.ForeignKey('exercises.id'), nullable=False)
    sets = db.Column(db.Integer)
    duration_seconds = db.Column(db.Integer)

    __table_args__ = (
        db.CheckConstraint(reps >= 0, name='check_reps_non_negative'),
        db.CheckConstraint(sets >= 0, name='check_sets_non_negative'),
        db.CheckConstraint(duration_seconds >= 0, name='check_duration_non_negative'),
    ) 

    workout=db.relationship(
    "Workout",
    back_populates="workout_exercises"
    )

    exercise=db.relationship(
    "Exercise",
    back_populates="workout_exercises"
    )

@validates('reps', 'sets', 'duration_seconds')
def validate_non_negative(self, key, value):
    if value is not None and value < 0:
        raise ValueError(f"{key} must be a non-negative integer.")
    return value    
