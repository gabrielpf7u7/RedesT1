# !/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime #usado para medir tiempo de validez del log, registrar entradas en log
from dns.py import * #para hacer llamado al comportamiento normal del resolver, sin considerar caché

max_time_s_inCache = 3600 #tiempo máximo de validez del caché
log_path = "log.txt" #ubicación del archivo


def cache_resolve(dn):

    response = None
    with open(log_path, 'r') as cache:
        #leer las lineas del log en orden inverso => desde la mas reciente
        for line in cache.readlines().reverse():
            if line == "":
                break
            elif line.split(";")[1] == dn:
                with datetime.datetime.strptime(line.split(";")[0],
                                                '%Y-%m-%D %H:%M:%S.%f')-datetime.datetime.now() as delta:
                    if delta.total_seconds() <= max_time_s_inCache:
                        response = line.split(";")[2]
    if response is None:
        response = dnsResolve(dn)
    with open(log_path,'a') as log:
        log.write(str(datetime.datetime.now())+";"+dn+";"+response+";\n")
    return response


