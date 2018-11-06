# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Lokasi(models.Model):
    _name = 'inventaris.lokasi'
    
    name = fields.Char('Name', required=True)