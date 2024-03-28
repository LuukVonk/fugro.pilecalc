from parapy.webgui import layout, mui, plotly
from parapy.webgui.core import Component, NodeType

from fpc.pages.page_home.cpt_map import MapOverview
from fpc.store import STORE


class CurrentCptBox(Component):
    def render(self) -> NodeType:
        return layout.Box(height='100%',
                       v_align='center',
                       h_align='center',
                       gap='1em',
                       )[
                mui.Paper(elevation=3,
                          sx={'width': "95%",
                              'height':"95%",
                              'padding': 2,
                              'textAlign': 'center'})[
                    layout.Split(orientation="vertical",
                                 height="100%",
                                 weights=[0,1,0])[
                        mui.Typography(variant="h6")['Select current CPT'],
                        MapOverview(),
                        layout.Box(h_align='center', style={'padding': '1em'})[
                            mui.Grid(container=True, spacing=4)[[
                                mui.Grid(item=True, xs=12, sm=8)[
                                    "Ground water level for CPT"
                                ],
                                mui.Grid(item=True, xs=12, sm=4)[
                                    mui.Button(variant='contained')['Reset ALL']
                                ],
                                mui.Grid(item=True, xs=12, sm=8)[
                                    "Zones for negative skin friction"
                                ],
                                mui.Grid(item=True, xs=12, sm=4)[
                                    mui.Button(variant='contained')['Reset ALL']
                                ]

                            ]]
                        ]

        ]]]

class CptPlot(Component):
    def render(self) -> NodeType:
       return plotly.Plot(
            data=[
                {"x": [1, 2, 3, 4, 5], "y": [1, 2, 4, 8, 16]},
                {"x": [1, 2, 3, 4, 5], "y": [1, 3, 6, 9, 12]},
            ],
            layout={
                "title": 'Selected CPT is plotted here',
                "xaxis": {"title": 'Time [s]'},
                "yaxis": {"title": 'Response [m]'}
            },
           style={
               'display': 'flex',
               'justifyContent': 'center',
               'width': '100%',
               'height': '100%'
           }
        )

class CptInterpretationPlot(Component):

    def _on_click_custom(self,*args):
        STORE.page = 1.5

    def _on_click_interpreation(self,*args):
        print('interpretation')


    def render(self) -> NodeType:
       return layout.Split(orientation='vertical',
                           height='100%',
                           style={'gap':'1em',
                                  'padding':'0.5em'},
                           weights=[1,0])[plotly.Plot(
            data=[
                {"x": [1, 2, 3, 4, 5], "y": [1, 2, 4, 8, 16]},
                {"x": [1, 2, 3, 4, 5], "y": [1, 3, 6, 9, 12]},
            ],
            layout={
                "title": 'CPT interpretation is plotted here',
                "xaxis": {"title": 'Time [s]'},
                "yaxis": {"title": 'Response [m]'}
            },
           style={
               'display': 'flex',
               'justifyContent': 'center',
               'width': '100%',
               'height': '100%'
           }
        ),
       layout.Split(gap='1em')[
           mui.Button(onClick=self._on_click_custom,
                      variant='contained',
                      fullWidth=True,
                      size='small')[
               f"Custom"
           ],
           mui.Button(onClick=self._on_click_interpreation,
                      variant='contained',
                      fullWidth=True,
                      size='small')[
               f"Interpretation rule"
           ]
       ],
       ]

class StressesPlot(Component):
    def render(self) -> NodeType:
       return plotly.Plot(
            data=[
                {"x": [1, 2, 3, 4, 5], "y": [1, 2, 4, 8, 16]},
                {"x": [1, 2, 3, 4, 5], "y": [1, 3, 6, 9, 12]},
            ],
            layout={
                "title": 'Stresses are plotted here',
                "xaxis": {"title": 'Time [s]'},
                "yaxis": {"title": 'Response [m]'}
            },
           style={
               'display': 'flex',
               'justifyContent': 'center',
               'width': '100%',
               'height': '100%'
           }
        )
class PageCpt(Component):

    def render(self) -> NodeType:
        return layout.Split(orientation="horizontal",
                            height="100%",
                            weights=[1,1,1,1])[
            CptPlot(),
            CptInterpretationPlot(),
            StressesPlot(),
            CurrentCptBox()
        ]