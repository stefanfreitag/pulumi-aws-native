// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::ElasticLoadBalancingV2::LoadBalancer
 */
export function getLoadBalancer(args: GetLoadBalancerArgs, opts?: pulumi.InvokeOptions): Promise<GetLoadBalancerResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("aws-native:elasticloadbalancingv2:getLoadBalancer", {
        "id": args.id,
    }, opts);
}

export interface GetLoadBalancerArgs {
    id: string;
}

export interface GetLoadBalancerResult {
    readonly canonicalHostedZoneID?: string;
    readonly dNSName?: string;
    readonly id?: string;
    readonly ipAddressType?: string;
    readonly loadBalancerAttributes?: outputs.elasticloadbalancingv2.LoadBalancerAttribute[];
    readonly loadBalancerFullName?: string;
    readonly loadBalancerName?: string;
    readonly securityGroups?: string[];
    readonly subnetMappings?: outputs.elasticloadbalancingv2.LoadBalancerSubnetMapping[];
    readonly subnets?: string[];
    readonly tags?: outputs.elasticloadbalancingv2.LoadBalancerTag[];
}
/**
 * Resource Type definition for AWS::ElasticLoadBalancingV2::LoadBalancer
 */
export function getLoadBalancerOutput(args: GetLoadBalancerOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetLoadBalancerResult> {
    return pulumi.output(args).apply((a: any) => getLoadBalancer(a, opts))
}

export interface GetLoadBalancerOutputArgs {
    id: pulumi.Input<string>;
}
