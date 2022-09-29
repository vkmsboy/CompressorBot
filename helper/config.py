#    This file is part of the Compressor distribution.
#    Copyright (c) 2021 Danish_00
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, version 3.
#
#    This program is distributed in the hope that it will be useful, but
#    WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
#    General Public License for more details.
#
#    License can be found in < https://github.com/1Danish-00/CompressorBot/blob/main/License> .

from . import *

try:
    APP_ID = config("15411499", cast=int)
    API_HASH = config("482e4968a9fbab2f7cb0e8ce409413d6")
    BOT_TOKEN = config("5279331861:AAFI5cp75kF9Lz1mHA72LLH9ZSOgfRr9euM")
    OWNER = config("1999010840", default=1322549723, cast=int)
    LOG = config("-1001624171223", cast=int)
except Exception as e:
    LOGS.info("Environment vars Missing")
    LOGS.info("something went wrong")
    LOGS.info(str(e))
    exit(1)
