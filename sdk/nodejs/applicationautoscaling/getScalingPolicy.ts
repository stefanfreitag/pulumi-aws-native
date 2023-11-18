// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::ApplicationAutoScaling::ScalingPolicy
 */
export function getScalingPolicy(args: GetScalingPolicyArgs, opts?: pulumi.InvokeOptions): Promise<GetScalingPolicyResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("aws-native:applicationautoscaling:getScalingPolicy", {
        "arn": args.arn,
        "scalableDimension": args.scalableDimension,
    }, opts);
}

export interface GetScalingPolicyArgs {
    /**
     * ARN is a read only property for the resource.
     */
    arn: string;
    /**
     * The scalable dimension. This string consists of the service namespace, resource type, and scaling property.
     */
    scalableDimension: string;
}

export interface GetScalingPolicyResult {
    /**
     * ARN is a read only property for the resource.
     */
    readonly arn?: string;
    /**
     * The scaling policy type.
     *
     * The following policy types are supported:
     *
     * TargetTrackingScaling Not supported for Amazon EMR
     *
     * StepScaling Not supported for DynamoDB, Amazon Comprehend, Lambda, Amazon Keyspaces, Amazon MSK, Amazon ElastiCache, or Neptune.
     */
    readonly policyType?: string;
    /**
     * A step scaling policy.
     */
    readonly stepScalingPolicyConfiguration?: outputs.applicationautoscaling.ScalingPolicyStepScalingPolicyConfiguration;
    /**
     * A target tracking scaling policy.
     */
    readonly targetTrackingScalingPolicyConfiguration?: outputs.applicationautoscaling.ScalingPolicyTargetTrackingScalingPolicyConfiguration;
}
/**
 * Resource Type definition for AWS::ApplicationAutoScaling::ScalingPolicy
 */
export function getScalingPolicyOutput(args: GetScalingPolicyOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetScalingPolicyResult> {
    return pulumi.output(args).apply((a: any) => getScalingPolicy(a, opts))
}

export interface GetScalingPolicyOutputArgs {
    /**
     * ARN is a read only property for the resource.
     */
    arn: pulumi.Input<string>;
    /**
     * The scalable dimension. This string consists of the service namespace, resource type, and scaling property.
     */
    scalableDimension: pulumi.Input<string>;
}
