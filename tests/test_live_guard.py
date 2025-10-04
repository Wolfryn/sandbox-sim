import pytest
from orchestrator.runner import LiveGuard

def test_live_guard_raises():
    with pytest.raises(RuntimeError):
        LiveGuard.ensure_authorized()
