# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Timelike'
        db.delete_table(u'timeview_timelike')


    def backwards(self, orm):
        # Adding model 'Timelike'
        db.create_table(u'timeview_timelike', (
            ('vimeosource', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('author', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True, blank=True)),
            ('localsource', self.gf('django.db.models.fields.files.FileField')(max_length=100, blank=True)),
            ('youtubesource', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'timeview', ['Timelike'])


    models = {
        
    }

    complete_apps = ['timeview']