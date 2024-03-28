from parapy.webgui import layout, mui, html
from parapy.webgui.core import Component, NodeType, Prop, State, get_asset_url

from fpc.widgets.paper import FPaper


class PagePiles(Component):
    def render(self) -> NodeType:
        return layout.Split(orientation="horizontal",
                            height="100%",
                            weights=[1,3])[
            PileList(),
            PileDetails()
        ]


class PileDetails(Component):
    def render(self) -> NodeType:
        return layout.Box(v_align='center',
                          h_align='center',
                          height="100%",
                          )[html.img(src=get_asset_url('cpt_truck.jpg'),
                     alt='CPT truck.',
                     height=750,
                     style={'border': '2px solid white',
                            'borderRadius': 5}
                     )]


class PileList(Component):
    no_items = Prop(12)
    checked = State(set([0]))


    def list_of_piles(self):
        return layout.Box(#height='100%',
                          width='100%',
                          h_align='center',
                          v_align='center')[
            layout.Box(orientation='vertical',
                       style={"maxWidth": 500,
                              'borderRadius': 10,
                              'height':'100%',
                              'backgroundColor': '#F8F9F9',
                              'boxShadow': 10,
                              'border': '1px solid #0002'})[
                mui.Typography(variant='h6',
                               sx={'padding-left':'15px'})['Select piletypes'],
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
                                             primary=f"Concrete pile of type {n + 1}")
                        ]
                    ]
                    for n in range(self.no_items)]]
            ]
        ]

    def render(self) -> NodeType:
        return layout.Split(orientation="vertical",
                            height="100%",
                            v_align="top",
                            style={'padding':"2em"},
                            weights=[1,0])[
            self.list_of_piles(),
            mui.Button(variant='contained')[mui.Icon()['upload'], 'Import piletypes']
        ]

    def handle_toggle(self, evt, value: int) -> None:
        new_checked = set(self.checked)

        if value in new_checked:
            new_checked.remove(value)
        else:
            new_checked.add(value)

        self.checked = new_checked