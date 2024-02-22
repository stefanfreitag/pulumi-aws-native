// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * An example resource schema demonstrating some basic constructs and validation rules.
 */
export function getDomain(args: GetDomainArgs, opts?: pulumi.InvokeOptions): Promise<GetDomainResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("aws-native:opensearchservice:getDomain", {
        "domainName": args.domainName,
    }, opts);
}

export interface GetDomainArgs {
    domainName: string;
}

export interface GetDomainResult {
    /**
     * Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::OpenSearchService::Domain` for more information about the expected schema for this property.
     */
    readonly accessPolicies?: any;
    readonly advancedOptions?: {[key: string]: string};
    readonly advancedSecurityOptions?: outputs.opensearchservice.DomainAdvancedSecurityOptionsInput;
    readonly arn?: string;
    readonly clusterConfig?: outputs.opensearchservice.DomainClusterConfig;
    readonly cognitoOptions?: outputs.opensearchservice.DomainCognitoOptions;
    readonly domainArn?: string;
    readonly domainEndpoint?: string;
    readonly domainEndpointOptions?: outputs.opensearchservice.DomainEndpointOptions;
    readonly domainEndpointV2?: string;
    readonly domainEndpoints?: {[key: string]: string};
    readonly ebsOptions?: outputs.opensearchservice.DomainEbsOptions;
    readonly encryptionAtRestOptions?: outputs.opensearchservice.DomainEncryptionAtRestOptions;
    readonly engineVersion?: string;
    readonly id?: string;
    readonly ipAddressType?: string;
    readonly logPublishingOptions?: {[key: string]: outputs.opensearchservice.DomainLogPublishingOption};
    readonly nodeToNodeEncryptionOptions?: outputs.opensearchservice.DomainNodeToNodeEncryptionOptions;
    readonly offPeakWindowOptions?: outputs.opensearchservice.DomainOffPeakWindowOptions;
    readonly serviceSoftwareOptions?: outputs.opensearchservice.DomainServiceSoftwareOptions;
    readonly snapshotOptions?: outputs.opensearchservice.DomainSnapshotOptions;
    readonly softwareUpdateOptions?: outputs.opensearchservice.DomainSoftwareUpdateOptions;
    /**
     * An arbitrary set of tags (key-value pairs) for this Domain.
     */
    readonly tags?: outputs.Tag[];
    readonly vpcOptions?: outputs.opensearchservice.DomainVpcOptions;
}
/**
 * An example resource schema demonstrating some basic constructs and validation rules.
 */
export function getDomainOutput(args: GetDomainOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetDomainResult> {
    return pulumi.output(args).apply((a: any) => getDomain(a, opts))
}

export interface GetDomainOutputArgs {
    domainName: pulumi.Input<string>;
}
