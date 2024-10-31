from odoo import models, fields, api

class ListClass(models.Model):
    _name = "list.class"
    _rec_name ='teacher_name'
    _description ='Quản lý lớp học'

    stt = fields.Char(string="STT", readonly=True, copy=False, default="New")
    class_name = fields.Char(string="Lớp")
    teacher_name = fields.Many2one('res.partner', string="Tên giáo viên", ondelete="cascade")
    class_size = fields.Integer(string="Sĩ số lớp", )
    address = fields.Char(string="Địa chỉ")
    status = fields.Selection([
        ('on', 'ON'),
        ('off', 'OFF')
    ], string="Trạng thái", default='off')


    @api.model
    def create(self, vals):
        if vals.get("stt", "New") == "New":
            vals["stt"] = self.env["ir.sequence"].next_by_code("list.class.stt") or "New"
        return super(ListClass, self).create(vals)


class InforClass(models.Model):
    _name = "infor.class"
    _rec_name = 'student_name'
    _description = 'Thông tin học sinh'

    stt = fields.Char(string="STT", readonly=True, copy=False, default="New")
    student_name = fields.Many2one('res.partner', string="Tên học sinh", ondelete="cascade")
    date = fields.Date(required=True, states={'confirm': [('readonly', False)]}, index=True, copy=False, default=fields.Date.context_today)
    male = fields.Selection(string='Giới tính', required=True, readonly=False, copy=False, tracking=True, selection=[
        ('nam', 'Nam'),
        ('nữ', 'Nữ'),
    ], default='nam',)
    address = fields.Char(string="Địa chỉ")
    role = fields.Char(string="Chức vụ")
    status = fields.Selection(string='Trạng thái', required=True, readonly=False, copy=False, tracking=True, selection=[
        ('dang_hoc', 'Đang học'),
        ('da_nghi', 'Đã nghỉ học'),
        ('da_chuyen', 'Đã chuyển lớp'),
    ], default='dang_hoc', )
    note = fields.Text(string="Ghi chú")

    @api.model
    def create(self, vals):
        if vals.get("stt", "New") == "New":
            vals["stt"] = self.env["ir.sequence"].next_by_code("list.class.stt") or "New"
        return super(InforClass, self).create(vals)



    # @api.model
    # def create(self, vals):
    #     max_stt = self.search([], order='stt desc', limit=1).stt
    #     vals['stt'] = max_stt + 1 if max_stt else 1
    #     return super(InforClass, self).create(vals)
