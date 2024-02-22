// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * The AWS::MemoryDB::SubnetGroup resource creates an Amazon MemoryDB Subnet Group.
 */
export function getSubnetGroup(args: GetSubnetGroupArgs, opts?: pulumi.InvokeOptions): Promise<GetSubnetGroupResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("aws-native:memorydb:getSubnetGroup", {
        "subnetGroupName": args.subnetGroupName,
    }, opts);
}

export interface GetSubnetGroupArgs {
    /**
     * The name of the subnet group. This value must be unique as it also serves as the subnet group identifier.
     */
    subnetGroupName: string;
}

export interface GetSubnetGroupResult {
    /**
     * The Amazon Resource Name (ARN) of the subnet group.
     */
    readonly arn?: string;
    /**
     * An optional description of the subnet group.
     */
    readonly description?: string;
    /**
     * A list of VPC subnet IDs for the subnet group.
     */
    readonly subnetIds?: string[];
    /**
     * An array of key-value pairs to apply to this subnet group.
     */
    readonly tags?: outputs.Tag[];
}
/**
 * The AWS::MemoryDB::SubnetGroup resource creates an Amazon MemoryDB Subnet Group.
 */
export function getSubnetGroupOutput(args: GetSubnetGroupOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetSubnetGroupResult> {
    return pulumi.output(args).apply((a: any) => getSubnetGroup(a, opts))
}

export interface GetSubnetGroupOutputArgs {
    /**
     * The name of the subnet group. This value must be unique as it also serves as the subnet group identifier.
     */
    subnetGroupName: pulumi.Input<string>;
}
