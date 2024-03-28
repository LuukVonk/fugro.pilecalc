from parapy.webgui.core import Component, NodeType

from fpc.pages.page_cpt.page_cpt import PageCpt
from fpc.pages.page_cpt.page_customize import PageCustomize
from fpc.pages.page_home.page_home import PageHome
from fpc.pages.page_piles.page_piles import PagePiles
from fpc.pages.page_preanalysis.page_preanalysis import PreliminaryAnalysis
from fpc.store import STORE


class Body(Component):
    def render(self) -> NodeType:

        if STORE.page == 0:
            body_page = PageHome()
        elif STORE.page == 1:
            body_page = PageCpt()
        elif STORE.page == 1.5:
            body_page = PageCustomize()
        elif STORE.page == 2:
            body_page = PagePiles()
        elif STORE.page == 3:
            body_page = PreliminaryAnalysis()
        else:
            body_page = "Under construction"

        return body_page
