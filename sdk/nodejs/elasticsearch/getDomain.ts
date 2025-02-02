// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::Elasticsearch::Domain
 */
export function getDomain(args: GetDomainArgs, opts?: pulumi.InvokeOptions): Promise<GetDomainResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("aws-native:elasticsearch:getDomain", {
        "id": args.id,
    }, opts);
}

export interface GetDomainArgs {
    id: string;
}

export interface GetDomainResult {
    /**
     * Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::Elasticsearch::Domain` for more information about the expected schema for this property.
     */
    readonly accessPolicies?: any;
    readonly advancedOptions?: {[key: string]: string};
    readonly advancedSecurityOptions?: outputs.elasticsearch.DomainAdvancedSecurityOptionsInput;
    readonly arn?: string;
    readonly cognitoOptions?: outputs.elasticsearch.DomainCognitoOptions;
    readonly domainArn?: string;
    readonly domainEndpoint?: string;
    readonly domainEndpointOptions?: outputs.elasticsearch.DomainEndpointOptions;
    readonly ebsOptions?: outputs.elasticsearch.DomainEbsOptions;
    readonly elasticsearchClusterConfig?: outputs.elasticsearch.DomainElasticsearchClusterConfig;
    readonly elasticsearchVersion?: string;
    readonly encryptionAtRestOptions?: outputs.elasticsearch.DomainEncryptionAtRestOptions;
    readonly id?: string;
    readonly logPublishingOptions?: {[key: string]: outputs.elasticsearch.DomainLogPublishingOption};
    readonly nodeToNodeEncryptionOptions?: outputs.elasticsearch.DomainNodeToNodeEncryptionOptions;
    readonly snapshotOptions?: outputs.elasticsearch.DomainSnapshotOptions;
    readonly tags?: outputs.Tag[];
    readonly vpcOptions?: outputs.elasticsearch.DomainVpcOptions;
}
/**
 * Resource Type definition for AWS::Elasticsearch::Domain
 */
export function getDomainOutput(args: GetDomainOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetDomainResult> {
    return pulumi.output(args).apply((a: any) => getDomain(a, opts))
}

export interface GetDomainOutputArgs {
    id: pulumi.Input<string>;
}
