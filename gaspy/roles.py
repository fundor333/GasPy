from rolepermissions.roles import AbstractUserRole


class Gasista(AbstractUserRole):
    available_permissions = {
        'show_verbali': True,
        'show_rubrica': True,
        'show_regolamento': True,
        'edit_verbali':True,
    }

class PreGasista(AbstractUserRole):
    available_permissions ={
    }

class Admin(AbstractUserRole):
    available_permissions ={
    }

class ExGasista(AbstractUserRole):
    available_permissions = {
        'show_verbali': False,
        'show_rubrica': False,
        'show_regolamento': False,
        'edit_verbali':False,
    }