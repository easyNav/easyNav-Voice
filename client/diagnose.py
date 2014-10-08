#!/usr/bin/env python2
import time
import re
import socket
import os
from subprocess import check_output, call


class Diagnostics:

    """
    Set of diagnostics to be run for determining the health of the
    host running Jasper

    To add new checks, add a boolean returning method with a name that starts
    with `check_`
    """
    @classmethod
    def jasper_modules_path(cls):
        return os.path.abspath('../../')

    @classmethod
    def check_network_connection(cls):
        try:
            # see if we can resolve the host name -- tells us if there is
            # a DNS listening
            host = socket.gethostbyname("www.google.com")
            # connect to the host -- tells us if the host is actually
            # reachable
            socket.create_connection((host, 80), 2)
        except Exception:
            return False
        else:
            return True

    @classmethod
    def check_phonetisaurus_dictionary_file(cls):
        return os.path.isfile(os.path.join(cls.jasper_modules_path(), "phonetisaurus/g014b2b.fst"))

    @classmethod
    def check_phonetisaurus_program(cls):
        return call(['which', 'phonetisaurus-g2p']) == 0

    @classmethod
    def info_git_revision(cls):
        return check_output(['git', 'rev-parse', 'HEAD'])


class DiagnosticRunner:

    """
    Performs a series of checks against the system, printing the results to the
    console and also saving them to diagnostic.log
    """

    def __init__(self, diagnostics):
        self.diagnostics = diagnostics

    def run(self):
        self.initialize_log()
        self.perform_checks()

    def perform_checks(self):
        self.failed_checks = 0
        for check in self.select_methods('check'):
            self.do_check(check)
        for info in self.select_methods('info'):
            self.get_info(info)
        if self.failed_checks == 0:
            self.log("All checks passed\n")
        else:
            self.log("%d checks failed\n" % self.failed_checks)

    def select_methods(self, prefix):
        def is_match(method_name):
            return callable(getattr(self.diagnostics, method_name)) and re.match(r"\A" + prefix + "_", method_name)

        return [method_name for method_name in dir(self.diagnostics) if is_match(method_name)]

    def initialize_log(self):
        self.output = open('diagnostic.log', 'w')
        self.log("Starting jasper diagnostic\n")
        self.log(time.strftime("%c") + "\n")

    def log(self, msg):
        print msg,
        self.output.write(msg)

    def get_info(self, info_name):
        message = info_name.replace("info_", "").replace("_", " ")
        info_method = getattr(self.diagnostics, info_name)
        info = info_method()
        self.log("%s: %s" % (message, info))

    def do_check(self, check_name):
        message = check_name.replace("check_", "").replace("_", " ")
        check = getattr(self.diagnostics, check_name)
        self.log("Checking %s... " % message)
        if check():
            self.log("OK")
        else:
            self.failed_checks += 1
            self.log("FAILED")
        self.log("\n")


if __name__ == '__main__':
    DiagnosticRunner(Diagnostics).run()
