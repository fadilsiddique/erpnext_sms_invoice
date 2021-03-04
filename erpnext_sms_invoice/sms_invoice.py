import frappe
from frappe import _
from frappe import publish_progress

def attach_pdf(doc,event=None):
    args = {
        "doctype":doc.doctype,
        "name":doc.name,
        "party":getattr(doc,"customer", _("Unknown")),
        "lang":getattr(doc,"language","en")
    }

    if doc.doctype=="Quotation":
        args["party"]=doc.party_name

    if doc.doctype =="Dunning":
        party=frappe.get_value("Sales Invoice",doc.sales_invoice,"customer")
        lang = frappe.get_value("Sales Invoice",doc.sales_invoice,"language")
        args["party"]=party
        args["lang"]=lang

    settings = frappe.get_single("SMS Invoice")
    slug="_".join(doc.doctype.lower().split(" "))

    if settings.get(slug):
        execute(**args)

    
def execute(doctype, name, party, lang=None):
    settings=frappe.get_single("SMS Invoice")
    progress_title=_("Creating PDF...")

    if lang:
        frappe.local.lang=lang

    doctype_folder=create_folder(_(doctype),"Home")
    party_folder = create_folder(party,doctype_folder)
    
    pdf_data = get_pdf_data(doctype,name)
    
    save_and_attach(pdf_data,doctype,name,party_folder)


def create_folder(folder,parent):
    from frappe.core.doctype.file.file import create_new_folder
    new_folder_name="/".join([parent, folder])

    if not frappe.db.exists("File",new_folder_name):
        create_new_folder(folder,parent)


    return new_folder_name

def get_pdf_data(doctype,name):
    html= frappe.get_print(doctype, name)

    return frappe.utils.pdf.get_pdf(html)


def save_and_attach(content, to_doctype, to_name, folder):

    from frappe.utils.file_manager import save_file

    file_name="{}.pdf".format(to_name.replace(" ", "-").replace("/", "-"))
    save_file(file_name,content,to_doctype,to_name,folder=folder, is_private=0)





