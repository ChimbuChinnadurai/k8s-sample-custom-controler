import json
from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/validate/pods", methods=["POST"])
def validate():
    admission_review = request.get_json()
    uid = admission_review["request"].get("uid")
    print("AdmissionReview Request:", json.dumps(admission_review))

    allowed = True
    try:
        for container_spec in request.json["request"]["object"]["spec"]["containers"]:
            if "env" in container_spec:
                allowed = False
    except KeyError:
        pass
    return jsonify({"apiVersion": "admission.k8s.io/v1",
                    "kind": "AdmissionReview",
                    "response":
                        {"allowed": allowed,
                         "uid": uid,
                         "status": {"message": "env keys are prohibited"}
                         }
                    })


@app.route("/health", methods=["GET"])
def health():
    return jsonify({
        'status': 'up'
    })