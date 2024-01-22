
import socket


hostname = socket.gethostname()


flower_url = "http://49.213.238.75:5555"
rabbitmq_url = "http://49.213.238.75:15672"
# 如果是本地测试环境，修改链接
if ".local" in hostname:
    flower_url = "http://localhost:5555"
    rabbitmq_url = "http://localhost:15672"

JAZZMIN_SETTINGS = {
    # title of the window (Will default to current_admin_site.site_title if absent or None)

    "site_title": "CPOP",

    # Title on the login screen (19 chars max) (defaults to current_admin_site.site_header if absent or None)

    "site_header": "CPOP",

    # Title on the brand (19 chars max) (defaults to current_admin_site.site_header if absent or None)
    "site_brand": "CPOP",

    # logo
    "site_logo": "logo.png",

    # CSS classes that are applied to the logo above
    "site_logo_classes": "img-circle",



    # Welcome text on the login screen
    "welcome_sign": "歡迎使用CPOP管理台!!",


    # Copyright on the footer
    "copyright": "CPOP團隊",

    ############
    # Top Menu #
    ############

    # Links to put along the top menu
    "topmenu_links": [

        {"name": "GA4", "url": "https://analytics.google.com/analytics/web/",
            "permissions": [], "new_window": True},

        {"name": "Swagger", "url": "http://49.213.238.75:8000/swagger/",
            "permissions": ["廠商組"], "new_window": True},

        {"name": "Flower", "url": flower_url,
            "permissions": ["廠商組"], "new_window": True},

        {"name": "RabbitMQ", "url": rabbitmq_url,
            "permissions": ["廠商組"], "new_window": True},
    ],


    #############
    # Side Menu #
    #############

    "show_sidebar": True,

    # Custom icons for side menu apps/models See https://fontawesome.com/icons?d=gallery&m=free&v=5.0.0,5.0.1,5.0.10,5.0.11,5.0.12,5.0.13,5.0.2,5.0.3,5.0.4,5.0.5,5.0.6,5.0.7,5.0.8,5.0.9,5.1.0,5.1.1,5.2.0,5.3.0,5.3.1,5.4.0,5.4.1,5.4.2,5.13.0,5.12.0,5.11.2,5.11.1,5.10.0,5.9.0,5.8.2,5.8.1,5.7.2,5.7.1,5.7.0,5.6.3,5.5.0,5.4.2
    # for the full list of 5.13.0 free icon classes
    "icons": {
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",
        "auth.Group": "fas fa-users",
    },


    # Icons that are used when one is not manually specified
    "default_icon_parents": "fas fa-chevron-circle-right",
    "default_icon_children": "fas fa-circle",

    #################
    # Related Modal #
    #################

    # Use modals instead of popups
    "related_modal_active": False,

    #############
    # UI Tweaks #
    #############


    # Relative paths to custom CSS/JS scripts (must be present in static files)
    "custom_css": None,
    "custom_js": None,
    # Whether to link font from fonts.googleapis.com (use custom_css to supply font otherwise)
    "use_google_fonts_cdn": True,
    # Whether to show the UI customizer on the sidebar
    "show_ui_builder": False,

}
