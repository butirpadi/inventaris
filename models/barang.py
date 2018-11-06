# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Barang(models.Model):
    _name = 'inventaris.barang'
    
    name = fields.Char('Name', required=True)
    code = fields.Char('Code')
    internal_reference = fields.Char('Kode')
    serial_number = fields.Char('Serial Number')
    panjang = fields.Float('Panjang', default=0.0)
    lebar = fields.Float('Lebar', default=0.0)
    tinggi = fields.Float('Tinggi', default=0.0)
    color_id = fields.Many2one('inventaris.color', ondelete="restrict")
    kategori_id = fields.Many2one('inventaris.kategori', string="Kategori", ondelete="restrict")
    nilai_penyusutan = fields.Float('Nilai Penyusutan', default=0.0)
    interval_penyusutan = fields.Integer('Bulan')
    lokasi_id = fields.Many2one('inventaris.lokasi', string="Lokasi")
    lokasi_move_id = fields.Many2many('inventaris.lokasi', relation="inventaris.barang.move", column1="barang_id", column2="lokasi_id" ,string="Lokasi Moving", ondelete="restrict")
    brand_id = fields.Many2one('inventaris.brand', string="Brand")
    satuan_id= fields.Many2one('inventaris.satuan', string="Satuan")
    
