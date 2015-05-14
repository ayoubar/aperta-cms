#
# coding=utf-8
#
import datetime

from django.conf import settings
from django.template.loader import render_to_string
from django.core.mail import EmailMessage

###############################
# GLOBAL SUPPORTING FUNCTIONS #
###############################
def debug(app,message):
  if settings.DEBUG:
    from sys import stderr as errlog
    print >>errlog, 'DEBUG ['+unicode(app)+']: '+unicode(message)

def notify_by_email(sender,to,subject,message_content,template='default.txt',attachment=None):

  if not sender: sender = settings.EMAILS['sender']['default']
  email = EmailMessage(
                subject=subject,
                from_email=sender,
                to=[to],
#                cc=[settings.TEMPLATE_CONTENT['email']['cc'][int(dept)]]
          )
  message_content['FOOTER'] = settings.EMAILS['footer']
  email.body = render_to_string(template,message_content)
  if attachment: email.attach(attachment)
  try:
    email.send()
    return True
  except:
    return False

def show_form(wiz,step,field,const):
  cleaned_data = wiz.get_cleaned_data_for_step(step) or {}
  d = cleaned_data.get(field) or 666
  return int(d) == const

def visualiseDecimal(decIn,currency=''):
  s = '{:,.12g}'.format(decIn)
  s = s.replace(',', ' ')
  s = s.replace('.', ',')
  if ',' in s:
    s = s.rstrip('0')
    s = s.rstrip(',')
  if not currency:
    return s
  elif currency != '' :
    s = s + ' ' + currency
  return s

def visualiseDateTime(dtIn):
  import locale
  locale.setlocale(locale.LC_ALL, settings.LC_ALL)

  if type(dtIn) is datetime.date: return dtIn.strftime('%a le ') + dtIn.strftime('%d %b %Y').lstrip('0')
  if type(dtIn) is datetime.time: return dtIn.strftime('%Hh%M').lstrip('0')
  if type(dtIn) is datetime.datetime: return dtIn.strftime('%a le ') + dtIn.strftime('%d %b %Y').lstrip('0') + u' à ' + dtIn.strftime('%Hh%M').lstrip('0')

# rename uploaded files
def rmf(instance, dir, filename=None):
  try:
    orig_name, orig_ext = splitext(filename)
  except:
    orig_ext = ''

  fn=dir.upper() + '_' + unicode(instance).replace(' ','') #remove whitespaces

  return {'name': normalize('NFKD', fn).encode('ascii','ignore'),'ext': orig_ext}

