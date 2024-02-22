// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::EC2::NetworkAcl
 */
export function getNetworkAcl(args: GetNetworkAclArgs, opts?: pulumi.InvokeOptions): Promise<GetNetworkAclResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("aws-native:ec2:getNetworkAcl", {
        "id": args.id,
    }, opts);
}

export interface GetNetworkAclArgs {
    id: string;
}

export interface GetNetworkAclResult {
    readonly id?: string;
    /**
     * The tags to assign to the network ACL.
     */
    readonly tags?: outputs.Tag[];
}
/**
 * Resource Type definition for AWS::EC2::NetworkAcl
 */
export function getNetworkAclOutput(args: GetNetworkAclOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetNetworkAclResult> {
    return pulumi.output(args).apply((a: any) => getNetworkAcl(a, opts))
}

export interface GetNetworkAclOutputArgs {
    id: pulumi.Input<string>;
}
