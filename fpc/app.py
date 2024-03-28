from parapy.webgui import mui, layout
from parapy.webgui.app_bar import AppBar
from parapy.webgui.core import Component, get_asset_url
from parapy.webgui.mui.themes import DefaultTheme

from fpc.pages.body import Body
from fpc.pages.stepper import Stepper


class App(Component):
    def render(self):
        return mui.ThemeProvider(theme=DefaultTheme)[
            mui.CssBaseline,
            layout.Split(className='main', orientation="vertical", height='100%', weights=[0,0,1],
                         style={'backgroundColor': '#F3F3F3'})[
                AppBar(title="Fugro 4D8D", logoSrc=get_asset_url("logo.png", 1),homeUrl="https://fugro.com"),
                Stepper(),
                Body()
            ],
        ]


if __name__ == '__main__':
    from parapy.webgui.core import display
    display(App, reload=True)
