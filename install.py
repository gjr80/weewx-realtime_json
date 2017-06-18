#
# This program is free software; you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free Software
# Foundation; either version 2 of the License, or (at your option) any later
# version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more
# details.
#
#                     Installer for Realtime JSON
#
# Version: 0.1.0                                        Date: 18 June 2017
#
# Revision History
#   18 June 2017         v0.1.0
#       - initial implementation
#

import weewx

from distutils.version import StrictVersion
from setup import ExtensionInstaller

REQUIRED_VERSION = "3.4.0"
RTD_VERSION = "0.1.0"


def loader():
    return RtdInstaller()


class RtdInstaller(ExtensionInstaller):
    def __init__(self):
        if StrictVersion(weewx.__version__) < StrictVersion(REQUIRED_VERSION):
            msg = "%s requires weeWX %s or greater, found %s" % ('Rtd ' + RTGD_VERSION,
                                                                 REQUIRED_VERSION,
                                                                 weewx.__version__)
            raise weewx.UnsupportedFeature(msg)
        super(RtdInstaller, self).__init__(
            version=RTD_VERSION,
            name='Rtd',
            description='Create a user defined JSON data string that can then be saved to file, dispatched to a URL via HTTP POST or dispatched as a message to a MQTT broker.',
            author="Gary Roderick",
            author_email="gjroderick<@>gmail.com",
            report_services=['user.rtd.RealtimeJSON'],
            config={
                'RealtimeJSON': {
                    'windrun_loop': 'false',
                    'max_cache_age': '600',
                    'Calculate': {
                        'atc': '0.8',
                        'nfac': '2',
                        'Algorithm': {
                            'maxSolarrad': 'RS'
                        }
                    }
                    'DecimalPlaces': {
                        'degree_C': '2',
                        'degree_F': '2',
                        'degree_compass': '1',
                        'foot': '2',
                        'hPa': '2',
                        'inHg': '4',
                        'inch': '3',
                        'inch_per_hour': '3',
                        'km_per_hour': '1',
                        'km': '2',
                        'mbar': '2',
                        'meter': '1',
                        'meter_per_second': '2',
                        'mile': '2',
                        'mile_per_hour': '1',
                        'mm': '2',
                        'mm_per_hour': '2',
                        'percent': '1',
                        'uv_index': '2',
                        'watt_per_meter_squared': '1'
                    },
                    'Groups': {
                        'group_altitude': 'foot',
                        'group_pressure': 'hPa',
                        'group_rain': 'mm',
                        'group_speed': 'km_per_hour',
                        'group_temperature': 'degree_C'
                    },
                }
            },
            files=[('bin/user', ['bin/user/rtd.py'])]
        )
