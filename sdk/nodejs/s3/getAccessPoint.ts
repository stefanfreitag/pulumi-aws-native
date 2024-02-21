// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * The AWS::S3::AccessPoint resource is an Amazon S3 resource type that you can use to access buckets.
 */
export function getAccessPoint(args: GetAccessPointArgs, opts?: pulumi.InvokeOptions): Promise<GetAccessPointResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("aws-native:s3:getAccessPoint", {
        "name": args.name,
    }, opts);
}

export interface GetAccessPointArgs {
    /**
     * The name you want to assign to this Access Point. If you don't specify a name, AWS CloudFormation generates a unique ID and uses that ID for the access point name.
     */
    name: string;
}

export interface GetAccessPointResult {
    /**
     * The alias of this Access Point. This alias can be used for compatibility purposes with other AWS services and third-party applications.
     */
    readonly alias?: string;
    /**
     * The Amazon Resource Name (ARN) of the specified accesspoint.
     */
    readonly arn?: string;
    /**
     * Indicates whether this Access Point allows access from the public Internet. If VpcConfiguration is specified for this Access Point, then NetworkOrigin is VPC, and the Access Point doesn't allow access from the public Internet. Otherwise, NetworkOrigin is Internet, and the Access Point allows access from the public Internet, subject to the Access Point and bucket access policies.
     */
    readonly networkOrigin?: enums.s3.AccessPointNetworkOrigin;
    /**
     * The Access Point Policy you want to apply to this access point.
     *
     * Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::S3::AccessPoint` for more information about the expected schema for this property.
     */
    readonly policy?: any;
    /**
     * The PublicAccessBlock configuration that you want to apply to this Access Point. You can enable the configuration options in any combination. For more information about when Amazon S3 considers a bucket or object public, see https://docs.aws.amazon.com/AmazonS3/latest/dev/access-control-block-public-access.html#access-control-block-public-access-policy-status 'The Meaning of Public' in the Amazon Simple Storage Service Developer Guide.
     */
    readonly publicAccessBlockConfiguration?: outputs.s3.AccessPointPublicAccessBlockConfiguration;
}
/**
 * The AWS::S3::AccessPoint resource is an Amazon S3 resource type that you can use to access buckets.
 */
export function getAccessPointOutput(args: GetAccessPointOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetAccessPointResult> {
    return pulumi.output(args).apply((a: any) => getAccessPoint(a, opts))
}

export interface GetAccessPointOutputArgs {
    /**
     * The name you want to assign to this Access Point. If you don't specify a name, AWS CloudFormation generates a unique ID and uses that ID for the access point name.
     */
    name: pulumi.Input<string>;
}
