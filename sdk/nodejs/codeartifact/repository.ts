// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * The resource schema to create a CodeArtifact repository.
 */
export class Repository extends pulumi.CustomResource {
    /**
     * Get an existing Repository resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): Repository {
        return new Repository(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:codeartifact:Repository';

    /**
     * Returns true if the given object is an instance of Repository.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Repository {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Repository.__pulumiType;
    }

    /**
     * The ARN of the repository.
     */
    public /*out*/ readonly arn!: pulumi.Output<string>;
    /**
     * A text description of the repository.
     */
    public readonly description!: pulumi.Output<string | undefined>;
    /**
     * The name of the domain that contains the repository.
     */
    public readonly domainName!: pulumi.Output<string>;
    /**
     * The 12-digit account ID of the AWS account that owns the domain.
     */
    public readonly domainOwner!: pulumi.Output<string>;
    /**
     * A list of external connections associated with the repository.
     */
    public readonly externalConnections!: pulumi.Output<string[] | undefined>;
    /**
     * The name of the repository. This is used for GetAtt
     */
    public /*out*/ readonly name!: pulumi.Output<string>;
    /**
     * The access control resource policy on the provided repository.
     *
     * Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::CodeArtifact::Repository` for more information about the expected schema for this property.
     */
    public readonly permissionsPolicyDocument!: pulumi.Output<any | undefined>;
    /**
     * The name of the repository.
     */
    public readonly repositoryName!: pulumi.Output<string>;
    /**
     * An array of key-value pairs to apply to this resource.
     */
    public readonly tags!: pulumi.Output<outputs.codeartifact.RepositoryTag[] | undefined>;
    /**
     * A list of upstream repositories associated with the repository.
     */
    public readonly upstreams!: pulumi.Output<string[] | undefined>;

    /**
     * Create a Repository resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: RepositoryArgs, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.domainName === undefined) && !opts.urn) {
                throw new Error("Missing required property 'domainName'");
            }
            resourceInputs["description"] = args ? args.description : undefined;
            resourceInputs["domainName"] = args ? args.domainName : undefined;
            resourceInputs["domainOwner"] = args ? args.domainOwner : undefined;
            resourceInputs["externalConnections"] = args ? args.externalConnections : undefined;
            resourceInputs["permissionsPolicyDocument"] = args ? args.permissionsPolicyDocument : undefined;
            resourceInputs["repositoryName"] = args ? args.repositoryName : undefined;
            resourceInputs["tags"] = args ? args.tags : undefined;
            resourceInputs["upstreams"] = args ? args.upstreams : undefined;
            resourceInputs["arn"] = undefined /*out*/;
            resourceInputs["name"] = undefined /*out*/;
        } else {
            resourceInputs["arn"] = undefined /*out*/;
            resourceInputs["description"] = undefined /*out*/;
            resourceInputs["domainName"] = undefined /*out*/;
            resourceInputs["domainOwner"] = undefined /*out*/;
            resourceInputs["externalConnections"] = undefined /*out*/;
            resourceInputs["name"] = undefined /*out*/;
            resourceInputs["permissionsPolicyDocument"] = undefined /*out*/;
            resourceInputs["repositoryName"] = undefined /*out*/;
            resourceInputs["tags"] = undefined /*out*/;
            resourceInputs["upstreams"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        const replaceOnChanges = { replaceOnChanges: ["domainName", "domainOwner", "repositoryName"] };
        opts = pulumi.mergeOptions(opts, replaceOnChanges);
        super(Repository.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a Repository resource.
 */
export interface RepositoryArgs {
    /**
     * A text description of the repository.
     */
    description?: pulumi.Input<string>;
    /**
     * The name of the domain that contains the repository.
     */
    domainName: pulumi.Input<string>;
    /**
     * The 12-digit account ID of the AWS account that owns the domain.
     */
    domainOwner?: pulumi.Input<string>;
    /**
     * A list of external connections associated with the repository.
     */
    externalConnections?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * The access control resource policy on the provided repository.
     *
     * Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::CodeArtifact::Repository` for more information about the expected schema for this property.
     */
    permissionsPolicyDocument?: any;
    /**
     * The name of the repository.
     */
    repositoryName?: pulumi.Input<string>;
    /**
     * An array of key-value pairs to apply to this resource.
     */
    tags?: pulumi.Input<pulumi.Input<inputs.codeartifact.RepositoryTagArgs>[]>;
    /**
     * A list of upstream repositories associated with the repository.
     */
    upstreams?: pulumi.Input<pulumi.Input<string>[]>;
}
