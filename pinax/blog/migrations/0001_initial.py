# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Post'
        db.create_table(u'blog_post', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('section', self.gf('django.db.models.fields.IntegerField')()),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=90)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
            ('author', self.gf('django.db.models.fields.related.ForeignKey')(related_name='posts', to=orm['core.User'])),
            ('markup', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('teaser_html', self.gf('django.db.models.fields.TextField')()),
            ('content_html', self.gf('django.db.models.fields.TextField')()),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('primary_image', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='+', null=True, to=orm['blog.Image'])),
            ('tweet_text', self.gf('django.db.models.fields.CharField')(max_length=140)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('published', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('state', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('secret_key', self.gf('django.db.models.fields.CharField')(unique=True, max_length=8, blank=True)),
            ('view_count', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'blog', ['Post'])

        # Adding model 'Revision'
        db.create_table(u'blog_revision', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('post', self.gf('django.db.models.fields.related.ForeignKey')(related_name='revisions', to=orm['blog.Post'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=90)),
            ('teaser', self.gf('django.db.models.fields.TextField')()),
            ('content', self.gf('django.db.models.fields.TextField')()),
            ('author', self.gf('django.db.models.fields.related.ForeignKey')(related_name='revisions', to=orm['core.User'])),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('published', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('view_count', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'blog', ['Revision'])

        # Adding model 'Image'
        db.create_table(u'blog_image', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('post', self.gf('django.db.models.fields.related.ForeignKey')(related_name='images', to=orm['blog.Post'])),
            ('image_path', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('url', self.gf('django.db.models.fields.CharField')(max_length=150, blank=True)),
            ('timestamp', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
        ))
        db.send_create_signal(u'blog', ['Image'])

        # Adding model 'FeedHit'
        db.create_table(u'blog_feedhit', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('request_data', self.gf('django.db.models.fields.TextField')()),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
        ))
        db.send_create_signal(u'blog', ['FeedHit'])

        # Adding model 'ReviewComment'
        db.create_table(u'blog_reviewcomment', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('post', self.gf('django.db.models.fields.related.ForeignKey')(related_name='review_comments', to=orm['blog.Post'])),
            ('review_text', self.gf('django.db.models.fields.TextField')()),
            ('timestamp', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('addressed', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'blog', ['ReviewComment'])


    def backwards(self, orm):
        # Deleting model 'Post'
        db.delete_table(u'blog_post')

        # Deleting model 'Revision'
        db.delete_table(u'blog_revision')

        # Deleting model 'Image'
        db.delete_table(u'blog_image')

        # Deleting model 'FeedHit'
        db.delete_table(u'blog_feedhit')

        # Deleting model 'ReviewComment'
        db.delete_table(u'blog_reviewcomment')


    models = {
        u'blog.feedhit': {
            'Meta': {'object_name': 'FeedHit'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'request_data': ('django.db.models.fields.TextField', [], {})
        },
        u'blog.image': {
            'Meta': {'object_name': 'Image'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image_path': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'post': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'images'", 'to': u"orm['blog.Post']"}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '150', 'blank': 'True'})
        },
        u'blog.post': {
            'Meta': {'ordering': "('-published',)", 'object_name': 'Post'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'posts'", 'to': u"orm['core.User']"}),
            'content_html': ('django.db.models.fields.TextField', [], {}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'markup': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'primary_image': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['blog.Image']"}),
            'published': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'secret_key': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '8', 'blank': 'True'}),
            'section': ('django.db.models.fields.IntegerField', [], {}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'state': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'teaser_html': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '90'}),
            'tweet_text': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'view_count': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'blog.reviewcomment': {
            'Meta': {'object_name': 'ReviewComment'},
            'addressed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'post': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'review_comments'", 'to': u"orm['blog.Post']"}),
            'review_text': ('django.db.models.fields.TextField', [], {}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'})
        },
        u'blog.revision': {
            'Meta': {'object_name': 'Revision'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'revisions'", 'to': u"orm['core.User']"}),
            'content': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'post': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'revisions'", 'to': u"orm['blog.Post']"}),
            'published': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'teaser': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '90'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'view_count': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'core.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '255', 'db_index': 'True'}),
            'full_name': ('django.db.models.fields.CharField', [], {'max_length': '1023', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_sales': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_service_for_tenant': ('django.db.models.fields.CharField', [], {'max_length': '32', 'null': 'True', 'blank': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'lang': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '5', 'blank': 'True'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'notify_system': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'notify_watching': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'otp_client_secret': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'otp_client_valid': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'use_beta': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'use_two_factor': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        }
    }

    complete_apps = ['blog']