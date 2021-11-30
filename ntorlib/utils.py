from ntorlib.config import *
from pathlib import Path


def path_torcc(i: int): return fr'{temp_data}\torcc{i}'


def path_data_dir(i: int): return fr'{temp_data}\Data{i}'


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


def get_tor_launch_line(i: int): return [tor_exe, '-f', path_torcc(i), '--DataDirectory', path_data_dir(i)]
