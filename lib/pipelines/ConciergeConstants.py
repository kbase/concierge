from dataclasses import dataclass
from typing import Optional
from enum import Enum

KBASE_CONCIERGE_USERNAME = "kbaseconcierge"
CONCIERGE_CLIENTGROUP = "kbase_concierge"
ONE_WEEK = 604800


@dataclass()
class ConciergeParams:
    """ Set requested params. If you don't specify CG, its automatically set for you"""

    # Request cores. Will allow more cycles more if no other jobs are running
    request_cpus: int
    # Memory and Disk in MB
    request_memory: int
    request_disk: int
    # Job prio from 0-20
    job_priority: int = None
    # Default to kbaseconcierge
    account_group: str = None
    # ['machine=worker102','color=red']
    requirements_list: list = None
    # Default to kbase_concierge
    client_group: Optional[str] = CONCIERGE_CLIENTGROUP


class Status(Enum):
    """
    A job begins at created, then can either be estimating
    """

    created = "created"
    estimating = "estimating"
    queued = "queued"
    running = "running"
    # finished = "finished"  # Successful termination legacy code
    completed = "completed"  # Successful termination
    error = (
        "error"
    )  # Something went wrong and job failed # Possible Reasons are (ErrorCodes)
    terminated = (
        "terminated"
    )  # Canceled by user, admin, or script # Possible Reasons are (TerminatedCodes)
