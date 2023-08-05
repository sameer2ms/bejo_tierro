from . import __version__ as app_version

app_name = "bajo_tierro"
app_title = "Bajo Tierro"
app_publisher = "Sameer"
app_description = "Custom App Two"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "sameer2mshaikh@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/bajo_tierro/css/bajo_tierro.css"
# app_include_js = "/assets/bajo_tierro/js/bajo_tierro.js"

# include js, css files in header of web template
# web_include_css = "/assets/bajo_tierro/css/bajo_tierro.css"
# web_include_js = "/assets/bajo_tierro/js/bajo_tierro.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "bajo_tierro/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

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

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "bajo_tierro.install.before_install"
# after_install = "bajo_tierro.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "bajo_tierro.uninstall.before_uninstall"
# after_uninstall = "bajo_tierro.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "bajo_tierro.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
#	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
#	"*": {
#		"on_update": "method",
#		"on_cancel": "method",
#		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
#	"all": [
#		"bajo_tierro.tasks.all"
#	],
#	"daily": [
#		"bajo_tierro.tasks.daily"
#	],
#	"hourly": [
#		"bajo_tierro.tasks.hourly"
#	],
#	"weekly": [
#		"bajo_tierro.tasks.weekly"
#	]
#	"monthly": [
#		"bajo_tierro.tasks.monthly"
#	]
# }

# Testing
# -------

# before_tests = "bajo_tierro.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "bajo_tierro.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "bajo_tierro.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Request Events
# ----------------
# before_request = ["bajo_tierro.utils.before_request"]
# after_request = ["bajo_tierro.utils.after_request"]

# Job Events
# ----------
# before_job = ["bajo_tierro.utils.before_job"]
# after_job = ["bajo_tierro.utils.after_job"]

# User Data Protection
# --------------------

user_data_fields = [
	{
		"doctype": "{doctype_1}",
		"filter_by": "{filter_by}",
		"redact_fields": ["{field_1}", "{field_2}"],
		"partial": 1,
	},
	{
		"doctype": "{doctype_2}",
		"filter_by": "{filter_by}",
		"partial": 1,
	},
	{
		"doctype": "{doctype_3}",
		"strict": False,
	},
	{
		"doctype": "{doctype_4}"
	}
]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"bajo_tierro.auth.validate"
# ]

