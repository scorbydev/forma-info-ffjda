import sys
from pathlib import Path

import pytest


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.license_rules import compute_license_status  # noqa: E402


def test_active_license_when_all_rules_ok():
    assert (
        compute_license_status("2025/2026", "2025/2026", "PAID", True)
        == "ACTIVE"
    )


def test_pending_payment_has_priority_in_current_season():
    assert (
        compute_license_status("2025/2026", "2025/2026", "PENDING", True)
        == "PENDING_PAYMENT"
    )


def test_pending_certificate_in_current_season():
    assert (
        compute_license_status("2025/2026", "2025/2026", "PAID", False)
        == "PENDING_CERTIFICATE"
    )


def test_pending_mutation_in_current_season():
    assert (
        compute_license_status("2025/2026", "2025/2026", "PAID", True, True)
        == "PENDING_MUTATION"
    )


def test_expired_season_when_no_other_blocker():
    assert (
        compute_license_status("2024/2025", "2025/2026", "PAID", True)
        == "EXPIRED_SEASON"
    )


@pytest.mark.xfail(reason="Bug pedagogique: l'ordre metier doit etre corrige en atelier.")
def test_payment_priority_before_expired_season_after_fix():
    assert (
        compute_license_status("2024/2025", "2025/2026", "PENDING", True)
        == "PENDING_PAYMENT"
    )

