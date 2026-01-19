from core.auth import login
from core.api_client import get_call, put_call

def disable_virtual_service():
    print("Test started")

    token = login()
    print("Token received")

    # Pre-Fetch
    vs_data = get_call("/api/virtualservice", token)
    vs_list = vs_data["results"]
    print("Total Virtual Services:", len(vs_list))

    # Pre-Validation
    target_vs = None
    for vs in vs_list:
        if vs["name"] == "backend-vs-t1r_1000-1":
            target_vs = vs
            break

    if not target_vs:
        print("Target VS not found")
        return

    uuid = target_vs["uuid"]
    print("Target VS UUID:", uuid)
    print("Pre-validation enabled:", target_vs["enabled"])

    # Task / Trigger
    put_call(f"/api/virtualservice/{uuid}", token, {"enabled": False})
    print("Virtual Service disabled")

    # Post-Validation
    final_status = get_call(f"/api/virtualservice/{uuid}", token)
    print("Post-validation enabled:", final_status["enabled"])
