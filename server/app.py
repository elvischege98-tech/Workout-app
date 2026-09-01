from flask import Flask, make_response,jsonify
from flask_migrate import Migrate

from models import *

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)

db.init_app(app)

# Define Routes here
@app.route("/exercises", methods=["GET"])
def get_exercises():
    exercises = Exercise.query.all()

    return jsonify([
        {
            "id": exercise.id,
            "name": exercise.name,
            "category": exercise.category,
            "equipment_needed": exercise.equipment_needed
        }
        for exercise in exercises
    ])


@app.route("/exercises/<int:id>", methods=["GET"])
def get_exercise(id):
    exercise = db.session.get(Exercise, id)

    if not exercise:
        return jsonify({"error": "Exercise not found"}), 404

    return jsonify({
        "id": exercise.id,
        "name": exercise.name,
        "category": exercise.category,
        "equipment_needed": exercise.equipment_needed
    })

@app.route("/workouts", methods=["GET"])
def get_workouts():
    workouts = Workout.query.all()

    return jsonify([
        {
            "id": workout.id,
            "date": workout.date.isoformat(),
            "duration_minutes": workout.duration_minutes,
            "notes": workout.notes
        }
        for workout in workouts
    ])

@app.route("/workouts/<int:id>", methods=["GET"])
def get_workout(id):
    workout = db.session.get(Workout, id)

    if not workout:
        return jsonify({"error": "Workout not found"}), 404

    return jsonify({
        "id": workout.id,
        "date": workout.date.isoformat(),
        "duration_minutes": workout.duration_minutes,
        "notes": workout.notes
    })

if __name__ == '__main__':
    app.run(port=5555, debug=True)
