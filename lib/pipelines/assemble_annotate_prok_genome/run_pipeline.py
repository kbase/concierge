import logging

logger = logging.getLogger("pipeline")

from lib.pipelines.ConciergeConstants import ConciergeParams
from lib.pipelines.Pipeline import NarrativeCellInfo, Pipeline

# TODO Get Tag and Version of App
wsid = 48739
project_directory = "some_dir"
pipeline = Pipeline()

def run_fast_qc(reads_ref, fast_qc_cell_id=None):
    """
    #TODO CHeckpoint if this job already ran, and skip it..
    Run fastqc on an assembly using default params
    :param reads:
    :return:
    """
    tag = "release"
    narrative_cell_info = NarrativeCellInfo(tag=tag, cell_id=fast_qc_cell_id)

    fastqc_params = {"input_file_ref": reads_ref}
    # for item in narrative_cell_info:
    # fastqc_params.

    fastqc_params = {"base_number": "105"}
    runjob_params = {
        "method": "kb_fastqc/runFastQC",
        "params": [fastqc_params],
        "service_ver": tag,
        "wsid": wsid,
        "app_id": "simpleapp",
    }

    concierge_params = ConciergeParams(
        request_cpus=1, request_memory=1000, request_disk=10000
    )
    job_id = pipeline.ee2.run_job_concierge(
        params=runjob_params, concierge_params=concierge_params
    )

    job_output = Pipeline.wait_on_submitted_job(job_id=job_id)
    if job_output.completed_successfully:
        # TODO Some Checkpoint Thing if Job succeeds
        return job_output.checkjob_output.get('job_output')
    else:
        raise Exception



if __name__ == "__main__":
    # Run FastQC
    reads_ref = "20498/2/1"
    fast_qc_cell_id = "TODO"
    fast_qc_report = run_fast_qc(reads_ref, fast_qc_cell_id)
