from model import Person
from error import Error
from typing import Dict, List

id2record: Dict[str, List[Person]] = {}


def process(record: Person):
    if record.objectInfo is None:
        return
    for m in record.family.member:
        detecting_objects = str(m.objectInfo.get('监测对象类别'))
        urban_insurance = str(m.objectInfo.get('是否参加城乡居民基本养老保险'))
        if detecting_objects != '' and urban_insurance == '':
            raise Error(no='5_15_001', objectInfo=[record.objectInfo])




