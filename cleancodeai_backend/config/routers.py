
class DatabaseRouter:

    #App for Audit Main Database
    route_app_main_labels = {
        "ai_core", 
        "authentication",
        "authorization",
        "mcp",
        "organization",
        "user_profile"
        }
    #App for Audit Logger Database
    route_app_log_labels = {"audit"}

    def db_for_read(self, model, **hints):
        if model._meta.app_label in self.route_app_main_labels:
            return "main"
        if model._meta.app_label in self.route_app_log_labels:
            return "logs"
        return None
    
    def db_for_write(self, model, **hints):
        if model._meta.app_label in self.route_app_main_labels:
            return "main"
        if model._meta.app_label in self.route_app_log_labels:
            return "logs"
        return None
    
    def allow_migrate(self, db, app_label, model_name=None, **hints):
        #Check if app label included to main database then check if db is actually called main or logs
        if app_label in self.route_app_main_labels:
            return db == "main"
        if app_label in self.route_app_log_labels:
            return db == "logs"
        if db in ("main", "logs"):
            return False # explicitly block
        return None