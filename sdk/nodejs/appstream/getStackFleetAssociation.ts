// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::AppStream::StackFleetAssociation
 */
export function getStackFleetAssociation(args: GetStackFleetAssociationArgs, opts?: pulumi.InvokeOptions): Promise<GetStackFleetAssociationResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("aws-native:appstream:getStackFleetAssociation", {
        "id": args.id,
    }, opts);
}

export interface GetStackFleetAssociationArgs {
    id: string;
}

export interface GetStackFleetAssociationResult {
    readonly fleetName?: string;
    readonly id?: string;
    readonly stackName?: string;
}
/**
 * Resource Type definition for AWS::AppStream::StackFleetAssociation
 */
export function getStackFleetAssociationOutput(args: GetStackFleetAssociationOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetStackFleetAssociationResult> {
    return pulumi.output(args).apply((a: any) => getStackFleetAssociation(a, opts))
}

export interface GetStackFleetAssociationOutputArgs {
    id: pulumi.Input<string>;
}
