from store_results import store_results
from profilers.utils import get_sandbox
from profilers.posix_extra import PosixExtraProfiler
from profilers.posix_core import PosixCoreProfiler

## Entrace point - handlers for different environments

def lambda_handler(event, context):
    env = get_sandbox()
    
    # results = core_profiler()
    # results = PosixExtraProfiler.run()
    results = PosixCoreProfiler.run()
    
    results['sandbox'] = env

    #store_results(results)
    
    return results

def wrapper():
    """Helper for easily calling this from a command line locally.

    Example: `python -c 'import main; main.wrapper()' | jq '.'`
    """
    res = lambda_handler(None, None)
    # print json.dumps(res)
    return res
