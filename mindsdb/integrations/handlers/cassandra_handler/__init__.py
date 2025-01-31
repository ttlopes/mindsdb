from mindsdb.integrations.libs.const import HANDLER_TYPE

try:
    from .cassandra_handler import CassandraHandler as Handler,  connection_args
    import_error = None
except Exception as e:
    Handler = None
    import_error = e
from .__about__ import __version__ as version, __description__ as description


title = 'Cassandra'
name = 'cassandra'
type = HANDLER_TYPE.DATA
icon_path = 'icon.svg'

__all__ = [
    'Handler', 'version', 'name', 'type', 'title', 'description',
    'connection_args', 'import_error', 'icon_path'
]
