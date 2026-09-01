from marshmallow import fields, validate, validates_schema, ValidationError
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

from server.models import Exercise, Workout, WorkoutExercise
from server import *


class ExerciseSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Exercise
        load_instance = True

    id = fields.Int(dump_only=True)

    name = fields.Str(
        required=True,
        validate=validate.Length(min=2, max=100)
    )

    category = fields.Str(
        required=True,
        validate=validate.Length(min=2, max=50)
    )

    equipment_needed = fields.Bool(required=True)


class WorkoutSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Workout
        load_instance = True

    id = fields.Int(dump_only=True)

    date = fields.Date(required=True)

    duration_minutes = fields.Int(
        required=True,
        validate=validate.Range(min=1, max=1440)
    )

    notes = fields.Str(
        allow_none=True,
        validate=validate.Length(max=500)
    )


class WorkoutExerciseSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = WorkoutExercise
        load_instance = True

    id = fields.Int(dump_only=True)

    workout_id = fields.Int(required=True)

    exercise_id = fields.Int(required=True)

    reps = fields.Int(
        allow_none=True,
        validate=validate.Range(min=0)
    )

    sets = fields.Int(
        allow_none=True,
        validate=validate.Range(min=0)
    )

    duration_seconds = fields.Int(
        allow_none=True,
        validate=validate.Range(min=0)
    )

    @validates_schema
    def validate_workout_exercise(self, data, **kwargs):
        reps = data.get("reps")
        duration = data.get("duration_seconds")

        if reps is None and duration is None:
            raise ValidationError(
                "Either reps or duration_seconds must be provided."
            )