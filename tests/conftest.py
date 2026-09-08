"""Windows OCP teardown guard.

OCP 7.9 may fault after pytest has completed successfully while native CAD
objects are destroyed. Flush the finished report and leave with pytest's code.
"""
import os
import sys


def pytest_sessionfinish(session, exitstatus):
    sys.stdout.flush(); sys.stderr.flush()
    os._exit(exitstatus)
