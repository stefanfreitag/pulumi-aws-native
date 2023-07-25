// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***


export const CapacityProviderAutoScalingGroupProviderManagedTerminationProtection = {
    Disabled: "DISABLED",
    Enabled: "ENABLED",
} as const;

export type CapacityProviderAutoScalingGroupProviderManagedTerminationProtection = (typeof CapacityProviderAutoScalingGroupProviderManagedTerminationProtection)[keyof typeof CapacityProviderAutoScalingGroupProviderManagedTerminationProtection];

export const CapacityProviderManagedScalingStatus = {
    Disabled: "DISABLED",
    Enabled: "ENABLED",
} as const;

export type CapacityProviderManagedScalingStatus = (typeof CapacityProviderManagedScalingStatus)[keyof typeof CapacityProviderManagedScalingStatus];

export const ClusterCapacityProviderAssociationsCapacityProvider = {
    Fargate: "FARGATE",
    FargateSpot: "FARGATE_SPOT",
} as const;

/**
 * If using ec2 auto-scaling, the name of the associated capacity provider. Otherwise FARGATE, FARGATE_SPOT.
 */
export type ClusterCapacityProviderAssociationsCapacityProvider = (typeof ClusterCapacityProviderAssociationsCapacityProvider)[keyof typeof ClusterCapacityProviderAssociationsCapacityProvider];

export const ClusterCapacityProviderAssociationsCapacityProvider0 = {
    Fargate: "FARGATE",
    FargateSpot: "FARGATE_SPOT",
} as const;

/**
 * If using ec2 auto-scaling, the name of the associated capacity provider. Otherwise FARGATE, FARGATE_SPOT.
 */
export type ClusterCapacityProviderAssociationsCapacityProvider0 = (typeof ClusterCapacityProviderAssociationsCapacityProvider0)[keyof typeof ClusterCapacityProviderAssociationsCapacityProvider0];

export const ServiceAwsVpcConfigurationAssignPublicIp = {
    Disabled: "DISABLED",
    Enabled: "ENABLED",
} as const;

export type ServiceAwsVpcConfigurationAssignPublicIp = (typeof ServiceAwsVpcConfigurationAssignPublicIp)[keyof typeof ServiceAwsVpcConfigurationAssignPublicIp];

export const ServiceDeploymentControllerType = {
    CodeDeploy: "CODE_DEPLOY",
    Ecs: "ECS",
    External: "EXTERNAL",
} as const;

export type ServiceDeploymentControllerType = (typeof ServiceDeploymentControllerType)[keyof typeof ServiceDeploymentControllerType];

export const ServiceLaunchType = {
    Ec2: "EC2",
    Fargate: "FARGATE",
    External: "EXTERNAL",
} as const;

export type ServiceLaunchType = (typeof ServiceLaunchType)[keyof typeof ServiceLaunchType];

export const ServicePlacementConstraintType = {
    DistinctInstance: "distinctInstance",
    MemberOf: "memberOf",
} as const;

export type ServicePlacementConstraintType = (typeof ServicePlacementConstraintType)[keyof typeof ServicePlacementConstraintType];

export const ServicePlacementStrategyType = {
    Binpack: "binpack",
    Random: "random",
    Spread: "spread",
} as const;

export type ServicePlacementStrategyType = (typeof ServicePlacementStrategyType)[keyof typeof ServicePlacementStrategyType];

export const ServicePropagateTags = {
    Service: "SERVICE",
    TaskDefinition: "TASK_DEFINITION",
} as const;

export type ServicePropagateTags = (typeof ServicePropagateTags)[keyof typeof ServicePropagateTags];

export const ServiceSchedulingStrategy = {
    Daemon: "DAEMON",
    Replica: "REPLICA",
} as const;

export type ServiceSchedulingStrategy = (typeof ServiceSchedulingStrategy)[keyof typeof ServiceSchedulingStrategy];

export const TaskDefinitionAuthorizationConfigIAM = {
    Enabled: "ENABLED",
    Disabled: "DISABLED",
} as const;

export type TaskDefinitionAuthorizationConfigIAM = (typeof TaskDefinitionAuthorizationConfigIAM)[keyof typeof TaskDefinitionAuthorizationConfigIAM];

export const TaskDefinitionEFSVolumeConfigurationTransitEncryption = {
    Enabled: "ENABLED",
    Disabled: "DISABLED",
} as const;

export type TaskDefinitionEFSVolumeConfigurationTransitEncryption = (typeof TaskDefinitionEFSVolumeConfigurationTransitEncryption)[keyof typeof TaskDefinitionEFSVolumeConfigurationTransitEncryption];

export const TaskDefinitionPortMappingAppProtocol = {
    Http: "http",
    Http2: "http2",
    Grpc: "grpc",
} as const;

export type TaskDefinitionPortMappingAppProtocol = (typeof TaskDefinitionPortMappingAppProtocol)[keyof typeof TaskDefinitionPortMappingAppProtocol];

export const TaskSetAwsVpcConfigurationAssignPublicIp = {
    Disabled: "DISABLED",
    Enabled: "ENABLED",
} as const;

/**
 * Whether the task's elastic network interface receives a public IP address. The default value is DISABLED.
 */
export type TaskSetAwsVpcConfigurationAssignPublicIp = (typeof TaskSetAwsVpcConfigurationAssignPublicIp)[keyof typeof TaskSetAwsVpcConfigurationAssignPublicIp];

export const TaskSetLaunchType = {
    Ec2: "EC2",
    Fargate: "FARGATE",
} as const;

/**
 * The launch type that new tasks in the task set will use. For more information, see https://docs.aws.amazon.com/AmazonECS/latest/developerguide/launch_types.html in the Amazon Elastic Container Service Developer Guide. 
 */
export type TaskSetLaunchType = (typeof TaskSetLaunchType)[keyof typeof TaskSetLaunchType];

export const TaskSetScaleUnit = {
    Percent: "PERCENT",
} as const;

/**
 * The unit of measure for the scale value.
 */
export type TaskSetScaleUnit = (typeof TaskSetScaleUnit)[keyof typeof TaskSetScaleUnit];
