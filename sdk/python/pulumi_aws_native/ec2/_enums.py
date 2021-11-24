# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'CapacityReservationFleetInstanceMatchCriteria',
    'CapacityReservationFleetTenancy',
    'EC2FleetCapacityRebalanceReplacementStrategy',
    'EC2FleetCapacityReservationOptionsRequestUsageStrategy',
    'EC2FleetExcessCapacityTerminationPolicy',
    'EC2FleetInstanceRequirementsRequestAcceleratorManufacturersItem',
    'EC2FleetInstanceRequirementsRequestAcceleratorNamesItem',
    'EC2FleetInstanceRequirementsRequestAcceleratorTypesItem',
    'EC2FleetInstanceRequirementsRequestBareMetal',
    'EC2FleetInstanceRequirementsRequestBurstablePerformance',
    'EC2FleetInstanceRequirementsRequestCpuManufacturersItem',
    'EC2FleetInstanceRequirementsRequestInstanceGenerationsItem',
    'EC2FleetInstanceRequirementsRequestLocalStorage',
    'EC2FleetInstanceRequirementsRequestLocalStorageTypesItem',
    'EC2FleetSpotOptionsRequestAllocationStrategy',
    'EC2FleetSpotOptionsRequestInstanceInterruptionBehavior',
    'EC2FleetTagSpecificationResourceType',
    'EC2FleetTargetCapacitySpecificationRequestDefaultTargetCapacityType',
    'EC2FleetTargetCapacitySpecificationRequestTargetCapacityUnitType',
    'EC2FleetType',
    'FlowLogLogDestinationType',
    'FlowLogResourceType',
    'FlowLogTrafficType',
    'NetworkInsightsAnalysisStatus',
    'NetworkInsightsPathProtocol',
    'PrefixListAddressFamily',
    'SpotFleetEbsBlockDeviceVolumeType',
    'SpotFleetInstanceRequirementsRequestAcceleratorManufacturersItem',
    'SpotFleetInstanceRequirementsRequestAcceleratorNamesItem',
    'SpotFleetInstanceRequirementsRequestAcceleratorTypesItem',
    'SpotFleetInstanceRequirementsRequestBareMetal',
    'SpotFleetInstanceRequirementsRequestBurstablePerformance',
    'SpotFleetInstanceRequirementsRequestCpuManufacturersItem',
    'SpotFleetInstanceRequirementsRequestInstanceGenerationsItem',
    'SpotFleetInstanceRequirementsRequestLocalStorage',
    'SpotFleetInstanceRequirementsRequestLocalStorageTypesItem',
    'SpotFleetRequestConfigDataAllocationStrategy',
    'SpotFleetRequestConfigDataExcessCapacityTerminationPolicy',
    'SpotFleetRequestConfigDataInstanceInterruptionBehavior',
    'SpotFleetRequestConfigDataTargetCapacityUnitType',
    'SpotFleetRequestConfigDataType',
    'SpotFleetSpotCapacityRebalanceReplacementStrategy',
    'SpotFleetSpotPlacementTenancy',
    'SpotFleetTagSpecificationResourceType',
    'VPCEndpointVpcEndpointType',
]


class CapacityReservationFleetInstanceMatchCriteria(str, Enum):
    OPEN = "open"


class CapacityReservationFleetTenancy(str, Enum):
    DEFAULT = "default"


class EC2FleetCapacityRebalanceReplacementStrategy(str, Enum):
    LAUNCH = "launch"
    LAUNCH_BEFORE_TERMINATE = "launch-before-terminate"


class EC2FleetCapacityReservationOptionsRequestUsageStrategy(str, Enum):
    USE_CAPACITY_RESERVATIONS_FIRST = "use-capacity-reservations-first"


class EC2FleetExcessCapacityTerminationPolicy(str, Enum):
    TERMINATION = "termination"
    NO_TERMINATION = "no-termination"


class EC2FleetInstanceRequirementsRequestAcceleratorManufacturersItem(str, Enum):
    NVIDIA = "nvidia"
    AMD = "amd"
    AMAZON_WEB_SERVICES = "amazon-web-services"
    XILINX = "xilinx"


class EC2FleetInstanceRequirementsRequestAcceleratorNamesItem(str, Enum):
    A100 = "a100"
    V100 = "v100"
    K80 = "k80"
    T4 = "t4"
    M60 = "m60"
    RADEON_PRO_V520 = "radeon-pro-v520"
    VU9P = "vu9p"
    INFERENTIA = "inferentia"
    K520 = "k520"


