// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::ElasticLoadBalancingV2::TargetGroup
 */
export function getTargetGroup(args: GetTargetGroupArgs, opts?: pulumi.InvokeOptions): Promise<GetTargetGroupResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("aws-native:elasticloadbalancingv2:getTargetGroup", {
        "targetGroupArn": args.targetGroupArn,
    }, opts);
}

export interface GetTargetGroupArgs {
    /**
     * The ARN of the Target Group
     */
    targetGroupArn: string;
}

export interface GetTargetGroupResult {
    /**
     * Indicates whether health checks are enabled. If the target type is lambda, health checks are disabled by default but can be enabled. If the target type is instance, ip, or alb, health checks are always enabled and cannot be disabled.
     */
    readonly healthCheckEnabled?: boolean;
    /**
     * The approximate amount of time, in seconds, between health checks of an individual target.
     */
    readonly healthCheckIntervalSeconds?: number;
    /**
     * [HTTP/HTTPS health checks] The destination for health checks on the targets. [HTTP1 or HTTP2 protocol version] The ping path. The default is /. [GRPC protocol version] The path of a custom health check method with the format /package.service/method. The default is /AWS.ALB/healthcheck.
     */
    readonly healthCheckPath?: string;
    /**
     * The port the load balancer uses when performing health checks on targets. 
     */
    readonly healthCheckPort?: string;
    /**
     * The protocol the load balancer uses when performing health checks on targets. 
     */
    readonly healthCheckProtocol?: string;
    /**
     * The amount of time, in seconds, during which no response from a target means a failed health check.
     */
    readonly healthCheckTimeoutSeconds?: number;
    /**
     * The number of consecutive health checks successes required before considering an unhealthy target healthy. 
     */
    readonly healthyThresholdCount?: number;
    /**
     * The Amazon Resource Names (ARNs) of the load balancers that route traffic to this target group.
     */
    readonly loadBalancerArns?: string[];
    /**
     * [HTTP/HTTPS health checks] The HTTP or gRPC codes to use when checking for a successful response from a target.
     */
    readonly matcher?: outputs.elasticloadbalancingv2.TargetGroupMatcher;
    /**
     * The tags.
     */
    readonly tags?: outputs.Tag[];
    /**
     * The ARN of the Target Group
     */
    readonly targetGroupArn?: string;
    /**
     * The attributes.
     */
    readonly targetGroupAttributes?: outputs.elasticloadbalancingv2.TargetGroupAttribute[];
    /**
     * The full name of the target group.
     */
    readonly targetGroupFullName?: string;
    /**
     * The name of the target group.
     */
    readonly targetGroupName?: string;
    /**
     * The targets.
     */
    readonly targets?: outputs.elasticloadbalancingv2.TargetGroupTargetDescription[];
    /**
     * The number of consecutive health check failures required before considering a target unhealthy.
     */
    readonly unhealthyThresholdCount?: number;
}
/**
 * Resource Type definition for AWS::ElasticLoadBalancingV2::TargetGroup
 */
export function getTargetGroupOutput(args: GetTargetGroupOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetTargetGroupResult> {
    return pulumi.output(args).apply((a: any) => getTargetGroup(a, opts))
}

export interface GetTargetGroupOutputArgs {
    /**
     * The ARN of the Target Group
     */
    targetGroupArn: pulumi.Input<string>;
}
