// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Publishes new or first hook version to AWS CloudFormation Registry.
 */
export function getHookVersion(args: GetHookVersionArgs, opts?: pulumi.InvokeOptions): Promise<GetHookVersionResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("aws-native:cloudformation:getHookVersion", {
        "arn": args.arn,
    }, opts);
}

export interface GetHookVersionArgs {
    /**
     * The Amazon Resource Name (ARN) of the type, here the HookVersion. This is used to uniquely identify a HookVersion resource
     */
    arn: string;
}

export interface GetHookVersionResult {
    /**
     * The Amazon Resource Name (ARN) of the type, here the HookVersion. This is used to uniquely identify a HookVersion resource
     */
    readonly arn?: string;
    /**
     * Indicates if this type version is the current default version
     */
    readonly isDefaultVersion?: boolean;
    /**
     * The Amazon Resource Name (ARN) of the type without the versionID.
     */
    readonly typeArn?: string;
    /**
     * The ID of the version of the type represented by this hook instance.
     */
    readonly versionId?: string;
    /**
     * The scope at which the type is visible and usable in CloudFormation operations.
     *
     * Valid values include:
     *
     * PRIVATE: The type is only visible and usable within the account in which it is registered. Currently, AWS CloudFormation marks any types you register as PRIVATE.
     *
     * PUBLIC: The type is publically visible and usable within any Amazon account.
     */
    readonly visibility?: enums.cloudformation.HookVersionVisibility;
}
/**
 * Publishes new or first hook version to AWS CloudFormation Registry.
 */
export function getHookVersionOutput(args: GetHookVersionOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetHookVersionResult> {
    return pulumi.output(args).apply((a: any) => getHookVersion(a, opts))
}

export interface GetHookVersionOutputArgs {
    /**
     * The Amazon Resource Name (ARN) of the type, here the HookVersion. This is used to uniquely identify a HookVersion resource
     */
    arn: pulumi.Input<string>;
}
