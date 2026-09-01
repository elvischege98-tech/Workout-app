#!/usr/bin/env python3

from datetime import date

from app import app
from models import db, Exercise, Workout, WorkoutExercise


with app.app_context():

    # Clear existing data
    WorkoutExercise.query.delete()
    Workout.query.delete()
    Exercise.query.delete()

    # Create exercises
    exercise1 = Exercise(
        name="Push-ups",
        category="Strength",
        equipment_needed=False
    )

    exercise2 = Exercise(
        name="Squats",
        category="Strength",
        equipment_needed=False
    )

    exercise3 = Exercise(
        name="Bench Press",
        category="Strength",
        equipment_needed=True
    )

    exercise4 = Exercise(
        name="Running",
        category="Cardio",
        equipment_needed=False
    )

    db.session.add_all([
        exercise1,
        exercise2,
        exercise3,
        exercise4
    ])

    db.session.commit()

    # Create workouts
    workout1 = Workout(
        date=date(2026, 9, 1),
        duration_minutes=45,
        notes="Upper body workout"
    )

    workout2 = Workout(
        date=date(2026, 9, 2),
        duration_minutes=30,
        notes="Lower body workout"
    )

    db.session.add_all([
        workout1,
        workout2
    ])

    db.session.commit()

    # Connect exercises to workouts
    workout_exercise1 = WorkoutExercise(
        workout_id=workout1.id,
        exercise_id=exercise1.id,
        reps=10,
        sets=3,
        duration_seconds=0
    )

    workout_exercise2 = WorkoutExercise(
        workout_id=workout1.id,
        exercise_id=exercise3.id,
        reps=8,
        sets=3,
        duration_seconds=0
    )

    workout_exercise3 = WorkoutExercise(
        workout_id=workout2.id,
        exercise_id=exercise2.id,
        reps=12,
        sets=3,
        duration_seconds=0
    )

    workout_exercise4 = WorkoutExercise(
        workout_id=workout2.id,
        exercise_id=exercise4.id,
        reps=0,
        sets=1,
        duration_seconds=1200
    )

    db.session.add_all([
        workout_exercise1,
        workout_exercise2,
        workout_exercise3,
        workout_exercise4
    ])

    db.session.commit()

    print("Database seeded successfully!")