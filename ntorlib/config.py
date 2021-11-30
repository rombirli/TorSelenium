socks_port_start = 3210
httptunel_start_port = 9051
lib_name='ntorlib'
temp_data = fr'{lib_name}\res\temp'  # a directory : where to store temp Data directories (proxy port modified)
orig_data = fr'{lib_name}\res\Data'  # a directory : where to get original Data directory (proxy port not modified)
tor_exe = fr'{lib_name}\res\tor.exe'  # a file : where is tor.exe