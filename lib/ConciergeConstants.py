from dataclasses import dataclass
from typing import Optional

KBASE_CONCIERGE_USERNAME = "kbaseconcierge"
CONCIERGE_CLIENTGROUP = "kbase_concierge"


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


@dataclass()
class