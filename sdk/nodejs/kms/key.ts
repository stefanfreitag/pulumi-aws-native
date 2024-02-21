// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * The AWS::KMS::Key resource specifies an AWS KMS key in AWS Key Management Service (AWS KMS). Authorized users can use the AWS KMS key to encrypt and decrypt small amounts of data (up to 4096 bytes), but they are more commonly used to generate data keys. You can also use AWS KMS keys to encrypt data stored in AWS services that are integrated with AWS KMS or within their applications.
 */
export class Key extends pulumi.CustomResource {
    /**
     * Get an existing Key resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): Key {
        return new Key(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:kms:Key';

    /**
     * Returns true if the given object is an instance of Key.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Key {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Key.__pulumiType;
    }

    public /*out*/ readonly arn!: pulumi.Output<string>;
    /**
     * Skips ("bypasses") the key policy lockout safety check. The default value is false.
     */
    public readonly bypassPolicyLockoutSafetyCheck!: pulumi.Output<boolean | undefined>;
    /**
     * A description of the AWS KMS key. Use a description that helps you to distinguish this AWS KMS key from others in the account, such as its intended use.
     */
    public readonly description!: pulumi.Output<string | undefined>;
    /**
     * Enables automatic rotation of the key material for the specified AWS KMS key. By default, automation key rotation is not enabled.
     */
    public readonly enableKeyRotation!: pulumi.Output<boolean | undefined>;
    /**
     * Specifies whether the AWS KMS key is enabled. Disabled AWS KMS keys cannot be used in cryptographic operations.
     */
    public readonly enabled!: pulumi.Output<boolean | undefined>;
    public /*out*/ readonly keyId!: pulumi.Output<string>;
    /**
     * The key policy that authorizes use of the AWS KMS key. The key policy must observe the following rules.
     *
     * Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::KMS::Key` for more information about the expected schema for this property.
     */
    public readonly keyPolicy!: pulumi.Output<any | undefined>;
    /**
     * Specifies the type of AWS KMS key to create. The default value is SYMMETRIC_DEFAULT. This property is required only for asymmetric AWS KMS keys. You can't change the KeySpec value after the AWS KMS key is created.
     */
    public readonly keySpec!: pulumi.Output<enums.kms.KeySpec | undefined>;
    /**
     * Determines the cryptographic operations for which you can use the AWS KMS key. The default value is ENCRYPT_DECRYPT. This property is required only for asymmetric AWS KMS keys. You can't change the KeyUsage value after the AWS KMS key is created.
     */
    public readonly keyUsage!: pulumi.Output<enums.kms.KeyUsage | undefined>;
    /**
     * Specifies whether the AWS KMS key should be Multi-Region. You can't change the MultiRegion value after the AWS KMS key is created.
     */
    public readonly multiRegion!: pulumi.Output<boolean | undefined>;
    /**
     * The source of the key material for the KMS key. You cannot change the origin after you create the KMS key. The default is AWS_KMS, which means that AWS KMS creates the key material.
     */
    public readonly origin!: pulumi.Output<enums.kms.KeyOrigin | undefined>;
    /**
     * Specifies the number of days in the waiting period before AWS KMS deletes an AWS KMS key that has been removed from a CloudFormation stack. Enter a value between 7 and 30 days. The default value is 30 days.
     */
    public readonly pendingWindowInDays!: pulumi.Output<number | undefined>;
    /**
     * An array of key-value pairs to apply to this resource.
     */
    public readonly tags!: pulumi.Output<outputs.kms.KeyTag[] | undefined>;

