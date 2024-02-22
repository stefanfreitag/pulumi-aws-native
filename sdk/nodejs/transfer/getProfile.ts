// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::Transfer::Profile
 */
export function getProfile(args: GetProfileArgs, opts?: pulumi.InvokeOptions): Promise<GetProfileResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("aws-native:transfer:getProfile", {
        "profileId": args.profileId,
    }, opts);
}

export interface GetProfileArgs {
    /**
     * A unique identifier for the profile
     */
    profileId: string;
}

export interface GetProfileResult {
    /**
     * Specifies the unique Amazon Resource Name (ARN) for the profile.
     */
    readonly arn?: string;
    /**
     * AS2 identifier agreed with a trading partner.
     */
    readonly as2Id?: string;
    /**
     * List of the certificate IDs associated with this profile to be used for encryption and signing of AS2 messages.
     */
    readonly certificateIds?: string[];
    /**
     * A unique identifier for the profile
     */
    readonly profileId?: string;
    /**
     * An array of key-value pairs to apply to this resource.
     */
    readonly tags?: outputs.Tag[];
}
/**
 * Resource Type definition for AWS::Transfer::Profile
 */
export function getProfileOutput(args: GetProfileOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetProfileResult> {
    return pulumi.output(args).apply((a: any) => getProfile(a, opts))
}

export interface GetProfileOutputArgs {
    /**
     * A unique identifier for the profile
     */
    profileId: pulumi.Input<string>;
}
