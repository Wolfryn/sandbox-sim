import json
import time

class VMMock:
    def __init__(self, image_name):
        self.image_name = image_name
        self.procmon = []
        self.memory = {"processes": []}

    def boot(self):
        print(f"[vmmock] Booting VM {self.image_name}")
        time.sleep(0.1)

    def execute_benign(self, path):
        print(f"[vmmock] Mock executing: {path}")
        event = {
            "event": "process_create",
            "proc": path,
            "timestamp": time.time()
        }
        self.procmon.append(event)
        self.memory["processes"].append({"name": path, "pid": 4242})

    def dump_procmon(self):
        return json.dumps(self.procmon)

    def dump_memory_snapshot(self):
        return json.dumps(self.memory)

class PCAPMock:
    def generate(self):
        return json.dumps([{"src": "10.0.0.1", "dst": "10.0.0.2", "len": 60, "timestamp": time.time()}])
