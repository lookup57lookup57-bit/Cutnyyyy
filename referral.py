def get_ref(payload):
    if payload and payload.startswith("ref_"):
        return int(payload.replace("ref_", ""))
    return None