#!/usr/bin/env python3
import argparse
import sys
from orchestrator.runner import SimulatorRunner, LiveGuard

def parse_args():
    p = argparse.ArgumentParser()
    p.add_argument("--simulate", action="store_true", help="Run in simulated (safe) mode")
    p.add_argument("--config", default="configs/default.yaml", help="Path to config file")
    return p.parse_args()

def main():
    args = parse_args()
    if args.simulate:
        runner = SimulatorRunner(args.config)
        runner.run()
        print("[main] Simulated run completed.")
        sys.exit(0)
    else:
        LiveGuard.ensure_authorized()
        print("Live mode disabled in this repository. See docs/runbook.md.")
        sys.exit(2)

if __name__ == "__main__":
    main()
