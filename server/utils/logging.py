from server.extensions import db
from server.models.tms_models import AuditLog

def create_audit_log(action, user_id=None, email=None, details=None):
    audit_log = AuditLog(action=action, user_id=user_id,
                         email=email, details=details)
    db.session.add(audit_log)
    db.session.commit()
