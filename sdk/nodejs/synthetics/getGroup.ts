// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::Synthetics::Group
 */
export function getGroup(args: GetGroupArgs, opts?: pulumi.InvokeOptions): Promise<GetGroupResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("aws-native:synthetics:getGroup", {
        "name": args.name,
    }, opts);
}

export interface GetGroupArgs {
    /**
     * Name of the group.
     */
    name: string;
}

export interface GetGroupResult {
    /**
     * Id of the group.
     */
    readonly id?: string;
    readonly resourceArns?: string[];
    readonly tags?: outputs.Tag[];
}
/**
 * Resource Type definition for AWS::Synthetics::Group
 */
export function getGroupOutput(args: GetGroupOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetGroupResult> {
    return pulumi.output(args).apply((a: any) => getGroup(a, opts))
}

export interface GetGroupOutputArgs {
    /**
     * Name of the group.
     */
    name: pulumi.Input<string>;
}
