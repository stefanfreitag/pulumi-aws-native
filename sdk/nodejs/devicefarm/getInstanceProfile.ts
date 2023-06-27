// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * AWS::DeviceFarm::InstanceProfile creates a new Device Farm Instance Profile
 */
export function getInstanceProfile(args: GetInstanceProfileArgs, opts?: pulumi.InvokeOptions): Promise<GetInstanceProfileResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("aws-native:devicefarm:getInstanceProfile", {
        "arn": args.arn,
    }, opts);
}

export interface GetInstanceProfileArgs {
    arn: string;
}

export interface GetInstanceProfileResult {
    readonly arn?: string;
    readonly description?: string;
    readonly excludeAppPackagesFromCleanup?: string[];
    readonly name?: string;
    readonly packageCleanup?: boolean;
    readonly rebootAfterUse?: boolean;
    readonly tags?: outputs.devicefarm.InstanceProfileTag[];
}
/**
 * AWS::DeviceFarm::InstanceProfile creates a new Device Farm Instance Profile
 */
export function getInstanceProfileOutput(args: GetInstanceProfileOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetInstanceProfileResult> {
    return pulumi.output(args).apply((a: any) => getInstanceProfile(a, opts))
}

export interface GetInstanceProfileOutputArgs {
    arn: pulumi.Input<string>;
}
