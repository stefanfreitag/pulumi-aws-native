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
    readonly accessPolicies?: any;
    readonly advancedOptions?: any;
    readonly advancedSecurityOptions?: outputs.elasticsearch.DomainAdvancedSecurityOptionsInput;
    readonly arn?: string;
    readonly cognitoOptions?: outputs.elasticsearch.DomainCognitoOptions;
    readonly domainArn?: string;
    readonly domainEndpoint?: string;
    readonly domainEndpointOptions?: outputs.elasticsearch.DomainEndpointOptions;
    readonly eBSOptions?: outputs.elasticsearch.DomainEBSOptions;
    readonly elasticsearchClusterConfig?: outputs.elasticsearch.DomainElasticsearchClusterConfig;
    readonly elasticsearchVersion?: string;
    readonly encryptionAtRestOptions?: outputs.elasticsearch.DomainEncryptionAtRestOptions;
    readonly id?: string;
    readonly logPublishingOptions?: any;
    readonly nodeToNodeEncryptionOptions?: outputs.elasticsearch.DomainNodeToNodeEncryptionOptions;
    readonly snapshotOptions?: outputs.elasticsearch.DomainSnapshotOptions;
    readonly tags?: outputs.elasticsearch.DomainTag[];
    readonly vPCOptions?: outputs.elasticsearch.DomainVPCOptions;
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
