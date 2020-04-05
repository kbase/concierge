import logging
import os
import time
import uuid
from typing import NamedTuple, Dict

from lib.installed_clients.execution_engine2Client import execution_engine2
from lib.pipelines.ConciergeConstants import Status, ONE_WEEK


class CompletedOutput(NamedTuple):
    completed_successfully: bool
    checkjob_output: Dict


class NarrativeCellInfo(NamedTuple):
    tag: str
    cell_id: str
    job_uid: uuid.UUID = uuid.uuid4()
    token_uid: uuid.UUID = uuid.uuid4()


class Pipeline:
    def __init__(self):
        self.concierge_token = os.environ["CONCIERGE_TOKEN"]
        self.ee2_url = os.environ.get("EE2_URL", "https://ci.kbase.us/services/ee2")
        self.ee2 = execution_engine2(url=self.ee2_url, token=self.concierge_token)
        self.logger = logging.getLogger("pipeline")

    def wait_on_submitted_job(self, job_id, timeout_seconds=ONE_WEEK):
        timeout = time.time() + timeout_seconds
        while True:
            if time.time() > timeout:
                raise TimeoutError(f"Job didn't finish after {timeout}")
            check_job = self.ee2.check_job({"job_id": job_id})
            status = Status(check_job.get("status"))
            if status in [
                Status.created,
                Status.estimating,
                Status.running,
                Status.queued,
            ]:
                time.sleep(2)
            else:
                if status is Status.completed:
                    return CompletedOutput(
                        completed_successfully=True, checkjob_output=check_job
                    )
                if status in [Status.error, Status.terminated]:
                    return CompletedOutput(
                        completed_successfully=False, checkjob_output=check_job
                    )
