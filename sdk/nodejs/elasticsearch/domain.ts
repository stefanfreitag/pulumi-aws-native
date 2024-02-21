// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::Elasticsearch::Domain
 *
 * @deprecated Domain is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.
 */
export class Domain extends pulumi.CustomResource {
    /**
     * Get an existing Domain resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): Domain {
        pulumi.log.warn("Domain is deprecated: Domain is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.")
        return new Domain(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:elasticsearch:Domain';

    /**
     * Returns true if the given object is an instance of Domain.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Domain {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Domain.__pulumiType;
    }

    /**
     * Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::Elasticsearch::Domain` for more information about the expected schema for this property.
     */
    public readonly accessPolicies!: pulumi.Output<any | undefined>;
    /**
     * Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::Elasticsearch::Domain` for more information about the expected schema for this property.
     */
    public readonly advancedOptions!: pulumi.Output<any | undefined>;
    public readonly advancedSecurityOptions!: pulumi.Output<outputs.elasticsearch.DomainAdvancedSecurityOptionsInput | undefined>;
    public /*out*/ readonly arn!: pulumi.Output<string>;
    public readonly cognitoOptions!: pulumi.Output<outputs.elasticsearch.DomainCognitoOptions | undefined>;
    public /*out*/ readonly domainArn!: pulumi.Output<string>;
    public /*out*/ readonly domainEndpoint!: pulumi.Output<string>;
    public readonly domainEndpointOptions!: pulumi.Output<outputs.elasticsearch.DomainEndpointOptions | undefined>;
    public readonly domainName!: pulumi.Output<string | undefined>;
    public readonly ebsOptions!: pulumi.Output<outputs.elasticsearch.DomainEbsOptions | undefined>;
    public readonly elasticsearchClusterConfig!: pulumi.Output<outputs.elasticsearch.DomainElasticsearchClusterConfig | undefined>;
    public readonly elasticsearchVersion!: pulumi.Output<string | undefined>;
    public readonly encryptionAtRestOptions!: pulumi.Output<outputs.elasticsearch.DomainEncryptionAtRestOptions | undefined>;
    /**
     * Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::Elasticsearch::Domain` for more information about the expected schema for this property.
     */
    public readonly logPublishingOptions!: pulumi.Output<any | undefined>;
    public readonly nodeToNodeEncryptionOptions!: pulumi.Output<outputs.elasticsearch.DomainNodeToNodeEncryptionOptions | undefined>;
    public readonly snapshotOptions!: pulumi.Output<outputs.elasticsearch.DomainSnapshotOptions | undefined>;
    public readonly tags!: pulumi.Output<outputs.elasticsearch.DomainTag[] | undefined>;
    public readonly vpcOptions!: pulumi.Output<outputs.elasticsearch.DomainVpcOptions | undefined>;