    /**
     * Create a Key resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args?: KeyArgs, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            resourceInputs["bypassPolicyLockoutSafetyCheck"] = args ? args.bypassPolicyLockoutSafetyCheck : undefined;
            resourceInputs["description"] = args ? args.description : undefined;
            resourceInputs["enableKeyRotation"] = args ? args.enableKeyRotation : undefined;
            resourceInputs["enabled"] = args ? args.enabled : undefined;
            resourceInputs["keyPolicy"] = args ? args.keyPolicy : undefined;
            resourceInputs["keySpec"] = args ? args.keySpec : undefined;
            resourceInputs["keyUsage"] = args ? args.keyUsage : undefined;
            resourceInputs["multiRegion"] = args ? args.multiRegion : undefined;
            resourceInputs["origin"] = args ? args.origin : undefined;
            resourceInputs["pendingWindowInDays"] = args ? args.pendingWindowInDays : undefined;
            resourceInputs["tags"] = args ? args.tags : undefined;
            resourceInputs["arn"] = undefined /*out*/;
            resourceInputs["keyId"] = undefined /*out*/;
        } else {
            resourceInputs["arn"] = undefined /*out*/;
            resourceInputs["bypassPolicyLockoutSafetyCheck"] = undefined /*out*/;
            resourceInputs["description"] = undefined /*out*/;
            resourceInputs["enableKeyRotation"] = undefined /*out*/;
            resourceInputs["enabled"] = undefined /*out*/;
            resourceInputs["keyId"] = undefined /*out*/;
            resourceInputs["keyPolicy"] = undefined /*out*/;
            resourceInputs["keySpec"] = undefined /*out*/;
            resourceInputs["keyUsage"] = undefined /*out*/;
            resourceInputs["multiRegion"] = undefined /*out*/;
            resourceInputs["origin"] = undefined /*out*/;
            resourceInputs["pendingWindowInDays"] = undefined /*out*/;
            resourceInputs["tags"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(Key.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a Key resource.
 */
export interface KeyArgs {
    /**
     * Skips ("bypasses") the key policy lockout safety check. The default value is false.
     */
    bypassPolicyLockoutSafetyCheck?: pulumi.Input<boolean>;
    /**
     * A description of the AWS KMS key. Use a description that helps you to distinguish this AWS KMS key from others in the account, such as its intended use.
     */
    description?: pulumi.Input<string>;
    /**
     * Enables automatic rotation of the key material for the specified AWS KMS key. By default, automation key rotation is not enabled.
     */
    enableKeyRotation?: pulumi.Input<boolean>;
    /**
     * Specifies whether the AWS KMS key is enabled. Disabled AWS KMS keys cannot be used in cryptographic operations.
     */
    enabled?: pulumi.Input<boolean>;
    /**
     * The key policy that authorizes use of the AWS KMS key. The key policy must observe the following rules.
     *
     * Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::KMS::Key` for more information about the expected schema for this property.
     */
    keyPolicy?: any;
    /**
     * Specifies the type of AWS KMS key to create. The default value is SYMMETRIC_DEFAULT. This property is required only for asymmetric AWS KMS keys. You can't change the KeySpec value after the AWS KMS key is created.
     */
    keySpec?: pulumi.Input<enums.kms.KeySpec>;
    /**
     * Determines the cryptographic operations for which you can use the AWS KMS key. The default value is ENCRYPT_DECRYPT. This property is required only for asymmetric AWS KMS keys. You can't change the KeyUsage value after the AWS KMS key is created.
     */
    keyUsage?: pulumi.Input<enums.kms.KeyUsage>;
    /**
     * Specifies whether the AWS KMS key should be Multi-Region. You can't change the MultiRegion value after the AWS KMS key is created.
     */
    multiRegion?: pulumi.Input<boolean>;
    /**
     * The source of the key material for the KMS key. You cannot change the origin after you create the KMS key. The default is AWS_KMS, which means that AWS KMS creates the key material.
     */
    origin?: pulumi.Input<enums.kms.KeyOrigin>;
    /**
     * Specifies the number of days in the waiting period before AWS KMS deletes an AWS KMS key that has been removed from a CloudFormation stack. Enter a value between 7 and 30 days. The default value is 30 days.
     */
    pendingWindowInDays?: pulumi.Input<number>;
    /**
     * An array of key-value pairs to apply to this resource.
     */
    tags?: pulumi.Input<pulumi.Input<inputs.kms.KeyTagArgs>[]>;
}
