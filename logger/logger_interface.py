#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
from abc import ABCMeta, abstractmethod


class SystemLoggerInterface(metaclass=ABCMeta):
    @abstractmethod
    def exception(self, message: str) -> None:
        raise NotImplemented()

    @abstractmethod
    def error(self, message: str) -> None:
        raise NotImplemented()

    @abstractmethod
    def debug(self, message: str) -> None:
        raise NotImplemented()

    @abstractmethod
    def info(self, message: str) -> None:
        raise NotImplemented()

    @abstractmethod
    def warn(self, message: str) -> None:
        raise NotImplemented()


class ServiceLoggerInterface(metaclass=ABCMeta):
    @abstractmethod
    def emit(self, request, response, suppress_log_inout: bool = False) -> None:
        raise NotImplemented()

    # noinspection PyMethodMayBeStatic
    def to_str_from_request(self, request) -> str:
        input, option = request
        tmp = {'input': input, 'option': option}
        return json.dumps(tmp)

    # noinspection PyMethodMayBeStatic
    def to_str_from_response(self, response) -> str:
        output, score, option = response
        tmp = {'output': output, 'score': score, 'option': option}
        return json.dumps(tmp)
