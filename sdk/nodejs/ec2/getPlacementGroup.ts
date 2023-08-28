// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::EC2::PlacementGroup
 */
export function getPlacementGroup(args: GetPlacementGroupArgs, opts?: pulumi.InvokeOptions): Promise<GetPlacementGroupResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("aws-native:ec2:getPlacementGroup", {
        "groupName": args.groupName,
    }, opts);
}

export interface GetPlacementGroupArgs {
    /**
     * The Group Name of Placement Group.
     */
    groupName: string;
}

export interface GetPlacementGroupResult {
    /**
     * The Group Name of Placement Group.
     */
    readonly groupName?: string;
}
/**
 * Resource Type definition for AWS::EC2::PlacementGroup
 */
export function getPlacementGroupOutput(args: GetPlacementGroupOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetPlacementGroupResult> {
    return pulumi.output(args).apply((a: any) => getPlacementGroup(a, opts))
}

export interface GetPlacementGroupOutputArgs {
    /**
     * The Group Name of Placement Group.
     */
    groupName: pulumi.Input<string>;
}
