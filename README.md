# Realtime JSON weeWX extension #

## Description ##

The *Realtime JSON* extension creates a user defined JSON data string that can then be saved to file, dispatched to a URL via HTTP POST or dispatched as a message to a MQTT broker.

## Pre-Requisites ##

The *Realtime JSON* extension requires *weeWX v3.4.0* or greater.

## Installation ##

The preferred method to install the *Realtime JSON* extension is to use the weeWX *wee\_extension* utility. To install the *Realtime JSON* extension using the weeWX *wee\_extension* utility:

**Note:** Symbolic names are used below to refer to some file location on the weeWX system. These symbolic names allow a common name to be used to refer to a directory that may be different from system to system. The following symbolic names are used below:

*$DOWNLOAD_ROOT*. The path to the directory containing the downloaded Highcharts for weeWX extension.

*$HTML_ROOT*. The path to the directory where weeWX generated reports are saved. This directory is normally set in the *[StdReport]* section of *weewx.conf*. Refer to [where to find things](http://weewx.com/docs/usersguide.htm#Where_to_find_things) in the weeWX [User's Guide](http://weewx.com/docs/usersguide.htm) for further information.

*$SKIN_ROOT*. The path to the directory where weeWX skin folders are located. This directory is normally set in the *[StdReport]* section of *weewx.conf*.Refer to [where to find things](http://weewx.com/docs/usersguide.htm#Where_to_find_things) in the weeWX [User's Guide](http://weewx.com/docs/usersguide.htm) for further information.

1.  Download the latest *Realtime JSON* extension from the *Realtime JSON* extension [releases page](https://github.com/gjr80/weewx-realtime_json/releases) into a directory accessible from the weeWX machine.

        $ wget -P $DOWNLOAD_ROOT https://github.com/gjr80/weewx-realtime_json/releases/download/v0.1.0/rtd-0.1.0.tar.gz

2.  Stop weeWX:

        $ sudo /etc/init.d/weewx stop

    or

        $ sudo service weewx stop

3.  Install the *Realtime JSON* extension downloaded at step 1 using the *wee_extension* utility:

        $ wee_extension --install=$DOWNLOAD_ROOT/hfw-0.2.1.tar.gz

    This will result in output similar to the following:

        Request to install '/var/tmp/rtd-0.1.0.tar.gz'
        Extracting from tar archive /var/tmp/rtd-0.1.0.tar.gz
        Saving installer file to /home/weewx/bin/user/installer/Rtd
        Saved configuration dictionary. Backup copy at /home/weewx/weewx.conf.20161123124410
        Finished installing extension '/var/tmp/rtd-0.1.0.tar.gz'

4. Start weeWX:

        $ sudo /etc/init.d/weewx start

    or

        $ sudo service weewx start

This will result in the JSON data object being generated after each loop packet has arrived and the JSON data will be saved/dispatched as per the *[RealtimeJSON]* settings in *weewx.conf*. The *Realtime JSON* installation can be further customized (eg units of measure, file locations etc) by referring to the Realtime JSON wiki.

## Support ###

General support issues may be raised in the Google Groups [weewx-user forum](https://groups.google.com/group/weewx-user "Google Groups weewx-user forum"). Specific bugs in the *Realtime JSON* extension code should be the subject of a new issue raised via the [Issues Page](https://github.com/gjr80/weewx-realtime_json/issues "Realtime JSON extension Issues").
 
## Licensing ##

The *Realtime JSON* extension is licensed under the [GNU Public License v3](https://github.com/gjr80/weewx-realtime_json/blob/master/LICENSE "Realtime JSON extension License").
