#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import with_statement
import boto.ses,sys,time

#aws configuration
AWS_KEY = ''
AWS_SECRET = ''
AWS_REGION = ''

#Put an email address verified in SES console
#Set sender name to anything you want
VER_EMAIL  = 'SENDER_NAME <SENDER_EMAIL>'

#emails per second
#by default, You can send 5 emails per second max or
#program fails to send emails.
#if your account has different limits, feel free to
#increase this value
eps = 5


def send_bulk_emails(listfile,mailfile):
  #establish connection with SES
  conn = boto.ses.connect_to_region(AWS_REGION,
                  aws_access_key_id=AWS_KEY,
              aws_secret_access_key=AWS_SECRET)
  delay = 1.0/eps
  #Read email data
  with open(mailfile) as f: subject, body = f.read().split('\n\n')
  with open(listfile,'r') as f:
    maillist = f.read().split('\n')[:-1]
    for e in maillist:
    
      #send to each recipient
      conn.send_email(VER_EMAIL, subject, body, e)
      time.sleep(delay)
      print "sent to %s"%e
    print "finished"

if __name__ == "__main__":
  try:
    send_bulk_emails(sys.argv[1],sys.argv[2])
  except Exception, e: print "Exception Ocurred:\n%s"%e
