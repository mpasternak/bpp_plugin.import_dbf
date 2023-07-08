from django.apps import AppConfig


class ImportDbfConfig(AppConfig):
    name = 'bpp_plugins.import_dbf'

    def ready(self):
        from django.conf import settings

        if getattr(settings, "PERMISSIONS_WIDGET_EXCLUDE_APPS", None) and hasattr(settings.PERMISSIONS_WIDGET_EXCLUDE_APPS, "append"):
            settings.PERMISSIONS_WIDGET_EXCLUDE_APPS.append("bpp_plugins.import_dbf")

        from bpp import system
        from bpp_plugins.import_dbf.models import Bib, B_A, Aut, Jed, Poz, B_U, Usi, Ses, Wx2, Ixn
        system.groups["import DBF"] = [Bib, B_A, Aut, Jed, Poz, B_U, Usi, Ses, Wx2, Ixn]

        # TODO: this is an admin menu hook. This should be shomehow called by the admin
        
# IMPORT_DBF_MENU_1 = [
#     (
#         "Zaimportowana bibliografia",
#         "/admin/import_dbf/bib/",
#     ),
#     (
#         "Zaimportowane dane Open Access",
#         "/admin/import_dbf/b_u/",
#     ),
#     (
#         "Zaimportowane opisy rekordów",
#         "/admin/import_dbf/poz/",
#     ),
#     (
#         "Zaimportowane i zanalizowane opisy rekordów",
#         "/admin/import_dbf/bib_desc/",
#     ),
#     (
#         "Zaimportowane źródła",
#         "/admin/import_dbf/usi/",
#     ),
#     (
#         "Zaimportowane jednostki",
#         "/admin/import_dbf/jed/",
#     ),
#     (
#         "Zaimportowani autorzy",
#         "/admin/import_dbf/aut/",
#     ),
#     (
#         "Zaimportowane powiązania autor-rekord",
#         "/admin/import_dbf/b_a/",
#     ),
#     # Tabela sesji - zbędna
#     # ('Zaimportowane Ses', '/admin/import_dbf/ses/',),
#     (
#         "Zaimportowane identyfikatory PBN",
#         "/admin/import_dbf/ixn/",
#     ),
#     (
#         "Zaimportowane dyscypliny pracowników",
#         "/admin/import_dbf/dys/",
#     ),
#     (
#         "Zaimportowane hasła naukowe",
#         "/admin/import_dbf/ixe/",
#     ),
#     (
#         "Zaimportowane charaktery publikacji",
#         "/admin/import_dbf/pub/",
#     ),
#     (
#         "Zaimportowana wersja systemu",
#         "/admin/import_dbf/sys/",
#     ),
#     (
#         "Zaimportowane wydziały",
#         "/admin/import_dbf/wyd/",
#     ),
#     (
#         "Zaimportowane dziedziny",
#         "/admin/import_dbf/ldy/",
#     ),
#     (
#         "Zaimportowane języki",
#         "/admin/import_dbf/jez/",
#     ),
#     (
#         "Zaimportowane typy KBN",
#         "/admin/import_dbf/kbn/",
#     ),
#     (
#         "Zaimportowane bazy",
#         "/admin/import_dbf/ixb/",
#     ),
#     (
#         "Zaimportowane listy wydawców",
#         "/admin/import_dbf/lis/",
#     ),
#     (
#         "Zaimportowane historia jednostek",
#         "/admin/import_dbf/j_h/",
#     ),
#     (
#         "Zaimportowane rekordy KBR",
#         "/admin/import_dbf/kbr/",
#     ),
#     (
#         "Zaimportowane Jer",
#         "/admin/import_dbf/jer/",
#     ),
#     (
#         "Zaimportowane B_B",
#         "/admin/import_dbf/b_b/",
#     ),
#     (
#         "Zaimportowane B_N",
#         "/admin/import_dbf/b_n/",
#     ),
# ]

# IMPORT_DBF_MENU_2 = [
#     (
#         "Zaimportowane Wx2",
#         "/admin/import_dbf/wx2/",
#     ),
#     (
#         "Zaimportowane Kad",
#         "/admin/import_dbf/kad/",
#     ),
#     (
#         "Zaimportowane Loc",
#         "/admin/import_dbf/loc/",
#     ),
#     (
#         "Zaimportowane Pbc",
#         "/admin/import_dbf/pbc/",
#     ),
#     (
#         "Zaimportowane Sci",
#         "/admin/import_dbf/sci/",
#     ),
#     (
#         "Zaimportowane Wsx",
#         "/admin/import_dbf/wsx/",
#     ),
#     (
#         "Zaimportowane B_E",
#         "/admin/import_dbf/b_e/",
#     ),
#     (
#         "Zaimportowane B_P",
#         "/admin/import_dbf/b_p/",
#     ),
#     (
#         "Zaimportowane Ixp",
#         "/admin/import_dbf/ixp/",
#     ),
#     (
#         "Zaimportowane Pba",
#         "/admin/import_dbf/pba/",
#     ),
#     (
#         "Zaimportowane Pbd",
#         "/admin/import_dbf/pbd/",
#     ),
#     (
#         "Zaimportowane Rtf",
#         "/admin/import_dbf/rtf/",
#     ),
#     (
#         "Zaimportowane S_B",
#         "/admin/import_dbf/s_b/",
#     ),
#     (
#         "Zaimportowane Wsy",
#         "/admin/import_dbf/wsy/",
#     ),
#     (
#         "Zaimportowane B_L",
#         "/admin/import_dbf/b_l/",
#     ),
#     (
#         "Zaimportowane Ext",
#         "/admin/import_dbf/ext/",
#     ),
#     (
#         "Zaimportowane Pbb",
#         "/admin/import_dbf/pbb/",
#     ),
# ]

        #if apps.is_installed("bpp_plugins.import_dbf"):
        #    if "import_dbf_aut" in connection.introspection.table_names():
        #        flt("import DBF", "import DBF", IMPORT_DBF_MENU_1)
        #        # flt("import DBF", "import DBF #2", IMPORT_DBF_MENU_2)
        #    else:
        #        # De-register all models from other apps
        #        for model in apps.get_app_config("import_dbf").models.values():
        #            if admin.site.is_registered(model):
        #                admin.site.unregister(model)

