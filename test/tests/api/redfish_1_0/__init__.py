# import tests
from chassis_tests import ChassisTests 
from systems_tests import SystemsTests 
from task_service_tests import TaskServiceTests
from registry_tests import RegistryTests
from schema_tests import SchemaTests
from session_service_tests import SessionServiceTests
from event_service_tests import EventServiceTests

tests = [
    'redfish.chassis.tests',
    'redfish.systems.tests',
    'redfish.task_service.tests',
    'redfish.registry.tests',
    'redfish.schema.tests',
    'redfish.event_service.tests',
    'redfish.session_service.tests'
]
