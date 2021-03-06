#coding=utf-8

from django.db.models import Model, EmailField, DateField, IntegerField, CharField, ForeignKey, ImageField
from django.contrib.auth.models import User

from cms.functions import rmf


def rename_photo(i, f):
  name = str(i.first_name) + '_' + str.upper(i.last_name)
  fn = rmf('members', f, name)

  from os import sep
  return fn['name'] + fn['ext']

class Member(Model):
  ACT = 0
  HON = 1
  WBE = 2
  STB = 3
  DEL = 4
  STATUSES = (
    (ACT, 'actif'),
    (HON, 'honoraire'),
    (WBE, 'aspirant (wouldbe)'),
    (STB, 'inactif (standby)'),
    (DEL, 'deleted'),
  )
  LU = 10
  BE = 11
  FR = 12
  DE = 13
  PREFIXES = (
    (LU, '+352'),
    (BE, '+32'),
    (DE, '+49'),
    (FR, '+33'),
  )


  photo		= ImageField(verbose_name=u'Photo',upload_to=rename_photo,blank=True,null=True)
  first_name    = CharField(verbose_name=u'Prénom',max_length=100)
  last_name	= CharField(verbose_name=u'Nom',max_length=100)
  address     	= CharField(verbose_name=u'Adresse',max_length=250,blank=True,null=True)
  prefix      	= IntegerField(verbose_name=u'Préfix',choices=PREFIXES,default=LU) 
  phone         = IntegerField(verbose_name=u'Tél. fixe',blank=True,null=True)
  mobile      	= IntegerField(verbose_name=u'Tél. mobile',blank=True,null=True)
  email		= EmailField()
  start_date    = DateField(verbose_name=u'Date de début',blank=True,null=True)
  end_date      = DateField(verbose_name=u'Date de fin',blank=True,null=True) 
  status      	= IntegerField(verbose_name=u'Statut',choices=STATUSES,default=ACT) 
  user		= ForeignKey(User,verbose_name=u'Utilisateur',blank=True,null=True) 

  def __str__(self):
    return str(self.first_name) + ' ' + str.upper(self.last_name)

class RoleType(Model):
  A = 0
  B = 1
  O = 2
  TYPES = (
    (A, u'comité'),
    (B, u'commission'),
    (O, u'other'),
  )

  title		= CharField(verbose_name=u'Titre',max_length=100)
  type		= IntegerField(verbose_name=u'Type',choices=TYPES,default=A)
  desc		= CharField(verbose_name=u'Description',max_length=500,blank=True,null=True)

  def __str__(self):
    return self.title + u' ('+str(self.TYPES[self.type][1])+u')'

class Role(Model):
  member 	= ForeignKey(Member)
  type        	= ForeignKey(RoleType)
  year        	= CharField(verbose_name=u'Saison',max_length=25)

  def __str__(self):
    return str(self.type) + ' : ' + str(self.member)

