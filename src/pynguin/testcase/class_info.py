import logging
import pprint

CREATE_MEMBER = "__create_member__"

_LOGGER = logging.getLogger(__name__)

class ClassInfo:
    def __init__(self):
        self.fields = dict()

    def add_fields(self, field_name: str, field_type: str):
        self.fields[field_name] = field_type

    def diff_fields(self, prev: 'ClassInfo') -> 'ClassInfo':
        diff = {}

        for field_name, field_type in self.fields.items():
            if field_name not in prev.fields:
                diff[field_name] = (CREATE_MEMBER, field_type)
                continue

            prev_field_type = prev.fields.get(field_name)
            if field_type != prev_field_type:
                diff[field_name] = (prev_field_type, field_type)

        return diff

class ClassChangeInfo:
    def __init__(self):
        self.changed_method = dict() # method name -> changed member variable

    def __str__(self):
        return pprint.pformat(self.changed_method, indent=4)
    
    def get(self, method_name: str, default=None):
        return self.changed_method.get(method_name, default)
    
    def merge(self, other):
        for method_name, changed_member in other.changed_method.items():
            if method_name not in self.changed_method:
                self.changed_method[method_name] = changed_member
            else:
                prev_changed_member = self.changed_method.get(method_name)
                for changed_member, type_info in changed_member.items():
                    prev_type_info = prev_changed_member.get(changed_member, set([]))
                    prev_type_info.update(type_info)
                    prev_changed_member[changed_member] = prev_type_info

                self.changed_method[method_name] = prev_changed_member

    def set_prev_class_info(self, prev_class_info: ClassInfo):
        self.prev_class_info = prev_class_info

    def add_changed_method(self, method_name: str, changed_member: str, prev_type: str, new_type: str):
        prev_changed_member = self.changed_method.get(method_name, {})
        type_info = prev_changed_member.get(changed_member, set([]))
        # _LOGGER.info(f"add_changed_method: {method_name}, {changed_member}, {prev_type}, {new_type}")
        type_info.add((prev_type, new_type))

        prev_changed_member[changed_member] = type_info

        self.changed_method[method_name] = prev_changed_member

    def update_changed_info(self, method_name: str, diff_fields: dict):
        for field_name, (prev_type, new_type) in diff_fields.items():
            self.add_changed_method(method_name, field_name, prev_type, new_type)

class ClassesInfo: 
    def __init__(self):
        self.classes = dict() # class name -> (ClassInfo, ClassChangeInfo)

    def __str__(self):
        return pprint.pformat(str(self.classes), indent=4)

    def add_class_info(self, class_name: str, method_name: str, class_info: ClassInfo):
        (prev_class_info, prev_class_change_info) = self.classes.get(class_name, (None, None))

        if prev_class_info is None:
            self.classes[class_name] = (class_info, ClassChangeInfo())
        else:
            diff_fields = class_info.diff_fields(prev_class_info)
            prev_class_change_info.update_changed_info(method_name, diff_fields)

            self.classes[class_name] = (class_info, prev_class_change_info)

    # def merge(self, other: 'ClassesInfo'):
    #     for class_name, (class_info, class_change_info) in other.classes.items():
    #         if class_name not in self.classes:
    #             self.classes[class_name] = (class_info, class_change_info)
    #         else:
    #             prev_class_info, prev_class_change_info = self.classes[class_name]
    #             prev_class_info.merge(class_info)
    #             prev_class_change_info.merge(class_change_info)

    #             self.classes[class_name] = (prev_class_info, prev_class_change_info)