class EC2FleetInstanceRequirementsRequestAcceleratorTypesItem(str, Enum):
    GPU = "gpu"
    FPGA = "fpga"
    INFERENCE = "inference"


class EC2FleetInstanceRequirementsRequestBareMetal(str, Enum):
    INCLUDED = "included"
    REQUIRED = "required"
    EXCLUDED = "excluded"


class EC2FleetInstanceRequirementsRequestBurstablePerformance(str, Enum):
    INCLUDED = "included"
    REQUIRED = "required"
    EXCLUDED = "excluded"


class EC2FleetInstanceRequirementsRequestCpuManufacturersItem(str, Enum):
    INTEL = "intel"
    AMD = "amd"
    AMAZON_WEB_SERVICES = "amazon-web-services"


class EC2FleetInstanceRequirementsRequestInstanceGenerationsItem(str, Enum):
    CURRENT = "current"
    PREVIOUS = "previous"


class EC2FleetInstanceRequirementsRequestLocalStorage(str, Enum):
    INCLUDED = "included"
    REQUIRED = "required"
    EXCLUDED = "excluded"


class EC2FleetInstanceRequirementsRequestLocalStorageTypesItem(str, Enum):
    HDD = "hdd"
    SSD = "ssd"


class EC2FleetSpotOptionsRequestAllocationStrategy(str, Enum):
    LOWEST_PRICE = "lowestPrice"
    DIVERSIFIED = "diversified"
    CAPACITY_OPTIMIZED = "capacityOptimized"
    CAPACITY_OPTIMIZED_PRIORITIZED = "capacityOptimizedPrioritized"


class EC2FleetSpotOptionsRequestInstanceInterruptionBehavior(str, Enum):
    HIBERNATE = "hibernate"
    STOP = "stop"
    TERMINATE = "terminate"


class EC2FleetTagSpecificationResourceType(str, Enum):
    CLIENT_VPN_ENDPOINT = "client-vpn-endpoint"
    CUSTOMER_GATEWAY = "customer-gateway"
    DEDICATED_HOST = "dedicated-host"
    DHCP_OPTIONS = "dhcp-options"
    EGRESS_ONLY_INTERNET_GATEWAY = "egress-only-internet-gateway"
    ELASTIC_GPU = "elastic-gpu"
    ELASTIC_IP = "elastic-ip"
    EXPORT_IMAGE_TASK = "export-image-task"
    EXPORT_INSTANCE_TASK = "export-instance-task"
    FLEET = "fleet"
    FPGA_IMAGE = "fpga-image"
    HOST_RESERVATION = "host-reservation"
    IMAGE = "image"
    IMPORT_IMAGE_TASK = "import-image-task"
    IMPORT_SNAPSHOT_TASK = "import-snapshot-task"
    INSTANCE = "instance"
    INTERNET_GATEWAY = "internet-gateway"
    KEY_PAIR = "key-pair"
    LAUNCH_TEMPLATE = "launch-template"
    LOCAL_GATEWAY_ROUTE_TABLE_VPC_ASSOCIATION = "local-gateway-route-table-vpc-association"
    NATGATEWAY = "natgateway"
    NETWORK_ACL = "network-acl"
    NETWORK_INSIGHTS_ANALYSIS = "network-insights-analysis"
    NETWORK_INSIGHTS_PATH = "network-insights-path"
    NETWORK_INTERFACE = "network-interface"
    PLACEMENT_GROUP = "placement-group"
    RESERVED_INSTANCES = "reserved-instances"
    ROUTE_TABLE = "route-table"
    SECURITY_GROUP = "security-group"
    SNAPSHOT = "snapshot"
    SPOT_FLEET_REQUEST = "spot-fleet-request"
    SPOT_INSTANCES_REQUEST = "spot-instances-request"
    SUBNET = "subnet"
    TRAFFIC_MIRROR_FILTER = "traffic-mirror-filter"
    TRAFFIC_MIRROR_SESSION = "traffic-mirror-session"
    TRAFFIC_MIRROR_TARGET = "traffic-mirror-target"
    TRANSIT_GATEWAY = "transit-gateway"
    TRANSIT_GATEWAY_ATTACHMENT = "transit-gateway-attachment"
    TRANSIT_GATEWAY_CONNECT_PEER = "transit-gateway-connect-peer"
    TRANSIT_GATEWAY_MULTICAST_DOMAIN = "transit-gateway-multicast-domain"
    TRANSIT_GATEWAY_ROUTE_TABLE = "transit-gateway-route-table"
    VOLUME = "volume"
    VPC = "vpc"
    VPC_FLOW_LOG = "vpc-flow-log"
    VPC_PEERING_CONNECTION = "vpc-peering-connection"
    VPN_CONNECTION = "vpn-connection"
    VPN_GATEWAY = "vpn-gateway"


