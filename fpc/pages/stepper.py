from parapy.webgui import layout, mui
from parapy.webgui.core import Component, NodeType

from fpc.store import STORE


class Stepper(Component):
    steps = ["Home",
             "CPT",
             "Pile Geometry",
             "Preliminary Analysis",
             "Analysis",
             "Output"]

    def _on_click_stepper(self,page,*kwargs):
        STORE.page = page

    def render(self) -> NodeType:
        return layout.Box(gap='1em',
                          height='100%',
                          v_align='center',
                          orientation='vertical',
                          style={'padding': '2em'},
                          width="100%")[
            mui.Stepper(activeStep=STORE.page,
                        alternativeLabel=True,
                        nonLinear=True)[[
                mui.Step(key=step,
                         )[
                    mui.StepLabel(onClick=lambda evt, idx = index: self._on_click_stepper(idx))[step]
                ]
                for index, step in enumerate(self.steps)]
            ],
        ]
