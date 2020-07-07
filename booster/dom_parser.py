#! /usr/bin/python3
# -*- coding: utf-8 -*-
"""Created on Fri May 10 03:47:45 UTC+8:00 2019
    解析器用于解析数据结构, 文档解析器
written by pyleo.
"""
from lxml import etree


class DomParser:
    """文档解析器

    """

    def __init__(self):
        self.logger: any = None  # 日志记录器

    def parse_as_attributes(self, selector: str = "", attribute_name: str = "",
                            selector_syntax: str = "", source_data: str = "") -> tuple:
        """解析元素属性
        :param selector:  选择器 type(css/xpath)
        :param attribute_name:  要解析的属性名称type(id/class/text)
        :param selector_syntax:  选择器语法
        :param source_data:  来源数据
        :return:  tuple
        """
        if not selector or type(selector) is not str or not attribute_name \
                or type(attribute_name) is not str:
            self.logger.info(f"解析属性非法传参(*>﹏<*)【{selector_syntax}】")
            return "", []
        try:
            html_dom = etree.HTML(source_data, parser=etree.HTMLPullParser(encoding="utf-8"))

            if selector == "css":
                elements = html_dom.cssselect(selector_syntax)
            elif selector == "xpath":
                elements = html_dom.xpath(selector_syntax)
            else:
                self.logger.info(f"解析属性非法选择(*>﹏<*)【{selector_syntax}】")
                return "", []
        except Exception as ex:
            self.logger.info(f"解析属性元素失败(*>﹏<*)【{selector_syntax}】")
            self.logger.info(f"解析属性失败原因(*>﹏<*)【{ex}】")
            return "", []
        else:
            if not elements:
                self.logger.info(f"解析属性非法元素(*>﹏<*)【{selector_syntax}】")
                return "", []

            if selector == "css":
                attr_values = []  # 属性返回值列表
                for n, v in enumerate(elements):
                    if attribute_name == "text":  # 判断属性是否是文本
                        element_text = v.text
                        attr_values.append(element_text)
                    else:
                        attribute = v.attrib
                        if attribute_name not in attribute.keys():
                            self.logger.info(f"解析属性返回失败(*>﹏<*)【{selector_syntax}】【{attribute_name}】【{n}】")
                            attribute_value = ""
                        else:
                            attribute_value = attribute.get(attribute_name)
                        attr_values.append(attribute_value)
                return attr_values[0], attr_values
            elif selector == "xpath":
                return_list = []
                for i in elements:
                    return_list.append(str(i))
                return return_list[0], return_list

    def parse_as_batch(self, selector: str = "css", attribute_name: str = "",
                       param_list: list = None, source_data: str = "") -> list:
        """解析批量元素
        :param selector:  选择器 type(css/xpath)
        :param attribute_name:  要解析的属性名称type(id/class/text)
        :param param_list:  传入的参数字典，拼接请求的字符串 ("key", False, "value"),
            "key":  拼接请求参数的key
            False:  是否需要解析type(True/False)
            "value":  需要解析就是语法/不需要解析就是value值
            例子如下:
            [
                ("key", False, "value"),
                ("key", True, "#id"),
            ]
        :param source_data:  来源数据
        :return:  list
        """
        if not selector or type(selector) is not str or not attribute_name \
                or type(attribute_name) is not str or not param_list \
                or type(param_list) is not list or not source_data or type(source_data) is not str:
            self.logger.info("解析批量非法传参(*>﹏<*)【batch】")
            return []

        return_list = []
        for n, v in enumerate(param_list):
            param_key = v[0]  # 需要解析的key
            is_parse = v[1]  # 是否需要解析
            is_value = v[2]  # 是否是值
            if not param_key or type(param_key) is not str or type(is_parse) is not bool:
                self.logger.info(f"解析批量返回失败(*>﹏<*)【{v}】【{n}】")
                continue

            if is_parse is True:
                return_data, temp_list = self.parse_as_attributes(
                    selector, attribute_name, str(is_value), source_data)
                return_list.append((str(param_key), str(return_data)), )
            elif is_parse is False:
                return_list.append((str(param_key), str(is_value)), )
            else:
                self.logger.info(f"解析批量非法名称(*>﹏<*)【{is_parse}】【{n}】")
                return []

        return return_list
