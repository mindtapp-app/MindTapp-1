try:
	from .prod_settings import *
except ImportError as e:
	from .dev_settings import *