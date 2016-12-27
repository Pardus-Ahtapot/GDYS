#!/usr/bin/env python

import logging
import logging.handlers
import subprocess

class Syslogger:
    def __init__(self,name,formatter,handler_address,user):
        self.log = logging.getLogger(name)
        self.log.setLevel(logging.DEBUG)
        handler = logging.handlers.SysLogHandler(address = handler_address)

        format = logging.Formatter(formatter)
        handler.setFormatter(format)
        self.log.addHandler(handler)
        self.user = user


    def send_log(self,log_level,message):
        if log_level == "debug":
            self.log.debug(message+" by " + self.user)
        elif log_level == "info":
            self.log.info(message+" by " + self.user)
        elif log_level == "critical":
            self.log.critical(message+" by " + self.user)
        elif log_level == "warning":
            self.log.warning(message+" by " + self.user)
        elif log_level == "error":
            self.log.error(message+" by " + self.user)
        else:
            pass


class Filelogger:
    def __init__(self,name,formatter,file_path,file_mode,user):
        self.name = name
        self.formatter = formatter
        self.file_path = file_path
        self.file_mode = file_mode
        self.user = user

    def send_log(self,log_level,message):
        logging.basicConfig(format=self.formatter,filename=self.file_path,filemode=self.file_mode,level=logging.DEBUG)
        if log_level == "debug":
            logging.debug(message+" by " + self.user)
        elif log_level == "info":
            logging.info(message+" by " + self.user)
        elif log_level == "critical":
            logging.critical(message+" by " + self.user)
        elif log_level == "warning":
            logging.warning(message+" by " + self.user)
        elif log_level == "error":
            logging.error(message+" by " + self.user)
        else:
            pass