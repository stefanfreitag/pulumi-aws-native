// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * resource definition
 */
export function getSoftwarePackageVersion(args: GetSoftwarePackageVersionArgs, opts?: pulumi.InvokeOptions): Promise<GetSoftwarePackageVersionResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("aws-native:iot:getSoftwarePackageVersion", {
        "packageName": args.packageName,
        "versionName": args.versionName,
    }, opts);
}

export interface GetSoftwarePackageVersionArgs {
    packageName: string;
    versionName: string;
}

export interface GetSoftwarePackageVersionResult {
    readonly attributes?: outputs.iot.SoftwarePackageVersionResourceAttributes;
    readonly description?: string;
    readonly errorReason?: string;
    readonly packageVersionArn?: string;
    readonly status?: enums.iot.SoftwarePackageVersionPackageVersionStatus;
    /**
     * An array of key-value pairs to apply to this resource.
     */
    readonly tags?: outputs.Tag[];
}
/**
 * resource definition
 */
export function getSoftwarePackageVersionOutput(args: GetSoftwarePackageVersionOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetSoftwarePackageVersionResult> {
    return pulumi.output(args).apply((a: any) => getSoftwarePackageVersion(a, opts))
}

export interface GetSoftwarePackageVersionOutputArgs {
    packageName: pulumi.Input<string>;
    versionName: pulumi.Input<string>;
}
