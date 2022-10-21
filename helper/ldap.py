from user.models import User


def sync_user_relations(user, ldap_attributes, *, connection=None, dn=None):
    print(user.username)
    local1 = {
        "responsable": "jose.ssanchez"
    }
    # responsable = Local.objets.filter(responsable_email=user.email).first()
    # if responsable is not None:
    #       user.rol = "Responsable"
    # responsable = Local.objets.filter(responsable_email=user.email).first()
    # if responsable is not None:
    #       user.rol = "Responsable"

    listado_locales = [local1]
    for local in listado_locales:
        if user.username == local["responsable"]:
            obj_user = User.objects.filter(username=user).first()
            if obj_user is not None:
                obj_user.rol = 'Responsable'
                obj_user.save()

        if user.username == "angel.napoles":
            obj_user = User.objects.filter(username=user).first()
            obj_user.is_superuser = True
            obj_user.save()

    print(ldap_attributes)
