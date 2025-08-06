from pydantic import BaseModel
from typing import Optional, Dict, Any

class UserContext(BaseModel):
    name: Optional[str] = None
    is_premium_user: bool = False
    issue_type: Optional[str] = None  # e.g., "billing", "technical", "general"
    raw_message: Optional[str] = None
    metadata: Dict[str, Any] = {}
