// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * The resource schema to create a CodeArtifact domain.
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
        return new Domain(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:codeartifact:Domain';

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
     * The ARN of the domain.
     */
    public /*out*/ readonly arn!: pulumi.Output<string>;
    /**
     * The name of the domain.
     */
    public readonly domainName!: pulumi.Output<string>;
    /**
     * The ARN of an AWS Key Management Service (AWS KMS) key associated with a domain.
     */
    public readonly encryptionKey!: pulumi.Output<string>;
    /**
     * The name of the domain. This field is used for GetAtt
     */
    public /*out*/ readonly name!: pulumi.Output<string>;
    /**
     * The 12-digit account ID of the AWS account that owns the domain. This field is used for GetAtt
     */
    public /*out*/ readonly owner!: pulumi.Output<string>;
    /**
     * The access control resource policy on the provided domain.
     *
     * Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::CodeArtifact::Domain` for more information about the expected schema for this property.
     */
    public readonly permissionsPolicyDocument!: pulumi.Output<any | undefined>;
    /**
     * An array of key-value pairs to apply to this resource.
     */
    public readonly tags!: pulumi.Output<outputs.Tag[] | undefined>;

    /**
     * Create a Domain resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args?: DomainArgs, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            resourceInputs["domainName"] = args ? args.domainName : undefined;
            resourceInputs["encryptionKey"] = args ? args.encryptionKey : undefined;
            resourceInputs["permissionsPolicyDocument"] = args ? args.permissionsPolicyDocument : undefined;
            resourceInputs["tags"] = args ? args.tags : undefined;
            resourceInputs["arn"] = undefined /*out*/;
            resourceInputs["name"] = undefined /*out*/;
            resourceInputs["owner"] = undefined /*out*/;
        } else {
            resourceInputs["arn"] = undefined /*out*/;
            resourceInputs["domainName"] = undefined /*out*/;
            resourceInputs["encryptionKey"] = undefined /*out*/;
            resourceInputs["name"] = undefined /*out*/;
            resourceInputs["owner"] = undefined /*out*/;
            resourceInputs["permissionsPolicyDocument"] = undefined /*out*/;
            resourceInputs["tags"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        const replaceOnChanges = { replaceOnChanges: ["domainName", "encryptionKey"] };
        opts = pulumi.mergeOptions(opts, replaceOnChanges);
        super(Domain.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a Domain resource.
 */
export interface DomainArgs {
    /**
     * The name of the domain.
     */
    domainName?: pulumi.Input<string>;
    /**
     * The ARN of an AWS Key Management Service (AWS KMS) key associated with a domain.
     */
    encryptionKey?: pulumi.Input<string>;
    /**
     * The access control resource policy on the provided domain.
     *
     * Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::CodeArtifact::Domain` for more information about the expected schema for this property.
     */
    permissionsPolicyDocument?: any;
    /**
     * An array of key-value pairs to apply to this resource.
     */
    tags?: pulumi.Input<pulumi.Input<inputs.TagArgs>[]>;
}
