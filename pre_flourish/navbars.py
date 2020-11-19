from django.conf import settings
from edc_navbar import NavbarItem, site_navbars, Navbar


no_url_namespace = True if settings.APP_NAME == 'pre_flourish' else False

pre_flourish_dashboard = Navbar(name='pre_flourish_dashboard')


pre_flourish_dashboard.append_item(
    NavbarItem(
        name='pre_flourish_screening',
        title='Pre Flourish Screening',
        label='pre flourish screening',
        fa_icon='far fa-user-circle',
        url_name='pre_flourish_screening_listboard_url',
        no_url_namespace=False))

pre_flourish_dashboard.append_item(
    NavbarItem(
        name='pre_flourish_consent',
        title='Caregiver Subjects',
        label='caregiver subjects',
        fa_icon='far fa-user-circle',
        url_name='pre_flourish_consent_listboard_url',
        no_url_namespace=False))

# flourish_dashboard.append_item(
#     NavbarItem(
#         name='consented_subject',
#         title='Maternal Subjects',
#         label='maternal subjects',
#         fa_icon='far fa-user-circle',
#         url_name=settings.DASHBOARD_URL_NAMES[
#             'subject_listboard_url'],
#         no_url_namespace=no_url_namespace))

pre_flourish_dashboard.append_item(
    NavbarItem(
        name='child_subjects',
        title='Child Subjects',
        label='child subjects',
        fa_icon='far fa-user-circle',
        url_name='child_listboard_url',
        no_url_namespace=False))


site_navbars.register(pre_flourish_dashboard)
