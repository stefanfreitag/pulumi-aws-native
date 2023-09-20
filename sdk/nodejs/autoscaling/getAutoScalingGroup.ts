// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::AutoScaling::AutoScalingGroup
 */
export function getAutoScalingGroup(args: GetAutoScalingGroupArgs, opts?: pulumi.InvokeOptions): Promise<GetAutoScalingGroupResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("aws-native:autoscaling:getAutoScalingGroup", {
        "id": args.id,
    }, opts);
}

export interface GetAutoScalingGroupArgs {
    id: string;
}

export interface GetAutoScalingGroupResult {
    readonly availabilityZones?: string[];
    readonly capacityRebalance?: boolean;
    readonly context?: string;
    readonly cooldown?: string;
    readonly defaultInstanceWarmup?: number;
    readonly desiredCapacity?: string;
    readonly desiredCapacityType?: string;
    readonly healthCheckGracePeriod?: number;
    readonly healthCheckType?: string;
    readonly id?: string;
    readonly instanceMaintenancePolicy?: outputs.autoscaling.AutoScalingGroupInstanceMaintenancePolicy;
    readonly launchConfigurationName?: string;
    readonly launchTemplate?: outputs.autoscaling.AutoScalingGroupLaunchTemplateSpecification;
    readonly lifecycleHookSpecificationList?: outputs.autoscaling.AutoScalingGroupLifecycleHookSpecification[];
    readonly loadBalancerNames?: string[];
    readonly maxInstanceLifetime?: number;
    readonly maxSize?: string;
    readonly metricsCollection?: outputs.autoscaling.AutoScalingGroupMetricsCollection[];
    readonly minSize?: string;
    readonly mixedInstancesPolicy?: outputs.autoscaling.AutoScalingGroupMixedInstancesPolicy;
    readonly newInstancesProtectedFromScaleIn?: boolean;
    readonly notificationConfigurations?: outputs.autoscaling.AutoScalingGroupNotificationConfiguration[];
    readonly placementGroup?: string;
    readonly serviceLinkedRoleArn?: string;
    readonly tags?: outputs.autoscaling.AutoScalingGroupTagProperty[];
    readonly targetGroupArns?: string[];
    readonly terminationPolicies?: string[];
    readonly vpcZoneIdentifier?: string[];
}
/**
 * Resource Type definition for AWS::AutoScaling::AutoScalingGroup
 */
export function getAutoScalingGroupOutput(args: GetAutoScalingGroupOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetAutoScalingGroupResult> {
    return pulumi.output(args).apply((a: any) => getAutoScalingGroup(a, opts))
}

export interface GetAutoScalingGroupOutputArgs {
    id: pulumi.Input<string>;
}
