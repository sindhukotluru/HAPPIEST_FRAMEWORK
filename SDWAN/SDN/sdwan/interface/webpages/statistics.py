import time
from SDN.sdwan.interface.webpages.base import BasePage

class Statistics(BasePage):

    SECTION_NAME = 'Statistics'
    FLOW_TABLE_STATISTICS_MENU_XPATH = "//a[@href='#flowtablestatistics']"
    FLOW_TABLE_XPATH = "//table[@id='flow_table']"
    FLOW_TABLE_HEADER_XPATH = FLOW_TABLE_XPATH + "/thead[@id='flowtable_header']/tr"
    FLOW_TABLE_BODY_XPATH = FLOW_TABLE_XPATH + "/tbody[@id='flows_tbody']"

    SERVICE_HEADER = 'Service'
    TABLEID_HEADER = 'Table Id'
    FLOWID_HEADER = 'Flow Id'
    PRIORITY_HEADER = 'Priority'
    INPUT_HEADER = 'Input'
    OUTPUT_HEADER = 'Output'

    def navigate_to_statistics_section(self):
        self.navigate_to_section(name=Statistics.SECTION_NAME)
        time.sleep(5)

    def navigate_to_flow_table_statistics(self):
        self.gui_driver.driver.find_element_by_xpath(self.FLOW_TABLE_STATISTICS_MENU_XPATH).click()
        time.sleep(5)

    def get_flow_table_information(self):
        table_records = []
        elem = self.gui_driver.driver.find_element_by_xpath(self.FLOW_TABLE_HEADER_XPATH)
        table_headers = [header.text for header in elem.find_elements_by_tag_name('th')]

        elem = self.gui_driver.driver.find_element_by_xpath(self.FLOW_TABLE_BODY_XPATH)
        row_elems = elem.find_elements_by_tag_name('tr')
        time.sleep(5)
        for elem in row_elems:
            records = [value.text for value in elem.find_elements_by_tag_name("td")]
            table_records.append({table_headers[index]:records[index] for index in range(len(table_headers))})

        return table_records