class EC2FleetTargetCapacitySpecificationRequestDefaultTargetCapacityType(str, Enum):
    ON_DEMAND = "on-demand"
    SPOT = "spot"


class EC2FleetTargetCapacitySpecificationRequestTargetCapacityUnitType(str, Enum):
    VCPU = "vcpu"
    MEMORY_MIB = "memory-mib"
    UNITS = "units"


class EC2FleetType(str, Enum):
    MAINTAIN = "maintain"
    REQUEST = "request"
    INSTANT = "instant"


class FlowLogLogDestinationType(str, Enum):
    """
    Specifies the type of destination to which the flow log data is to be published. Flow log data can be published to CloudWatch Logs or Amazon S3.
    """
    CLOUD_WATCH_LOGS = "cloud-watch-logs"
    S3 = "s3"


class FlowLogResourceType(str, Enum):
    """
    The type of resource for which to create the flow log. For example, if you specified a VPC ID for the ResourceId property, specify VPC for this property.
    """
    NETWORK_INTERFACE = "NetworkInterface"
    SUBNET = "Subnet"
    VPC = "VPC"


class FlowLogTrafficType(str, Enum):
    """
    The type of traffic to log. You can log traffic that the resource accepts or rejects, or all traffic.
    """
    ACCEPT = "ACCEPT"
    ALL = "ALL"
    REJECT = "REJECT"


class NetworkInsightsAnalysisStatus(str, Enum):
    RUNNING = "running"
    FAILED = "failed"
    SUCCEEDED = "succeeded"


class NetworkInsightsPathProtocol(str, Enum):
    TCP = "tcp"
    UDP = "udp"


class PrefixListAddressFamily(str, Enum):
    """
    Ip Version of Prefix List.
    """
    I_PV4 = "IPv4"
    I_PV6 = "IPv6"


class SpotFleetEbsBlockDeviceVolumeType(str, Enum):
    GP2 = "gp2"
    GP3 = "gp3"
    IO1 = "io1"
    IO2 = "io2"
    SC1 = "sc1"
    ST1 = "st1"
    STANDARD = "standard"


class SpotFleetInstanceRequirementsRequestAcceleratorManufacturersItem(str, Enum):
    NVIDIA = "nvidia"
    AMD = "amd"
    AMAZON_WEB_SERVICES = "amazon-web-services"
    XILINX = "xilinx"


class SpotFleetInstanceRequirementsRequestAcceleratorNamesItem(str, Enum):
    A100 = "a100"
    V100 = "v100"
    K80 = "k80"
    T4 = "t4"
    M60 = "m60"
    RADEON_PRO_V520 = "radeon-pro-v520"
    VU9P = "vu9p"
    INFERENTIA = "inferentia"
    K520 = "k520"


class SpotFleetInstanceRequirementsRequestAcceleratorTypesItem(str, Enum):
    GPU = "gpu"
    FPGA = "fpga"
    INFERENCE = "inference"


class SpotFleetInstanceRequirementsRequestBareMetal(str, Enum):
    INCLUDED = "included"
    REQUIRED = "required"
    EXCLUDED = "excluded"


class SpotFleetInstanceRequirementsRequestBurstablePerformance(str, Enum):
    INCLUDED = "included"
    REQUIRED = "required"
    EXCLUDED = "excluded"


class SpotFleetInstanceRequirementsRequestCpuManufacturersItem(str, Enum):
    INTEL = "intel"
    AMD = "amd"
    AMAZON_WEB_SERVICES = "amazon-web-services"


class SpotFleetInstanceRequirementsRequestInstanceGenerationsItem(str, Enum):
    CURRENT = "current"
    PREVIOUS = "previous"


class SpotFleetInstanceRequirementsRequestLocalStorage(str, Enum):
    INCLUDED = "included"
    REQUIRED = "required"
    EXCLUDED = "excluded"


class SpotFleetInstanceRequirementsRequestLocalStorageTypesItem(str, Enum):
    HDD = "hdd"
    SSD = "ssd"


