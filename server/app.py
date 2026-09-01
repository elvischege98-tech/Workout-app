from flask import Flask, make_response,jsonify,request
from flask_migrate import Migrate  # type: ignore

from models import db, Exercise, Workout, WorkoutExercise
from schemas import ExerciseSchema, WorkoutSchema, WorkoutExerciseSchema

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)

db.init_app(app)

exercise_schema = ExerciseSchema()
exercises_schema = ExerciseSchema(many=True)

workout_schema = WorkoutSchema()
workouts_schema = WorkoutSchema(many=True)

workout_exercise_schema = WorkoutExerciseSchema()
workout_exercises_schema = WorkoutExerciseSchema(many=True)

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

#Get all exercises for a specific workout
@app.route("/exercises", methods=["POST"])
def create_exercise():
    data = request.get_json()

    if not data:
        return jsonify({"error": "Invalid input"}), 400

    required_fields = ["name", "category", "equipment_needed"]

    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"Missing field: {field}"}), 400

    exercise = Exercise(
        name=data["name"],
        category=data["category"],
        equipment_needed=data["equipment_needed"]
    )

    db.session.add(exercise)
    db.session.commit()

    return jsonify({
        "id": exercise.id,
        "name": exercise.name,
        "category": exercise.category,
        "equipment_needed": exercise.equipment_needed
    }), 201

#Patching
@app.route("/exercises/<int:id>", methods=["PATCH"])
def update_exercise(id):
    exercise = db.session.get(Exercise, id)

    if not exercise:
        return jsonify({"error": "Exercise not found"}), 404

    data = request.get_json()

    if not data:
        return jsonify({"error": "Invalid input"}), 400

    try:
        if "name" in data:
            exercise.name = data["name"]

        if "category" in data:
            exercise.category = data["category"]

        if "equipment_needed" in data:
            exercise.equipment_needed = data["equipment_needed"]

        db.session.commit()

        return jsonify({
            "id": exercise.id,
            "name": exercise.name,
            "category": exercise.category,
            "equipment_needed": exercise.equipment_needed
        }), 200

    except ValueError as error:
        db.session.rollback()
        return jsonify({"error": str(error)}), 400

    
# DELETE a workout exercise
@app.route("/workout-exercises/<int:id>", methods=["DELETE"])
def delete_workout_exercise(id):
    item = db.session.get(WorkoutExercise, id)

    if not item:
        return jsonify({"error": "Workout exercise not found"}), 404

    db.session.delete(item)
    db.session.commit()

    return jsonify({
        "message": "Workout exercise deleted successfully"
    }), 200



if __name__ == '__main__':
    app.run(port=5555, debug=True)
