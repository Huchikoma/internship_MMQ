################################################################################
#
# File Name: views.py
# Application: explore_tree/renderer
# Purpose:
#
# Author:
#         Philippe Dessauw
#         philippe.dessauw@nist.gov
#
#         Guillaume Sousa Amaral
#         guillaume.sousa@nist.gov
#
# Sponsor: National Institute of Standards and Technology (NIST)
#
################################################################################
from os.path import join
from django.template import Context, Template
from explore_tree.api.navigation.views import navigation_get
import query
from mgi.settings import BASE_DIR
from utils.xml_utils.projection import get_projection

TEMPLATES_PATH = join(BASE_DIR, 'explore_tree', 'parser', 'templates')


def render_navigation(navigation):
    """
    Renders a navigation tree
    :param navigation:
    :return:
    """
    nav_tree_html = ""
    for navigation_id in navigation.children:
        navigation_child = navigation_get(navigation_id)

        with open(join(TEMPLATES_PATH, 'li.html'), 'r') as li_file:
            li_content = li_file.read()
            li_template = Template(li_content)

            name = navigation_child.name.split('#')[1] if '#' in navigation_child.name else navigation_child.name

            # there is a projection, get documents from database
            if 'projection' in navigation_child.options and navigation_child.options['projection'] is not None:
                context = {
                    'branch_id': navigation_id,
                    'branch_name': name,
                    'branches': render_documents(navigation_child)
                }
            else:
                context = {
                    'branch_id': navigation_id,
                    'branch_name': name,
                    'branches': render_navigation(navigation_child)
                }

            if 'view' in navigation_child.options and navigation_child.options['view'] is not None:
                context["branch_view"] = "true"

            if "hidden" in navigation_child.options and navigation_child.options["hidden"]:
                context["hidden"] = True

            nav_tree_html += li_template.render(Context(context))

    return nav_tree_html


def render_documents(navigation):
    doc_tree_html = ""

    try:
        # Get the navigation id
        navigation_id = str(navigation.id)

        # Get projection
        projection = navigation.options['projection']

        # get filters from parents
        filters = []
        while True:
            # add filter to the list of filters
            if 'filter' in navigation.options and navigation.options['filter'] is not None:
                filters.append(navigation.options['filter'])

            # if no parent, stops the filter lookup
            if navigation.parent is None:
                break
            else:  # if parent, continue the filter lookup at the parent level
                navigation = navigation_get(navigation.parent)

        # get the documents matching the query
        documents = query.execute_query(filters, projection)

        for document in documents:
            with open(join(TEMPLATES_PATH, 'li_document.html'), 'r') as li_file:
                li_content = li_file.read()
                li_template = Template(li_content)

                branch_name = get_projection(document)
                context = {
                    'branch_id': document['_id'],
                    "parent_id": navigation_id,
                    'branch_name': branch_name,
                }

                doc_tree_html += li_template.render(Context(context))
    except Exception, e:
        with open(join(TEMPLATES_PATH, 'li_error.html'), 'r') as li_file:
            li_content = li_file.read()
            li_template = Template(li_content)

        context = {
            "error_message": e.message
        }

        doc_tree_html = li_template.render(Context(context))

    return doc_tree_html
