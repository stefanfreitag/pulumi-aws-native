// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * The AWS::KMS::Alias resource specifies a display name for an AWS KMS key in AWS Key Management Service (AWS KMS). You can use an alias to identify an AWS KMS key in cryptographic operations.
 */
export class Alias extends pulumi.CustomResource {
    /**
     * Get an existing Alias resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): Alias {
        return new Alias(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:kms:Alias';

    /**
     * Returns true if the given object is an instance of Alias.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Alias {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Alias.__pulumiType;
    }

    /**
     * Specifies the alias name. This value must begin with alias/ followed by a name, such as alias/ExampleAlias. The alias name cannot begin with alias/aws/. The alias/aws/ prefix is reserved for AWS managed keys.
     */
    public readonly aliasName!: pulumi.Output<string>;
    /**
     * Identifies the AWS KMS key to which the alias refers. Specify the key ID or the Amazon Resource Name (ARN) of the AWS KMS key. You cannot specify another alias. For help finding the key ID and ARN, see Finding the Key ID and ARN in the AWS Key Management Service Developer Guide.
     */
    public readonly targetKeyId!: pulumi.Output<string>;

    /**
     * Create a Alias resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: AliasArgs, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.targetKeyId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'targetKeyId'");
            }
            resourceInputs["aliasName"] = args ? args.aliasName : undefined;
            resourceInputs["targetKeyId"] = args ? args.targetKeyId : undefined;
        } else {
            resourceInputs["aliasName"] = undefined /*out*/;
            resourceInputs["targetKeyId"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(Alias.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a Alias resource.
 */
export interface AliasArgs {
    /**
     * Specifies the alias name. This value must begin with alias/ followed by a name, such as alias/ExampleAlias. The alias name cannot begin with alias/aws/. The alias/aws/ prefix is reserved for AWS managed keys.
     */
    aliasName?: pulumi.Input<string>;
    /**
     * Identifies the AWS KMS key to which the alias refers. Specify the key ID or the Amazon Resource Name (ARN) of the AWS KMS key. You cannot specify another alias. For help finding the key ID and ARN, see Finding the Key ID and ARN in the AWS Key Management Service Developer Guide.
     */
    targetKeyId: pulumi.Input<string>;
}
