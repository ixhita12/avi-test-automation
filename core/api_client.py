def get_call(endpoint, token):
    print(f"MOCK GET CALL -> {endpoint}")

    # LIST virtual services
    if endpoint == "/api/virtualservice":
        return {
            "results": [
                {
                    "name": "backend-vs-t1r_1000-1",
                    "uuid": "vs-123",
                    "enabled": True
                }
            ]
        }

    # SINGLE virtual service
    if endpoint == "/api/virtualservice/vs-123":
        return {
            "enabled": False
        }

    return {}


def put_call(endpoint, token, payload):
    print(f"MOCK PUT CALL -> {endpoint} | payload={payload}")
    return {"status": "success"}
