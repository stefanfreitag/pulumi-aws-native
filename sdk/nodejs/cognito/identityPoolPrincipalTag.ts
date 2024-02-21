// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::Cognito::IdentityPoolPrincipalTag
 */
export class IdentityPoolPrincipalTag extends pulumi.CustomResource {
    /**
     * Get an existing IdentityPoolPrincipalTag resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): IdentityPoolPrincipalTag {
        return new IdentityPoolPrincipalTag(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:cognito:IdentityPoolPrincipalTag';

    /**
     * Returns true if the given object is an instance of IdentityPoolPrincipalTag.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is IdentityPoolPrincipalTag {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === IdentityPoolPrincipalTag.__pulumiType;
    }

    public readonly identityPoolId!: pulumi.Output<string>;
    public readonly identityProviderName!: pulumi.Output<string>;
    /**
     * Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::Cognito::IdentityPoolPrincipalTag` for more information about the expected schema for this property.
     */
    public readonly principalTags!: pulumi.Output<any | undefined>;
    public readonly useDefaults!: pulumi.Output<boolean | undefined>;

    /**
     * Create a IdentityPoolPrincipalTag resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: IdentityPoolPrincipalTagArgs, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.identityPoolId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'identityPoolId'");
            }
            if ((!args || args.identityProviderName === undefined) && !opts.urn) {
                throw new Error("Missing required property 'identityProviderName'");
            }
            resourceInputs["identityPoolId"] = args ? args.identityPoolId : undefined;
            resourceInputs["identityProviderName"] = args ? args.identityProviderName : undefined;
            resourceInputs["principalTags"] = args ? args.principalTags : undefined;
            resourceInputs["useDefaults"] = args ? args.useDefaults : undefined;
        } else {
            resourceInputs["identityPoolId"] = undefined /*out*/;
            resourceInputs["identityProviderName"] = undefined /*out*/;
            resourceInputs["principalTags"] = undefined /*out*/;
            resourceInputs["useDefaults"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        const replaceOnChanges = { replaceOnChanges: ["identityPoolId", "identityProviderName"] };
        opts = pulumi.mergeOptions(opts, replaceOnChanges);
        super(IdentityPoolPrincipalTag.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a IdentityPoolPrincipalTag resource.
 */
export interface IdentityPoolPrincipalTagArgs {
    identityPoolId: pulumi.Input<string>;
    identityProviderName: pulumi.Input<string>;
    /**
     * Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::Cognito::IdentityPoolPrincipalTag` for more information about the expected schema for this property.
     */
    principalTags?: any;
    useDefaults?: pulumi.Input<boolean>;
}
