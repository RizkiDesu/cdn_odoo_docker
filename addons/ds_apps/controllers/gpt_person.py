import base64
from odoo import http
from odoo.http import request

class CrudController(http.Controller):

    @http.route('/crud/persons', auth='public', website=True)
    def list_persons(self, **kwargs):
        persons = request.env['crud.person'].sudo().search([])
        return request.render('ds_apps.person_list', {'persons': persons})

    @http.route('/crud/person/create', auth='public', website=True)
    def create_person_form(self, **kwargs):
        return request.render('ds_apps.person_form', {})

    @http.route('/crud/person/save', auth='public', website=True, csrf=False, methods=['POST'])
    def save_person(self, **kwargs):
        image = request.httprequest.files.get('image')
        image_base64 = base64.b64encode(image.read()) if image else False

        request.env['crud.person'].sudo().create({
            'name': kwargs.get('name'),
            'email': kwargs.get('email'),
            'age': kwargs.get('age'),
            'image': image_base64,
        })
        return request.redirect('/crud/persons')

    @http.route('/crud/person/edit/<int:person_id>', auth='public', website=True)
    def edit_person_form(self, person_id, **kwargs):
        person = request.env['crud.person'].sudo().browse(person_id)
        return request.render('ds_apps.person_form', {'person': person})

    @http.route('/crud/person/update/<int:person_id>', auth='public', website=True, csrf=False, methods=['POST'])
    def update_person(self, person_id, **kwargs):
        person = request.env['crud.person'].sudo().browse(person_id)
        image = request.httprequest.files.get('image')
        image_base64 = base64.b64encode(image.read()) if image else person.image

        person.sudo().write({
            'name': kwargs.get('name'),
            'email': kwargs.get('email'),
            'age': kwargs.get('age'),
            'image': image_base64,
        })
        return request.redirect('/crud/persons')

    @http.route('/crud/person/delete/<int:person_id>', auth='public', website=True)
    def delete_person(self, person_id, **kwargs):
        person = request.env['crud.person'].sudo().browse(person_id)
        person.sudo().unlink()
        return request.redirect('/crud/persons')
