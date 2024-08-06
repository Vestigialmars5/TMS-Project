from server.extensions import db
from server.models.tms_models import AuditLog

def create_audit_log(user_id, action, details):
    audit_log = AuditLog(
        user_id=user_id, action=action, details=details
    )
    db.session.add(audit_log)
    db.session.commit()