from enum import Enum


class EndpointsDemoq(Enum):
    # Elements
    TEXT_BOX = "/text-box"
    CHECKBOX = "/checkbox"
    RADIO_BUTTON = "/radio-button"
    WEB_TABLES = "/webtables"
    BUTTONS = "/buttons"
    LINKS = "/links"
    BROKEN_LINKS = "/broken"
    UPLOAD_DOWNLOAD = "/upload-download"
    DYNAMIC_PROPERTIES = "/dynamic-properties"

    # Forms
    AUTOMATION_PRACTICE_FORM = "/automation-practice-form"

    # Alerts, Frame And Windows
    BROWSER_WINDOWS = "/browser-windows"
    ALERTS = "/alerts"
    FRAMES = "/frames"
    NESTED_FRAMES = "/nestedframes"
    MODAL_DIALOGS = "/modal-dialogs"

    # Widgets
    ACCORDIAN = "/accordian"
    AUTO_COMPLETE = "/auto-complete"
    DATE_PICKER = "/date-picker"
    SLIDER = "/slider"
    PROGRESS_BAR = "/progress-bar"
    TABS = "/tabs"
    TOOL_TIPS = "/tool-tips"
    MENU = "/menu"
    SELECT_MENU = "/select-menu"

    # Interactions
    SORTABLE = "/sortable"
    SELECTABLE = "/selectable"
    RESIZABLE = "/resizable"
    DROPPABLE = "/droppable"
    DRAGABBLE = "/dragabble"

    # Book Store Application
    LOGIN = "/login"
    BOOKS_STORE = "/books"
    PROFILE = "/profile"
