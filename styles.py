import qdarktheme

qss = """
    QPushButton[cssClass="specialButton"] {
        color: #fff;
        background: #1e81b0;
    }
    QPushButton[cssClass="specialButton"]:hover {
        color: #fff;
        background: #16656a;
    }
    QPushButton[cssClass="specialButton"]:pressed {
        color: #fff;
        background: #115270;
    }
"""

def setupTheme():
    qdarktheme.setup_theme(
        theme='dark',
        corner_shape='rounded',
        custom_colors={
            "[dark]":{
                "primary": "#1e81b0"
            },
            "[light]":{
                "primary": "#1e81b0"
            }
        },
        additional_qss = qss
    )