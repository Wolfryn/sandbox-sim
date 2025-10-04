from orchestrator.mocks import VMMock, PCAPMock
from analyzer.report import ReportGenerator
import os
import uuid

class SimulatorRunner:
    def __init__(self, config_path):
        self.config_path = config_path

    def run(self):
        print("[sim] Loading config:", self.config_path)
        vm = VMMock("win10-golden")
        vm.boot()
        print("[sim] Executing benign payload (mock mode).")
        vm.execute_benign("tools/sample_payloads/benign_test.py")
        artifacts = {
            "procmon": vm.dump_procmon(),
            "memory": vm.dump_memory_snapshot(),
            "pcap": PCAPMock().generate()
        }
        outdir = "artifacts"
        os.makedirs(outdir, exist_ok=True)
        report = ReportGenerator(artifacts)
        report_path = os.path.join(outdir, f"report_{uuid.uuid4().hex}.json")
        report.save(report_path)
        print("[sim] Report saved at:", report_path)

class LiveGuard:
    @staticmethod
    def ensure_authorized():
        # Always block live mode in this repo
        raise RuntimeError("Live mode is disabled in this repository. Use --simulate.")
