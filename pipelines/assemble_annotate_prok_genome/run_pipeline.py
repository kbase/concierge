import os
import time
from lib.installed_clients.execution_engine2Client import execution_engine2

ee2 = execution_engine2(url=os.environ.get("EE2_URL", "https://ci.kbase.us/services/ee2"),
                        token=os.environ.get("CONCIERGE_TOKEN"))


from lib.ConciergeConstants import ConciergeParams

def run_fast_qc(reads_ref, narrative_cell_info=None):
    """
    Run fastqc on an assembly using default params
    :param reads:
    :return:
    """
    fastqc_params = {'input_file_ref' : reads_ref}
    for item in narrative_cell_info:
        fastqc_params['item'] =

    concierge_params = ConciergeParams(request_cpus=1,request_memory=1000,request_disk=10000)
    job_id = ee2.run_job_concierge(params=fastqc_params,concierge_params=concierge_params)
    return job_id

def wait_on_job(job_id):
    while(True):
        time.sleep()
        status = ee2.check_job_canceled(job_id)
        if status

def get_output_file(job_id,output_file_key):



def run_fast_qc_app(r):
    fast_qc_job_id = run_fast_qc()
    wait_on_job(fast_qc_job_id)
    get_output_file(job_id=job_id,output_file_key='abc')


if __name__ == '__main__':
    reads_ref = '20498/2/1'
    fast_qc_report = run_fast_qc(reads_ref)
    fast_qc(reads)