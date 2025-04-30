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


# @app.route("/mutate", methods=["POST"])
# def mutate():
#     admission_review = request.get_json()
#     print("AdmissionReview Request:", json.dumps(admission_review))
#     uid = admission_review["request"].get("uid")
#
#     spec = request.json["request"]["object"]
#     modified_spec = copy.deepcopy(spec)
#
#     try:
#         modified_spec["metadata"]["labels"]["example.com/new-label"] = str(
#             random.randint(1, 1000)
#         )
#     except KeyError:
#         pass
#     patch = jsonpatch.JsonPatch.from_diff(spec, modified_spec)
#     return jsonify(
#         {
#             "response": {
#                 "allowed": True,
#                 "uid": request.json["request"]["uid"],
#                 "patch": base64.b64encode(str(patch).encode()).decode(),
#                 "patchtype": "JSONPatch",
#             }
#         }
#     )


@app.route("/health", methods=["GET"])
def health():
    return jsonify({
        'status': 'up'
    })

#
# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=8080, debug=True,ssl_context=('tls.key', 'tls.cert'))