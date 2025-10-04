import os
import json
from orchestrator.runner import SimulatorRunner

def test_simulated_run_creates_report(tmp_path, monkeypatch):
    # Use tmp_path as working directory so we don’t pollute repo folder
    cwd = os.getcwd()
    os.chdir(tmp_path)
    runner = SimulatorRunner(config_path="configs/default.yaml")
    runner.run()
    # After run, look for a report file in "artifacts" directory
    artifacts_dir = tmp_path / "artifacts"
    files = list(artifacts_dir.glob("report_*.json"))
    assert len(files) >= 1, "No report file found"
    # Load JSON and check expected fields
    data = json.loads(files[0].read_text())
    assert "summary" in data
    assert "artifacts" in data
    os.chdir(cwd)
