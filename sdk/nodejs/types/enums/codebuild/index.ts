// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***


export const FleetComputeType = {
    BuildGeneral1Small: "BUILD_GENERAL1_SMALL",
    BuildGeneral1Medium: "BUILD_GENERAL1_MEDIUM",
    BuildGeneral1Large: "BUILD_GENERAL1_LARGE",
    BuildGeneral12xlarge: "BUILD_GENERAL1_2XLARGE",
} as const;

export type FleetComputeType = (typeof FleetComputeType)[keyof typeof FleetComputeType];

export const FleetEnvironmentType = {
    WindowsServer2019Container: "WINDOWS_SERVER_2019_CONTAINER",
    WindowsServer2022Container: "WINDOWS_SERVER_2022_CONTAINER",
    LinuxContainer: "LINUX_CONTAINER",
    LinuxGpuContainer: "LINUX_GPU_CONTAINER",
    ArmContainer: "ARM_CONTAINER",
} as const;

export type FleetEnvironmentType = (typeof FleetEnvironmentType)[keyof typeof FleetEnvironmentType];
