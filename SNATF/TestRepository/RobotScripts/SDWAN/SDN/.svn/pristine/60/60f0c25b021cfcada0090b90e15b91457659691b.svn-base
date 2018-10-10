import unittest
from SDN import config
from SDN.sdwan.interface.webpages.pages import Pages
from SDN.core.interface.web_interface import WebInterface
from SDN.core.utils.common_types import BrowserType
from SDN.sdwan.interface.webpages.configure import SERVICE_TYPE, LINK_TYPE

class TestSDWANPage(unittest.TestCase):

    def test_configure_page(self):
        self.sdwan_page = Pages(WebInterface(browser=BrowserType.CHROME))
        self.sdwan_page.base_page.browse_url(url=config.BASE_PAGE_URL)

        self.sdwan_page.configure_page.navigate_to_configure_section()
        self.sdwan_page.configure_page.configure_service(service=SERVICE_TYPE.SSH,
                                                         link_type=LINK_TYPE.MPLS)
        self.sdwan_page.configure_page.configure_service(service=SERVICE_TYPE.ARP,
                                                        link_type=LINK_TYPE.MPLS)

        self.sdwan_page.topology_page.navigate_to_topology_section()
        self.sdwan_page.topology_page.reload_topology_view()

        self.sdwan_page.statistics_page.navigate_to_statistics_section()
        self.sdwan_page.statistics_page.navigate_to_flow_table_statistics()
        self.sdwan_page.statistics_page.get_flow_table_information()




