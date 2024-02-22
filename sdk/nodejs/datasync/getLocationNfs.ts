// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Resource schema for AWS::DataSync::LocationNFS
 */
export function getLocationNfs(args: GetLocationNfsArgs, opts?: pulumi.InvokeOptions): Promise<GetLocationNfsResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("aws-native:datasync:getLocationNfs", {
        "locationArn": args.locationArn,
    }, opts);
}

export interface GetLocationNfsArgs {
    /**
     * The Amazon Resource Name (ARN) of the NFS location.
     */
    locationArn: string;
}

export interface GetLocationNfsResult {
    /**
     * The Amazon Resource Name (ARN) of the NFS location.
     */
    readonly locationArn?: string;
    /**
     * The URL of the NFS location that was described.
     */
    readonly locationUri?: string;
    readonly mountOptions?: outputs.datasync.LocationNfsMountOptions;
    readonly onPremConfig?: outputs.datasync.LocationNfsOnPremConfig;
    /**
     * An array of key-value pairs to apply to this resource.
     */
    readonly tags?: outputs.Tag[];
}
/**
 * Resource schema for AWS::DataSync::LocationNFS
 */
export function getLocationNfsOutput(args: GetLocationNfsOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetLocationNfsResult> {
    return pulumi.output(args).apply((a: any) => getLocationNfs(a, opts))
}

export interface GetLocationNfsOutputArgs {
    /**
     * The Amazon Resource Name (ARN) of the NFS location.
     */
    locationArn: pulumi.Input<string>;
}
