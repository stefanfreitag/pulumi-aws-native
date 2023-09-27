// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Macie CustomDataIdentifier resource schema
 */
export function getCustomDataIdentifier(args: GetCustomDataIdentifierArgs, opts?: pulumi.InvokeOptions): Promise<GetCustomDataIdentifierResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("aws-native:macie:getCustomDataIdentifier", {
        "id": args.id,
    }, opts);
}

export interface GetCustomDataIdentifierArgs {
    /**
     * Custom data identifier ID.
     */
    id: string;
}

export interface GetCustomDataIdentifierResult {
    /**
     * Custom data identifier ARN.
     */
    readonly arn?: string;
    /**
     * Custom data identifier ID.
     */
    readonly id?: string;
    /**
     * A collection of tags associated with a resource
     */
    readonly tags?: outputs.macie.CustomDataIdentifierTag[];
}
/**
 * Macie CustomDataIdentifier resource schema
 */
export function getCustomDataIdentifierOutput(args: GetCustomDataIdentifierOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetCustomDataIdentifierResult> {
    return pulumi.output(args).apply((a: any) => getCustomDataIdentifier(a, opts))
}

export interface GetCustomDataIdentifierOutputArgs {
    /**
     * Custom data identifier ID.
     */
    id: pulumi.Input<string>;
}
