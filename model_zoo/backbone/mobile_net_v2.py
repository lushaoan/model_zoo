#!/usr/bin/env python3.6
# -*- coding:utf-8 -*-
__author__ = 'Lu ShaoAn'
__version__ = '1.0'
__date__ = '2023.08.06'


import torch


class MobilNetV2(torch.nn.Module):
    def __init__(self):
        super().__init__()