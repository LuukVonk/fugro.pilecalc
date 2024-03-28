from parapy.webgui import plotly, layout, mui
from parapy.webgui.core import Component, NodeType, State
from parapy.webgui.mui import Input

from fpc.widgets.paper import FPaper


class PreliminaryAnalysis(Component):
    def render(self) -> NodeType:
        return layout.Split(orientation="horizontal",
                            height="100%",
                            weights=[1,2])[
            LeftPanel(),
            RightPanel()
        ]



class LeftPanel(Component):
    expanded = State(set(['panel1']))

    level_from: float = Input(0)
    level_till: float = Input(-10)
    def render_heights(self):
        return layout.Split(orientation='vertical')[
            'Select the range for the calculation',
            mui.Input(placeholder='from',
                      type='number',
                      defaultValue= self.level_from,
                      endAdornment='m+NAP',
                      inputProps={'aria-label':'weight'}),
            mui.Input(placeholder='till',
                      endAdornment='m+NAP')
        ]
    def accordion(self):
        return [mui.Accordion(expanded='panel1' in self.expanded,
                          onChange=lambda evt, panel: self.handle_change(evt, 'panel1'))[
                mui.AccordionSummary(expandIcon=mui.Icon['expand_more_icon'])[
                    mui.Typography(sx={'width': '75%',
                                       'flexShrink': 0},
                                   variant='h6')['Calculation levels']
                ],
                mui.AccordionDetails[
                    self.render_heights()
                ]
            ],
            mui.Accordion(expanded='panel2' in self.expanded,
                          onChange=lambda evt, panel: self.handle_change(evt, 'panel2'))[
                mui.AccordionSummary(expandIcon=mui.Icon['expand_more_icon'])[
                    mui.Typography(sx={'width': '75%',
                                       'flexShrink': 0},
                                   variant='h6')['Piles']
                ],
                mui.AccordionDetails[
                    PileTree()
                ]
            ],
            mui.Accordion(expanded='panel3' in self.expanded,
                          onChange=lambda evt, panel: self.handle_change(evt, 'panel3'))[
                mui.AccordionSummary(expandIcon=mui.Icon['expand_more_icon'])[
                    mui.Typography(sx={'width': '75%',
                                       'flexShrink': 0},
                                   variant='h6')["CPT's"]
                ],
                mui.AccordionDetails[
                    CptTree()
                ]
            ],
            ]

    def handle_change(self, evt, panel: str):
        new_expanded = set(self.expanded)

        if panel in self.expanded:
            new_expanded.remove(panel)
        else:
            new_expanded.add(panel)

        self.expanded = new_expanded


    def render(self) -> NodeType:
        return layout.Box(height='100%',
                          v_align='top',
                          h_align='center',
                          orientation='vertical',
                          gap='1 em',
                          style={'padding':'2em'}
                          )[ self.accordion()]



class RightPanel(Component):
    def render(self) -> NodeType:
        return plotly.Plot(
            data=[
                {"x": [1, 2, 3, 4, 5], "y": [1, 2, 4, 8, 16]},
                {"x": [1, 2, 3, 4, 5], "y": [1, 3, 6, 9, 12]},
            ],
            layout={
                "title": 'Calculated bearing capacity',
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

class CptTree(Component):
    expanded_nodes: list[str] = State(default_factory=list)
    selected_nodes: list[str] = State(default_factory=list)
    num_cpt:int = State(10)

    def render(self) -> NodeType:
        return [
                mui.TreeView(
                    defaultCollapseIcon=mui.Icon['expand_more_icon'],
                    defaultExpandIcon=mui.Icon['chevron_right_icon'],
                    expanded=self.expanded_nodes,
                    selected=self.selected_nodes,
                    onNodeToggle=self.on_expanded_change,
                    onNodeSelect=self.on_selection_change,
                    multiSelect=True
                )[self.render_tree_item()
                ],
            layout.Split(gap='1em')[
                mui.Button(onClick=self.deselect_all,
                           variant='contained',
                           fullWidth=True,
                           size='small')[
                    f"Deselect all"
                ],
                mui.Button(onClick=self.select_all,
                           variant='contained',
                           fullWidth=True,
                           size='small')[
                    f"Select all"
                ],
            ],
        ]

    def render_tree_item(self):
        return [mui.TreeItem(nodeId=f"{index}", label=f"CPT{index}",
                             icon=mui.Icon()['check_box_outlined' if str(index) in self.selected_nodes else 'check_box_outline_blank'],
                             classes={'backgroundColor':'red'})
            for index in range(self.num_cpt)
        ]

    def deselect_all(self, *args):
        self.selected_nodes = []

    def select_all(self, *args):
        self.selected_nodes = list(map(str, range(0, self.num_cpt)))

    def on_expanded_change(self, evt, items):
        self.expanded_nodes = items

    def on_selection_change(self, evt, items):
        new_list = self.selected_nodes
        for item in items:
            if item in self.selected_nodes:
                new_list = [x for x in new_list if x != item]
            elif item not in self.selected_nodes:
                new_list = new_list + [item]

        self.selected_nodes = new_list


class PileTree(Component):
    expanded_nodes: list[str] = State(default_factory=list)
    selected_nodes: list[str] = State(default_factory=list)
    num_cpt:int = State(10)

    def render(self) -> NodeType:
        return [
                mui.TreeView(
                    defaultCollapseIcon=mui.Icon['expand_more_icon'],
                    defaultExpandIcon=mui.Icon['chevron_right_icon'],
                    expanded=self.expanded_nodes,
                    selected=self.selected_nodes,
                    onNodeToggle=self.on_expanded_change,
                    onNodeSelect=self.on_selection_change,
                    multiSelect=True
                )[self.render_tree_item()
                ],
            layout.Split(gap='1em')[
                mui.Button(onClick=self.deselect_all,
                           variant='contained',
                           fullWidth=True,
                           size='small')[
                    f"Deselect all"
                ],
                mui.Button(onClick=self.select_all,
                           variant='contained',
                           fullWidth=True,
                           size='small')[
                    f"Select all"
                ],
            ],
        ]

    def render_tree_item(self):
        return [mui.TreeItem(nodeId=f"{index}", label=f"Pile {index}",
                             icon=mui.Icon()['check_box_outlined' if str(index) in self.selected_nodes else 'check_box_outline_blank'],
                             classes={'backgroundColor':'red'})
            for index in range(self.num_cpt)
        ]

    def deselect_all(self, *args):
        self.selected_nodes = []

    def select_all(self, *args):
        self.selected_nodes = list(map(str, range(0, self.num_cpt)))

    def on_expanded_change(self, evt, items):
        self.expanded_nodes = items

    def on_selection_change(self, evt, items):
        new_list = self.selected_nodes
        for item in items:
            if item in self.selected_nodes:
                new_list = [x for x in new_list if x != item]
            elif item not in self.selected_nodes:
                new_list = new_list + [item]

        self.selected_nodes = new_list
