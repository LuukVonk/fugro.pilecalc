from parapy.webgui import layout, mui
from parapy.webgui.core import Component, NodeType, Prop, State

from fpc.pages.page_home.cpt_map import MapOverview


class RequestedCalculations(Component):
    no_items = Prop(4)
    checked = State(set([0]))

    def render(self) -> NodeType:
        return layout.Box(height='100%',
                          h_align='center',
                          v_align='center')[
            layout.Box(orientation='vertical',
                       style={"maxWidth": 360,
                              'borderRadius': 10,
                              'backgroundColor': '#F8F9F9',
                              'boxShadow': 10,
                              'border': '1px solid #0002'})[
                mui.List(sx={"width": '100%'})[[
                    mui.ListItem(key=n,
                                 disablePadding=True,
                                 secondaryAction=mui.IconButton(edge="end")[
                                     mui.Icon['info']]
                                 )[
                        mui.ListItemButton(role=None,
                                           onClick=lambda evt,
                                                          value_=n: self.handle_toggle(
                                               evt, value_),
                                           dense=True)[
                            mui.ListItemIcon[
                                mui.Checkbox(edge="start",
                                             checked=n in self.checked,
                                             tabIndex=-1,
                                             disableRipple=True)
                            ],
                            mui.ListItemText(id=f"checkbox-list-label-{n}",
                                             primary=f"Calculation type {n + 1}")
                        ]
                    ]
                    for n in range(self.no_items)]]
            ]
        ]

    def handle_toggle(self, evt, value: int) -> None:
        new_checked = set(self.checked)

        if value in new_checked:
            new_checked.remove(value)
        else:
            new_checked.add(value)

        self.checked = new_checked
class ExcavationInstallation(Component):
    no_items = Prop(4)
    checked = State(set([0]))

    def render(self) -> NodeType:
        return layout.Box(height='100%',
                          h_align='center',
                          v_align='center')[
            layout.Box(orientation='vertical',
                       style={"maxWidth": 360,
                              'borderRadius': 10,
                              'backgroundColor': '#F8F9F9',
                              'boxShadow': 10,
                              'border': '1px solid #0002'})[
                mui.List(sx={"width": '100%'})[[
                    mui.ListItem(key=n,
                                 disablePadding=True,
                                 secondaryAction=mui.IconButton(edge="end")[
                                     mui.Icon['info']]
                                 )[
                        mui.ListItemButton(role=None,
                                           onClick=lambda evt,
                                                          value_=n: self.handle_toggle(
                                               evt, value_),
                                           dense=True)[
                            mui.ListItemIcon[
                                mui.Checkbox(edge="start",
                                             checked=n in self.checked,
                                             tabIndex=-1,
                                             disableRipple=True)
                            ],
                            mui.ListItemText(id=f"checkbox-list-label-{n}",
                                             primary=f"Excavation option {n + 1}")
                        ]
                    ]
                    for n in range(self.no_items)]]
            ]
        ]

    def handle_toggle(self, evt, value: int) -> None:
        new_checked = set(self.checked)

        if value in new_checked:
            new_checked.remove(value)
        else:
            new_checked.add(value)

        self.checked = new_checked
class SelectedCpt(Component):
    def render(self) -> NodeType:
        return layout.Box(height='100%',
                          v_align='center',
                          h_align='center',
                          gap='1em',
                          style={'backgroundColor': '#F3F3F3'})[
            mui.Paper(elevation=3,
                      sx={'width':"95%",
                          'padding': 2,
                          'textAlign': 'center'})[
                layout.Split(height="100%",
                             orientation="vertical",
                             weights=[0, 1],
                             h_align="center")[
                    mui.Typography(variant='h6')["Select CPT's for this project"],
                    "Something should be here?!"
                ],
            ],
        ]

class RightBox(Component):

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
                                      'textAlign': 'center'})[
                                        layout.Split(height="100%",
                                                        orientation="vertical",
                                                        weights=[0,0,1,0,1],
                                                        h_align="center")[
                                                            mui.Typography(variant='h5')['General options'],
                                                            mui.Typography(variant='subtitle1')[
                                                                'Calculation options'],
                                                            RequestedCalculations(),
                                                            mui.Typography(
                                                                variant='subtitle1')[
                                                                'Excavation / installation options'],
                                                            ExcavationInstallation()
                                        ],
                ],
        ]

class LeftBox(Component):
    def render(self) -> NodeType:
        return layout.Split(orientation="vertical",
                            height="100%",
                            weights=[1,3])[
            SelectedCpt(),
            MapOverview()
        ]
class PageHome(Component):

    def render(self) -> NodeType:

        return layout.Split(orientation="horizontal",
                            height="100%",
                            weights=[2,1])[
            LeftBox(),
            RightBox()
        ]