    /**
     * Create a Domain resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    /** @deprecated Domain is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible. */
    constructor(name: string, args?: DomainArgs, opts?: pulumi.CustomResourceOptions) {
        pulumi.log.warn("Domain is deprecated: Domain is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.")
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            resourceInputs["accessPolicies"] = args ? args.accessPolicies : undefined;
            resourceInputs["advancedOptions"] = args ? args.advancedOptions : undefined;
            resourceInputs["advancedSecurityOptions"] = args ? args.advancedSecurityOptions : undefined;
            resourceInputs["cognitoOptions"] = args ? args.cognitoOptions : undefined;
            resourceInputs["domainEndpointOptions"] = args ? args.domainEndpointOptions : undefined;
            resourceInputs["domainName"] = args ? args.domainName : undefined;
            resourceInputs["ebsOptions"] = args ? args.ebsOptions : undefined;
            resourceInputs["elasticsearchClusterConfig"] = args ? args.elasticsearchClusterConfig : undefined;
            resourceInputs["elasticsearchVersion"] = args ? args.elasticsearchVersion : undefined;
            resourceInputs["encryptionAtRestOptions"] = args ? args.encryptionAtRestOptions : undefined;
            resourceInputs["logPublishingOptions"] = args ? args.logPublishingOptions : undefined;
            resourceInputs["nodeToNodeEncryptionOptions"] = args ? args.nodeToNodeEncryptionOptions : undefined;
            resourceInputs["snapshotOptions"] = args ? args.snapshotOptions : undefined;
            resourceInputs["tags"] = args ? args.tags : undefined;
            resourceInputs["vpcOptions"] = args ? args.vpcOptions : undefined;
            resourceInputs["arn"] = undefined /*out*/;
            resourceInputs["domainArn"] = undefined /*out*/;
            resourceInputs["domainEndpoint"] = undefined /*out*/;
        } else {
            resourceInputs["accessPolicies"] = undefined /*out*/;
            resourceInputs["advancedOptions"] = undefined /*out*/;
            resourceInputs["advancedSecurityOptions"] = undefined /*out*/;
            resourceInputs["arn"] = undefined /*out*/;
            resourceInputs["cognitoOptions"] = undefined /*out*/;
            resourceInputs["domainArn"] = undefined /*out*/;
            resourceInputs["domainEndpoint"] = undefined /*out*/;
            resourceInputs["domainEndpointOptions"] = undefined /*out*/;
            resourceInputs["domainName"] = undefined /*out*/;
            resourceInputs["ebsOptions"] = undefined /*out*/;
            resourceInputs["elasticsearchClusterConfig"] = undefined /*out*/;
            resourceInputs["elasticsearchVersion"] = undefined /*out*/;
            resourceInputs["encryptionAtRestOptions"] = undefined /*out*/;
            resourceInputs["logPublishingOptions"] = undefined /*out*/;
            resourceInputs["nodeToNodeEncryptionOptions"] = undefined /*out*/;
            resourceInputs["snapshotOptions"] = undefined /*out*/;
            resourceInputs["tags"] = undefined /*out*/;
            resourceInputs["vpcOptions"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        const replaceOnChanges = { replaceOnChanges: ["domainName"] };
        opts = pulumi.mergeOptions(opts, replaceOnChanges);
        super(Domain.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a Domain resource.
 */
export interface DomainArgs {
    /**
     * Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::Elasticsearch::Domain` for more information about the expected schema for this property.
     */
    accessPolicies?: any;
    /**
     * Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::Elasticsearch::Domain` for more information about the expected schema for this property.
     */
    advancedOptions?: any;
    advancedSecurityOptions?: pulumi.Input<inputs.elasticsearch.DomainAdvancedSecurityOptionsInputArgs>;
    cognitoOptions?: pulumi.Input<inputs.elasticsearch.DomainCognitoOptionsArgs>;
    domainEndpointOptions?: pulumi.Input<inputs.elasticsearch.DomainEndpointOptionsArgs>;
    domainName?: pulumi.Input<string>;
    ebsOptions?: pulumi.Input<inputs.elasticsearch.DomainEbsOptionsArgs>;
    elasticsearchClusterConfig?: pulumi.Input<inputs.elasticsearch.DomainElasticsearchClusterConfigArgs>;
    elasticsearchVersion?: pulumi.Input<string>;
    encryptionAtRestOptions?: pulumi.Input<inputs.elasticsearch.DomainEncryptionAtRestOptionsArgs>;
    /**
     * Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::Elasticsearch::Domain` for more information about the expected schema for this property.
     */
    logPublishingOptions?: any;
    nodeToNodeEncryptionOptions?: pulumi.Input<inputs.elasticsearch.DomainNodeToNodeEncryptionOptionsArgs>;
    snapshotOptions?: pulumi.Input<inputs.elasticsearch.DomainSnapshotOptionsArgs>;
    tags?: pulumi.Input<pulumi.Input<inputs.elasticsearch.DomainTagArgs>[]>;
    vpcOptions?: pulumi.Input<inputs.elasticsearch.DomainVpcOptionsArgs>;
}
