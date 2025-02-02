// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * The ``AWS::EFS::MountTarget`` resource is an Amazon EFS resource that creates a mount target for an EFS file system. You can then mount the file system on Amazon EC2 instances or other resources by using the mount target.
 */
export function getMountTarget(args: GetMountTargetArgs, opts?: pulumi.InvokeOptions): Promise<GetMountTargetResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("aws-native:efs:getMountTarget", {
        "id": args.id,
    }, opts);
}

export interface GetMountTargetArgs {
    id: string;
}

export interface GetMountTargetResult {
    readonly id?: string;
    /**
     * Up to five VPC security group IDs, of the form ``sg-xxxxxxxx``. These must be for the same VPC as subnet specified.
     */
    readonly securityGroups?: string[];
}
/**
 * The ``AWS::EFS::MountTarget`` resource is an Amazon EFS resource that creates a mount target for an EFS file system. You can then mount the file system on Amazon EC2 instances or other resources by using the mount target.
 */
export function getMountTargetOutput(args: GetMountTargetOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetMountTargetResult> {
    return pulumi.output(args).apply((a: any) => getMountTarget(a, opts))
}

export interface GetMountTargetOutputArgs {
    id: pulumi.Input<string>;
}
