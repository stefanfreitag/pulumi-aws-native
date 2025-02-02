// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Definition of AWS::MediaTailor::ChannelPolicy Resource Type
 */
export class ChannelPolicy extends pulumi.CustomResource {
    /**
     * Get an existing ChannelPolicy resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): ChannelPolicy {
        return new ChannelPolicy(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:mediatailor:ChannelPolicy';

    /**
     * Returns true if the given object is an instance of ChannelPolicy.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is ChannelPolicy {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === ChannelPolicy.__pulumiType;
    }

    public readonly channelName!: pulumi.Output<string>;
    /**
     * <p>The IAM policy for the channel. IAM policies are used to control access to your channel.</p>
     *
     * Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::MediaTailor::ChannelPolicy` for more information about the expected schema for this property.
     */
    public readonly policy!: pulumi.Output<any>;

    /**
     * Create a ChannelPolicy resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: ChannelPolicyArgs, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.channelName === undefined) && !opts.urn) {
                throw new Error("Missing required property 'channelName'");
            }
            if ((!args || args.policy === undefined) && !opts.urn) {
                throw new Error("Missing required property 'policy'");
            }
            resourceInputs["channelName"] = args ? args.channelName : undefined;
            resourceInputs["policy"] = args ? args.policy : undefined;
        } else {
            resourceInputs["channelName"] = undefined /*out*/;
            resourceInputs["policy"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        const replaceOnChanges = { replaceOnChanges: ["channelName"] };
        opts = pulumi.mergeOptions(opts, replaceOnChanges);
        super(ChannelPolicy.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a ChannelPolicy resource.
 */
export interface ChannelPolicyArgs {
    channelName: pulumi.Input<string>;
    /**
     * <p>The IAM policy for the channel. IAM policies are used to control access to your channel.</p>
     *
     * Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::MediaTailor::ChannelPolicy` for more information about the expected schema for this property.
     */
    policy: any;
}
