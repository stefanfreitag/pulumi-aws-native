// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::SecretsManager::ResourcePolicy
 */
export function getResourcePolicy(args: GetResourcePolicyArgs, opts?: pulumi.InvokeOptions): Promise<GetResourcePolicyResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("aws-native:secretsmanager:getResourcePolicy", {
        "id": args.id,
    }, opts);
}

export interface GetResourcePolicyArgs {
    id: string;
}

export interface GetResourcePolicyResult {
    readonly blockPublicPolicy?: boolean;
    readonly id?: string;
    /**
     * Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::SecretsManager::ResourcePolicy` for more information about the expected schema for this property.
     */
    readonly resourcePolicy?: any;
}
/**
 * Resource Type definition for AWS::SecretsManager::ResourcePolicy
 */
export function getResourcePolicyOutput(args: GetResourcePolicyOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetResourcePolicyResult> {
    return pulumi.output(args).apply((a: any) => getResourcePolicy(a, opts))
}

export interface GetResourcePolicyOutputArgs {
    id: pulumi.Input<string>;
}
