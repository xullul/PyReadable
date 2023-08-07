from typing import Tuple


size_units: Tuple[Tuple[str, str], ...] = (
    ('B', 'Byte'),
    ('K', 'Kilobyte'),
    ('M', 'Megabyte'),
    ('G', 'Gigabyte'),
    ('T', 'Terabyte'),
    ('P', 'Petrabyte'),
    ('E', 'Exabyte'),
    ('Z', 'Zettabyte')
)

class Readable:
    
    class Size:
        size: int | float
        
        def __init__(self, size):
            self.size = self.get_size(size)
            
        def get_size(self, size) -> int | float:
            if isinstance(size, int) or isinstance(size, float):
                return size
            else:
                raise TypeError('size must be integer or float')
        
        def readable_size(self, size: int | float, full: bool = False):
            for unit in size_units:
                if abs(size) < 1024:
                    u = unit[1] if (full == True) else unit[0]
                    s = '{:.2f}'.format(size)
                    return f'{s} {u}'
                else:
                    size /= 1024