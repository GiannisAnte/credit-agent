import pytest
from pydantic import ValidationError

from app.schemas.intent import ExtractedIntent


def test_valid_extracted_intent() -> None:
    intent = ExtractedIntent(
        business_goal="развитие бизнеса",
        requested_amount=2_000_000,
    )

    assert intent.business_goal == "развитие бизнеса"
    assert intent.requested_amount == 2_000_000


def test_amount_must_be_positive() -> None:
    with pytest.raises(ValidationError):
        ExtractedIntent(requested_amount=0)


def test_unknown_fields_are_rejected() -> None:
    with pytest.raises(ValidationError):
        ExtractedIntent(unexpected_field="value")


def test_missing_parameters_are_allowed() -> None:
    intent = ExtractedIntent(
        business_goal=None,
        requested_amount=None,
        clarification_field="business_goal",
    )

    assert intent.business_goal is None
    assert intent.requested_amount is None
    assert intent.clarification_field == "business_goal"
