// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::SecretsManager::Secret
 */
export class Secret extends pulumi.CustomResource {
    /**
     * Get an existing Secret resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): Secret {
        return new Secret(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:secretsmanager:Secret';

    /**
     * Returns true if the given object is an instance of Secret.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Secret {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Secret.__pulumiType;
    }

    /**
     * (Optional) Specifies a user-provided description of the secret.
     */
    public readonly description!: pulumi.Output<string | undefined>;
    /**
     * (Optional) Specifies text data that you want to encrypt and store in this new version of the secret.
     */
    public readonly generateSecretString!: pulumi.Output<outputs.secretsmanager.SecretGenerateSecretString | undefined>;
    /**
     * (Optional) Specifies the ARN, Key ID, or alias of the AWS KMS customer master key (CMK) used to encrypt the SecretString.
     */
    public readonly kmsKeyId!: pulumi.Output<string | undefined>;
    /**
     * The friendly name of the secret. You can use forward slashes in the name to represent a path hierarchy.
     */
    public readonly name!: pulumi.Output<string | undefined>;
    /**
     * (Optional) A list of ReplicaRegion objects. The ReplicaRegion type consists of a Region (required) and the KmsKeyId which can be an ARN, Key ID, or Alias.
     */
    public readonly replicaRegions!: pulumi.Output<outputs.secretsmanager.SecretReplicaRegion[] | undefined>;
    /**
     * (Optional) Specifies text data that you want to encrypt and store in this new version of the secret.
     */
    public readonly secretString!: pulumi.Output<string | undefined>;
    /**
     * The list of user-defined tags associated with the secret. Use tags to manage your AWS resources. For additional information about tags, see TagResource.
     */
    public readonly tags!: pulumi.Output<outputs.Tag[] | undefined>;

    /**
     * Create a Secret resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args?: SecretArgs, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            resourceInputs["description"] = args ? args.description : undefined;
            resourceInputs["generateSecretString"] = args ? args.generateSecretString : undefined;
            resourceInputs["kmsKeyId"] = args ? args.kmsKeyId : undefined;
            resourceInputs["name"] = args ? args.name : undefined;
            resourceInputs["replicaRegions"] = args ? args.replicaRegions : undefined;
            resourceInputs["secretString"] = args ? args.secretString : undefined;
            resourceInputs["tags"] = args ? args.tags : undefined;
        } else {
            resourceInputs["description"] = undefined /*out*/;
            resourceInputs["generateSecretString"] = undefined /*out*/;
            resourceInputs["kmsKeyId"] = undefined /*out*/;
            resourceInputs["name"] = undefined /*out*/;
            resourceInputs["replicaRegions"] = undefined /*out*/;
            resourceInputs["secretString"] = undefined /*out*/;
            resourceInputs["tags"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        const replaceOnChanges = { replaceOnChanges: ["name"] };
        opts = pulumi.mergeOptions(opts, replaceOnChanges);
        super(Secret.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a Secret resource.
 */
export interface SecretArgs {
    /**
     * (Optional) Specifies a user-provided description of the secret.
     */
    description?: pulumi.Input<string>;
    /**
     * (Optional) Specifies text data that you want to encrypt and store in this new version of the secret.
     */
    generateSecretString?: pulumi.Input<inputs.secretsmanager.SecretGenerateSecretStringArgs>;
    /**
     * (Optional) Specifies the ARN, Key ID, or alias of the AWS KMS customer master key (CMK) used to encrypt the SecretString.
     */
    kmsKeyId?: pulumi.Input<string>;
    /**
     * The friendly name of the secret. You can use forward slashes in the name to represent a path hierarchy.
     */
    name?: pulumi.Input<string>;
    /**
     * (Optional) A list of ReplicaRegion objects. The ReplicaRegion type consists of a Region (required) and the KmsKeyId which can be an ARN, Key ID, or Alias.
     */
    replicaRegions?: pulumi.Input<pulumi.Input<inputs.secretsmanager.SecretReplicaRegionArgs>[]>;
    /**
     * (Optional) Specifies text data that you want to encrypt and store in this new version of the secret.
     */
    secretString?: pulumi.Input<string>;
    /**
     * The list of user-defined tags associated with the secret. Use tags to manage your AWS resources. For additional information about tags, see TagResource.
     */
    tags?: pulumi.Input<pulumi.Input<inputs.TagArgs>[]>;
}
