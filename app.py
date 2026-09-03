from flask import Flask, jsonify, request

app = Flask(__name__)

# =====================================================
# PATIENT DATA
# =====================================================

patients = []


def save_patient(data):
    patient = {
        "id": len(patients) + 1,
        **data
    }

    patients.append(patient)
    return patient


def get_patients():
    return patients


def get_patient_by_id(patient_id):
    for patient in patients:
        if patient["id"] == int(patient_id):
            return patient

    return None


def update_patient_by_id(patient_id, data):
    for index, patient in enumerate(patients):
        if patient["id"] == int(patient_id):
            patients[index] = {
                **patient,
                **data
            }

            return patients[index]

    return None


def delete_patient_by_id(patient_id):
    for index, patient in enumerate(patients):
        if patient["id"] == int(patient_id):
            return patients.pop(index)

    return None


# =====================================================
# PATIENT HANDLERS
# =====================================================

def list_patients():
    return jsonify({
        "status": 200,
        "data": get_patients()
    }), 200


def show_patient(patient_id):
    patient = get_patient_by_id(patient_id)

    if patient is None:
        return jsonify({
            "status": 404,
            "error": "Patient not found"
        }), 404

    return jsonify({
        "status": 200,
        "data": patient
    }), 200


def create_patient():
    data = request.get_json() or {}
    patient = save_patient(data)

    return jsonify({
        "status": 201,
        "data": patient
    }), 201


def update_patient(patient_id):
    data = request.get_json() or {}
    patient = update_patient_by_id(patient_id, data)

    if patient is None:
        return jsonify({
            "status": 404,
            "error": "Patient not found"
        }), 404

    return jsonify({
        "status": 200,
        "data": patient
    }), 200


def delete_patient(patient_id):
    patient = delete_patient_by_id(patient_id)

    if patient is None:
        return jsonify({
            "status": 404,
            "error": "Patient not found"
        }), 404

    return jsonify({
        "status": 200,
        "data": patient
    }), 200


# =====================================================
# PATIENT ROUTES
# =====================================================

@app.route("/patients", methods=["GET"])
def patient_list_route():
    return list_patients()


@app.route("/patients/<int:patient_id>", methods=["GET"])
def patient_show_route(patient_id):
    return show_patient(patient_id)


@app.route("/patients", methods=["POST"])
def patient_create_route():
    return create_patient()


@app.route("/patients/<int:patient_id>", methods=["PUT"])
def patient_update_route(patient_id):
    return update_patient(patient_id)


@app.route("/patients/<int:patient_id>", methods=["DELETE"])
def patient_delete_route(patient_id):
    return delete_patient(patient_id)


# =====================================================
# APPOINTMENT ROUTES
# =====================================================

@app.route("/appointments", methods=["GET"])
def list_appointments():
    return jsonify({
        "status": 200,
        "data": []
    }), 200


@app.route("/appointments/<int:appointment_id>", methods=["GET"])
def show_appointment(appointment_id):
    return jsonify({
        "status": 200,
        "data": {
            "id": appointment_id
        }
    }), 200


@app.route("/appointments", methods=["POST"])
def create_appointment():
    data = request.get_json() or {}

    return jsonify({
        "status": 201,
        "data": data
    }), 201


@app.route("/appointments/<int:appointment_id>", methods=["PUT"])
def update_appointment(appointment_id):
    data = request.get_json() or {}

    return jsonify({
        "status": 200,
        "data": {
            "id": appointment_id,
            **data
        }
    }), 200


@app.route("/appointments/<int:appointment_id>", methods=["DELETE"])
def delete_appointment(appointment_id):
    return jsonify({
        "status": 200,
        "data": {
            "id": appointment_id
        }
    }), 200


# =====================================================
# MEDICAL RECORDS ROUTES
# =====================================================

@app.route("/medical-records", methods=["GET"])
def list_medical_records():
    return jsonify({
        "status": 200,
        "data": []
    }), 200


@app.route("/medical-records/<int:record_id>", methods=["GET"])
def show_medical_record(record_id):
    return jsonify({
        "status": 200,
        "data": {
            "id": record_id
        }
    }), 200


@app.route("/medical-records", methods=["POST"])
def create_medical_record():
    data = request.get_json() or {}

    return jsonify({
        "status": 201,
        "data": data
    }), 201


@app.route("/medical-records/<int:record_id>", methods=["PUT"])
def update_medical_record(record_id):
    data = request.get_json() or {}

    return jsonify({
        "status": 200,
        "data": {
            "id": record_id,
            **data
        }
    }), 200


@app.route("/medical-records/<int:record_id>", methods=["DELETE"])
def delete_medical_record(record_id):
    return jsonify({
        "status": 200,
        "data": {
            "id": record_id
        }
    }), 200


# =====================================================
# HEALTH SERVICES ROUTES
# =====================================================

@app.route("/health-services", methods=["GET"])
def list_health_services():
    return jsonify({
        "status": 200,
        "data": []
    }), 200


@app.route("/health-services/<int:service_id>", methods=["GET"])
def show_health_service(service_id):
    return jsonify({
        "status": 200,
        "data": {
            "id": service_id
        }
    }), 200


@app.route("/health-services", methods=["POST"])
def create_health_service():
    data = request.get_json() or {}

    return jsonify({
        "status": 201,
        "data": data
    }), 201


@app.route("/health-services/<int:service_id>", methods=["PUT"])
def update_health_service(service_id):
    data = request.get_json() or {}

    return jsonify({
        "status": 200,
        "data": {
            "id": service_id,
            **data
        }
    }), 200


@app.route("/health-services/<int:service_id>", methods=["DELETE"])
def delete_health_service(service_id):
    return jsonify({
        "status": 200,
        "data": {
            "id": service_id
        }
    }), 200


# =====================================================
# USER MANAGEMENT ROUTES
# =====================================================

@app.route("/users", methods=["GET"])
def list_users():
    return jsonify({
        "status": 200,
        "data": []
    }), 200


@app.route("/users/<int:user_id>", methods=["GET"])
def show_user(user_id):
    return jsonify({
        "status": 200,
        "data": {
            "id": user_id
        }
    }), 200


@app.route("/users", methods=["POST"])
def create_user():
    data = request.get_json() or {}

    return jsonify({
        "status": 201,
        "data": data
    }), 201


@app.route("/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    data = request.get_json() or {}

    return jsonify({
        "status": 200,
        "data": {
            "id": user_id,
            **data
        }
    }), 200


@app.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    return jsonify({
        "status": 200,
        "data": {
            "id": user_id
        }
    }), 200


# =====================================================
# START FLASK
# =====================================================

if __name__ == "__main__":
    app.run(debug=True)