class SpotFleetRequestConfigDataAllocationStrategy(str, Enum):
    CAPACITY_OPTIMIZED = "capacityOptimized"
    CAPACITY_OPTIMIZED_PRIORITIZED = "capacityOptimizedPrioritized"
    DIVERSIFIED = "diversified"
    LOWEST_PRICE = "lowestPrice"


class SpotFleetRequestConfigDataExcessCapacityTerminationPolicy(str, Enum):
    DEFAULT = "Default"
    NO_TERMINATION = "NoTermination"


class SpotFleetRequestConfigDataInstanceInterruptionBehavior(str, Enum):
    HIBERNATE = "hibernate"
    STOP = "stop"
    TERMINATE = "terminate"


class SpotFleetRequestConfigDataTargetCapacityUnitType(str, Enum):
    VCPU = "vcpu"
    MEMORY_MIB = "memory-mib"
    UNITS = "units"


class SpotFleetRequestConfigDataType(str, Enum):
    MAINTAIN = "maintain"
    REQUEST = "request"


class SpotFleetSpotCapacityRebalanceReplacementStrategy(str, Enum):
    LAUNCH = "launch"
    LAUNCH_BEFORE_TERMINATE = "launch-before-terminate"


class SpotFleetSpotPlacementTenancy(str, Enum):
    DEDICATED = "dedicated"
    DEFAULT = "default"
    HOST = "host"


class SpotFleetTagSpecificationResourceType(str, Enum):
    CLIENT_VPN_ENDPOINT = "client-vpn-endpoint"
    CUSTOMER_GATEWAY = "customer-gateway"
    DEDICATED_HOST = "dedicated-host"
    DHCP_OPTIONS = "dhcp-options"
    EGRESS_ONLY_INTERNET_GATEWAY = "egress-only-internet-gateway"
    ELASTIC_GPU = "elastic-gpu"
    ELASTIC_IP = "elastic-ip"
    EXPORT_IMAGE_TASK = "export-image-task"
    EXPORT_INSTANCE_TASK = "export-instance-task"
    FLEET = "fleet"
    FPGA_IMAGE = "fpga-image"
    HOST_RESERVATION = "host-reservation"
    IMAGE = "image"
    IMPORT_IMAGE_TASK = "import-image-task"
    IMPORT_SNAPSHOT_TASK = "import-snapshot-task"
    INSTANCE = "instance"
    INTERNET_GATEWAY = "internet-gateway"
    KEY_PAIR = "key-pair"
    LAUNCH_TEMPLATE = "launch-template"
    LOCAL_GATEWAY_ROUTE_TABLE_VPC_ASSOCIATION = "local-gateway-route-table-vpc-association"
    NATGATEWAY = "natgateway"
    NETWORK_ACL = "network-acl"
    NETWORK_INSIGHTS_ANALYSIS = "network-insights-analysis"
    NETWORK_INSIGHTS_PATH = "network-insights-path"
    NETWORK_INTERFACE = "network-interface"
    PLACEMENT_GROUP = "placement-group"
    RESERVED_INSTANCES = "reserved-instances"
    ROUTE_TABLE = "route-table"
    SECURITY_GROUP = "security-group"
    SNAPSHOT = "snapshot"
    SPOT_FLEET_REQUEST = "spot-fleet-request"
    SPOT_INSTANCES_REQUEST = "spot-instances-request"
    SUBNET = "subnet"
    TRAFFIC_MIRROR_FILTER = "traffic-mirror-filter"
    TRAFFIC_MIRROR_SESSION = "traffic-mirror-session"
    TRAFFIC_MIRROR_TARGET = "traffic-mirror-target"
    TRANSIT_GATEWAY = "transit-gateway"
    TRANSIT_GATEWAY_ATTACHMENT = "transit-gateway-attachment"
    TRANSIT_GATEWAY_CONNECT_PEER = "transit-gateway-connect-peer"
    TRANSIT_GATEWAY_MULTICAST_DOMAIN = "transit-gateway-multicast-domain"
    TRANSIT_GATEWAY_ROUTE_TABLE = "transit-gateway-route-table"
    VOLUME = "volume"
    VPC = "vpc"
    VPC_FLOW_LOG = "vpc-flow-log"
    VPC_PEERING_CONNECTION = "vpc-peering-connection"
    VPN_CONNECTION = "vpn-connection"
    VPN_GATEWAY = "vpn-gateway"


class VPCEndpointVpcEndpointType(str, Enum):
    INTERFACE = "Interface"
    GATEWAY = "Gateway"
    GATEWAY_LOAD_BALANCER = "GatewayLoadBalancer"
