// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::IoT1Click::Placement
 */
export function getPlacement(args: GetPlacementArgs, opts?: pulumi.InvokeOptions): Promise<GetPlacementResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("aws-native:iot1click:getPlacement", {
        "id": args.id,
    }, opts);
}

export interface GetPlacementArgs {
    id: string;
}

export interface GetPlacementResult {
    /**
     * Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::IoT1Click::Placement` for more information about the expected schema for this property.
     */
    readonly attributes?: any;
    readonly id?: string;
}
/**
 * Resource Type definition for AWS::IoT1Click::Placement
 */
export function getPlacementOutput(args: GetPlacementOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetPlacementResult> {
    return pulumi.output(args).apply((a: any) => getPlacement(a, opts))
}

export interface GetPlacementOutputArgs {
    id: pulumi.Input<string>;
}
