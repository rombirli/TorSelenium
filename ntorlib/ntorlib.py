import subprocess
from pathlib import Path
from os import makedirs
from shutil import copytree, rmtree

# !! ntorlib has its own config !!
socks_port_start = 3210
httptunel_start_port = 9051
lib_name='ntorlib'
temp_data = fr'{lib_name}\res\temp'  # a directory : where to store temp Data directories (proxy port modified)
orig_data = fr'{lib_name}\res\Data'  # a directory : where to get original Data directory (proxy port not modified)
tor_exe = fr'{lib_name}\res\tor.exe'  # a file : where is tor.exe


def path_torcc(i: int): return fr'{temp_data}\torcc{i}'


def path_data_dir(i: int): return fr'{temp_data}\Data{i}'


def get_proxy(i: int): return f'127.0.0.1:{httptunel_start_port + i}'


def create_n_dependencies(n) -> None:
    """
    Create all dependencies to run n instances of tor
    See the what are modif_data orig_data tor_exe. All those files & directories must exist
    :param n: how many tor instance of tor will you be able to run simultaneously
    :return:None
    """

    def check_torcc(i: int) -> bool:
        return Path(path_torcc(i)).exists() and Path(path_torcc(i)).is_file()

    def check_data_dir(i: int) -> bool:
        return Path(path_data_dir(i)).exists() and Path(path_data_dir(i)).is_dir()

    def create_torcc(i: int):
        with open(path_torcc(i), 'w+') as file:
            file.write(
                f"""
        SocksListenAddress 127.0.0.1:{httptunel_start_port + i}
        HTTPTunnelPort {httptunel_start_port + i}
        SocksPort {socks_port_start + i}
                """
            )

    def create_data_dir(i: int):
        copytree(orig_data, f'{temp_data}/Data{i}')

    for i in range(n):
        if not check_torcc(i): create_torcc(i)
        if not check_data_dir(i): create_data_dir(i)


def run_n_tor(n):
    """
    Run n tor instances into n threads. You must create dependencies before calling this function
    You can't call this function again without killing those threads.
    Otherwise those tor sessions will have the same proxy port as already running sessions and will crash.
    :param n: How many instances of tor to run
    :return: tor threads as a List[Popen[Str]]
    """

    def get_tor_launch_line(i: int): return [f'{tor_exe}', '-f', path_torcc(i), '--DataDirectory', path_data_dir(i)]

    return [subprocess.Popen(get_tor_launch_line(i), stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT) for i in
            range(n)]


def clean_dependencies():
    """
    Clean modif_data.
    You can choose to call it or not. If you don't, the existing datas will not be overwritten when calling create_n_dependencies
    :return: None
    """
    rmtree(temp_data)
    makedirs(temp_data)
