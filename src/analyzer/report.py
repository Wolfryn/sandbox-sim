import json
from datetime import datetime

class ReportGenerator:
    def __init__(self, artifacts):
        self.artifacts = artifacts

    def summarize(self):
        return {
            "timestamp_utc": datetime.utcnow().isoformat() + "Z",
            "artifacts": {k: len(v) if isinstance(v, str) else None for k, v in self.artifacts.items()},
            "notes": "This is a simulated run."
        }

    def save(self, path):
        report = {
            "summary": self.summarize(),
            "artifacts": self.artifacts
        }
        with open(path, "w") as fh:
            json.dump(report, fh, indent=2)
