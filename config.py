#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7110231022:AAHzjuE3MR7FdUvdFnaEHKurmQ9526aTIiM")
    API_ID = int(os.environ.get("API_ID", "22727464"))
    API_HASH = os.environ.get("API_HASH", "f0e595a263c89aa17f6571b8af296ced")
    AUTH_USERS = "887699812"

