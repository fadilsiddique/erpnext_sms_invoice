# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "erpnext_sms_invoice"
app_title = "Erpnext Sms Invoice"
app_publisher = "TRidz"
app_description = "SMS Invoice"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "fadil@tridz.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/erpnext_sms_invoice/css/erpnext_sms_invoice.css"
# app_include_js = "/assets/erpnext_sms_invoice/js/erpnext_sms_invoice.js"

# include js, css files in header of web template
# web_include_css = "/assets/erpnext_sms_invoice/css/erpnext_sms_invoice.css"
# web_include_js = "/assets/erpnext_sms_invoice/js/erpnext_sms_invoice.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "erpnext_sms_invoice.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "erpnext_sms_invoice.install.before_install"
# after_install = "erpnext_sms_invoice.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "erpnext_sms_invoice.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }
doc_events = {
#   "*": {
#       "on_update": "method",
#       "on_cancel": "method",
#       "on_trash": "method"
#   }
    "*":{
        "on_submit":"erpnext_sms_invoice.sms_invoice.attach_pdf"
    }
        
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"erpnext_sms_invoice.tasks.all"
# 	],
# 	"daily": [
# 		"erpnext_sms_invoice.tasks.daily"
# 	],
# 	"hourly": [
# 		"erpnext_sms_invoice.tasks.hourly"
# 	],
# 	"weekly": [
# 		"erpnext_sms_invoice.tasks.weekly"
# 	]
# 	"monthly": [
# 		"erpnext_sms_invoice.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "erpnext_sms_invoice.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "erpnext_sms_invoice.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "erpnext_sms_invoice.task.get_dashboard_data"
# }

