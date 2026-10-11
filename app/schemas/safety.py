from pydantic import BaseModel, ConfigDict


class SafetyCheckResult(BaseModel):
    model_config = ConfigDict(extra="forbid")

    is_trolling: bool
    is_compliance: bool
    prompt_injection: bool