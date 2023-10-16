// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * The AWS::EC2::VerifiedAccessTrustProvider type describes a verified access trust provider
 */
export function getVerifiedAccessTrustProvider(args: GetVerifiedAccessTrustProviderArgs, opts?: pulumi.InvokeOptions): Promise<GetVerifiedAccessTrustProviderResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("aws-native:ec2:getVerifiedAccessTrustProvider", {
        "verifiedAccessTrustProviderId": args.verifiedAccessTrustProviderId,
    }, opts);
}

export interface GetVerifiedAccessTrustProviderArgs {
    /**
     * The ID of the Amazon Web Services Verified Access trust provider.
     */
    verifiedAccessTrustProviderId: string;
}

export interface GetVerifiedAccessTrustProviderResult {
    /**
     * The creation time.
     */
    readonly creationTime?: string;
    /**
     * A description for the Amazon Web Services Verified Access trust provider.
     */
    readonly description?: string;
    /**
     * The last updated time.
     */
    readonly lastUpdatedTime?: string;
    readonly oidcOptions?: outputs.ec2.VerifiedAccessTrustProviderOidcOptions;
    /**
     * The configuration options for customer provided KMS encryption.
     */
    readonly sseSpecification?: outputs.ec2.SseSpecificationProperties;
    /**
     * An array of key-value pairs to apply to this resource.
     */
    readonly tags?: outputs.ec2.VerifiedAccessTrustProviderTag[];
    /**
     * The ID of the Amazon Web Services Verified Access trust provider.
     */
    readonly verifiedAccessTrustProviderId?: string;
}
/**
 * The AWS::EC2::VerifiedAccessTrustProvider type describes a verified access trust provider
 */
export function getVerifiedAccessTrustProviderOutput(args: GetVerifiedAccessTrustProviderOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetVerifiedAccessTrustProviderResult> {
    return pulumi.output(args).apply((a: any) => getVerifiedAccessTrustProvider(a, opts))
}

export interface GetVerifiedAccessTrustProviderOutputArgs {
    /**
     * The ID of the Amazon Web Services Verified Access trust provider.
     */
    verifiedAccessTrustProviderId: pulumi.Input<string>;
}
