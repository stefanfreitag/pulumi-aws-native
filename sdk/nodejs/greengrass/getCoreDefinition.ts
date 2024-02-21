// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::Greengrass::CoreDefinition
 */
export function getCoreDefinition(args: GetCoreDefinitionArgs, opts?: pulumi.InvokeOptions): Promise<GetCoreDefinitionResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("aws-native:greengrass:getCoreDefinition", {
        "id": args.id,
    }, opts);
}

export interface GetCoreDefinitionArgs {
    id: string;
}

export interface GetCoreDefinitionResult {
    readonly arn?: string;
    readonly id?: string;
    readonly latestVersionArn?: string;
    readonly name?: string;
    /**
     * Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::Greengrass::CoreDefinition` for more information about the expected schema for this property.
     */
    readonly tags?: any;
}
/**
 * Resource Type definition for AWS::Greengrass::CoreDefinition
 */
export function getCoreDefinitionOutput(args: GetCoreDefinitionOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetCoreDefinitionResult> {
    return pulumi.output(args).apply((a: any) => getCoreDefinition(a, opts))
}

export interface GetCoreDefinitionOutputArgs {
    id: pulumi.Input<string>;
}
