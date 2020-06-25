#!/usr/bin/python

import os
import shutil
import json

# Setup debug logging...
log_file = '~/.MailMate.log'
log = open(log_file, 'w')
log.write('Starting ATTACHSAVE')

# Parse the json from MailMate to save the attachments
if "MM_FILES" in os.environ:
    for attachment in json.loads(os.environ['MM_FILES']):
        if attachment["filePath"]:
            # Create directories for attachments, based on the sender name...
            directory = '~/Library/Mobile\ Documents/com~apple~CloudDocs/potpourri/'
            log.write('Saving attachment: {}'.format(attachment))
            shutil.copy(attachment["filePath"], directory)

log.close()
