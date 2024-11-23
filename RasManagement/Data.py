import json
import os.path
from docxtpl import DocxTemplate
from InputData import *


class DataRas:
    def __init__(self, json_data: InputData):

        self.results, self.header = \
            json_data.Results, json_data.Header

        self.template = 'C:\\Users\\Dmitry\\PycharmProjects\\RasMaker\\Templates\\Маршрутно-сопроводительный лист для ПИ 026-04.docx'
        self.MSL = DocxTemplate(self.template)
        self.save_dir: str = os.path.join(os.getcwd(), "Templates", "МСЛ", "")

