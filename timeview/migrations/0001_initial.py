# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Timelike'
        db.create_table(u'timeview_timelike', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('localsource', self.gf('django.db.models.fields.files.FileField')(max_length=100, blank=True)),
            ('youtubesource', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('vimeosource', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
        ))
        db.send_create_signal(u'timeview', ['Timelike'])


    def backwards(self, orm):
        # Deleting model 'Timelike'
        db.delete_table(u'timeview_timelike')


    models = {
        u'timeview.timelike': {
            'Meta': {'object_name': 'Timelike'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'localsource': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'vimeosource': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'youtubesource': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'})
        }
    }

    complete_apps = ['timeview']