#!/bin/python3
# connecting to a router using SSH and getting a response

import random
import string
import paramiko
import time

un = 'admin'
pw = 'r3d3m3ta####'
ip = input('Insira o IP: ')

#file = open('twomodebackup.txt', 'r')
#profile = input('Entre com o nome do profile: ')
#number = input('insira o numero de usuarios a serem gerados: ')
#filel = open(file, 'a')
#for i in range(int (number)):
#    username = ''.join(random.choice(string.ascii_letters + string.digits) for b in range(8))
#    password = ''.join(random.choice(string.ascii_letters + string.digits) for b in range(8))
#    filel.write('ppp secret add name=' + username +' password=' + password + ' profile=' + profile + ' service=pppoe\n')
#
#filel.close()

def ssh_backup_add(ip):
    try:
        session = paramiko.SSHClient()
        session.set_missing_host_key_policy(paramiko.AutoAddPolicy)
        session.connect(ip, username=un, password=pw)
        selected_cmd_file = open('add_backup_rsc.txt', 'r')
        selected_cmd_file.seek(0)
        for each_line in selected_cmd_file.readlines():
            connection = session.exec_command(each_line + '\n')
            time.sleep(1)
        selected_cmd_file.close()
        session.close()
        print('=====================Configuration done ========================')
    except paramiko.AuthenticationException:
        print('* invalid username or password \n Please, check the configuration')

def ssh_backup_rm(ip):
    try:
        session = paramiko.SSHClient()
        session.set_missing_host_key_policy(paramiko.AutoAddPolicy)
        session.connect(ip, username=un, password=pw)
        selected_cmd_file = open('rm_backup_rsc.txt', 'r')
        selected_cmd_file.seek(0)
        for each_line in selected_cmd_file.readlines():
            connection = session.exec_command(each_line + '\n')
            time.sleep(1)
        selected_cmd_file.close()
        session.close()
        print('=====================Configuration done ========================')
    except paramiko.AuthenticationException:
        print('* invalid username or password \n Please, check the configuration')

ssh_backup_rm(ip)
