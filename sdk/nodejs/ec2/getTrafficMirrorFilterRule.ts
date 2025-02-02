// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::EC2::TrafficMirrorFilterRule
 */
export function getTrafficMirrorFilterRule(args: GetTrafficMirrorFilterRuleArgs, opts?: pulumi.InvokeOptions): Promise<GetTrafficMirrorFilterRuleResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("aws-native:ec2:getTrafficMirrorFilterRule", {
        "id": args.id,
    }, opts);
}

export interface GetTrafficMirrorFilterRuleArgs {
    id: string;
}

export interface GetTrafficMirrorFilterRuleResult {
    readonly description?: string;
    readonly destinationCidrBlock?: string;
    readonly destinationPortRange?: outputs.ec2.TrafficMirrorFilterRuleTrafficMirrorPortRange;
    readonly id?: string;
    readonly protocol?: number;
    readonly ruleAction?: string;
    readonly ruleNumber?: number;
    readonly sourceCidrBlock?: string;
    readonly sourcePortRange?: outputs.ec2.TrafficMirrorFilterRuleTrafficMirrorPortRange;
    readonly trafficDirection?: string;
}
/**
 * Resource Type definition for AWS::EC2::TrafficMirrorFilterRule
 */
export function getTrafficMirrorFilterRuleOutput(args: GetTrafficMirrorFilterRuleOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetTrafficMirrorFilterRuleResult> {
    return pulumi.output(args).apply((a: any) => getTrafficMirrorFilterRule(a, opts))
}

export interface GetTrafficMirrorFilterRuleOutputArgs {
    id: pulumi.Input<string>;
}
