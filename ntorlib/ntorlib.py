from subprocess import Popen, DEVNULL, STDOUT
from os import makedirs
from shutil import copytree, rmtree
from typing import List
from ntorlib.utils import *


def create_n_dependencies(n) -> None:
    """
    Create all dependencies to run n instances of tor
    See the what are modif_data orig_data tor_exe. All those files & directories must exist
    :param n: how many tor instance of tor will you be able to run simultaneously
    :return:None
    """

    def create_data_dir(i: int):
        copytree(orig_data, f'{temp_data}/Data{i}')

    for i in range(n):
        if not check_torcc(i): create_torcc(i)
        if not check_data_dir(i): create_data_dir(i)


def run_n_tor(n: int) -> List[Popen[str]]:
    """
    Run n tor instances into n threads. You must create dependencies before calling this function
    You can't call this function again without killing those threads.
    Otherwise those tor sessions will have the same proxy port as already running sessions and will crash.
    :param n: How many instances of tor to run
    :return: tor threads as a List[Popen[Str]]
    """
    return [run_1_tor(i) for i in range(n)]


def run_1_tor(i: int) -> Popen[str]:
    """
    Run 1 tor instances into 1 thread. You must create dependencies for n>i before calling this function for i
    You can't call this function again with the same i without killing this thread.
    Otherwise the new tor sessions will have the same proxy port as old session and will crash.
    :param i: which tor thread will you creat
    :return: tor threads as a Popen[Str]
    """
    return Popen(get_tor_launch_line(i), stdout=DEVNULL, stderr=STDOUT)


def get_proxy(i: int):
    """
    Once you have started tor instances those instances provides a proxy connection that your browser can bind to.
    You must call run_n_tor before calling it.
    :param i: for which instance of tor do you want the proxy
    :return: a proxy as a string in the form '127.0.0.1:9051'
    """
    return f'127.0.0.1:{httptunel_start_port + i}'


def clean_dependencies():
    """
    Clean modif_data.
    You can choose to call it or not. If you don't, the existing datas will not be overwritten when calling create_n_dependencies
    :return: None
    """
    rmtree(temp_data)
    makedirs(temp_data)

