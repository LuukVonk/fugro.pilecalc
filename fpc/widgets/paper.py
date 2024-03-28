from parapy.webgui import layout, mui
from parapy.webgui.core import NodeType, Component


class FPaper(Component):

    def render(self) -> NodeType:
        return layout.Box(height='100%',
                                      v_align='center',
                                      h_align='center',
                                      gap='1 em',
                                      )[
                                mui.Paper(elevation=3,
                                             sx={'width': 500,
                                                  'height': 750,
                                                  'padding': 2,
                                                  'textAlign': 'center'})[*self.children]]