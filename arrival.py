toolbar_helper = """
Screen:
    NavigationLayout:
        ScreenManager:
            Screen:
                BoxLayout:
                    orientation: 'vertical'
                    MDToolbar:
                        title: "Covid App"
                        elevation: 10
                        left_action_items: [['menu', lambda x: nav_drawer.set_state()]]
                    Widget:
        MDNavigationDrawer:
            id: nav_drawer

            BoxLayout:
                orientation: 'vertical'

                MDLabel:
                    text: 'Username'
                    font_style: 'Caption'
                MDLabel:
                    text: 'Location'
                    font_style: 'Caption'                            
"""