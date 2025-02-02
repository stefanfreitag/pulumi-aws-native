// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::IoT::BillingGroup
 */
export class BillingGroup extends pulumi.CustomResource {
    /**
     * Get an existing BillingGroup resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): BillingGroup {
        return new BillingGroup(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:iot:BillingGroup';

    /**
     * Returns true if the given object is an instance of BillingGroup.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is BillingGroup {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === BillingGroup.__pulumiType;
    }

    public /*out*/ readonly arn!: pulumi.Output<string>;
    public readonly billingGroupName!: pulumi.Output<string | undefined>;
    public readonly billingGroupProperties!: pulumi.Output<outputs.iot.BillingGroupPropertiesProperties | undefined>;
    /**
     * An array of key-value pairs to apply to this resource.
     */
    public readonly tags!: pulumi.Output<outputs.Tag[] | undefined>;

    /**
     * Create a BillingGroup resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args?: BillingGroupArgs, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            resourceInputs["billingGroupName"] = args ? args.billingGroupName : undefined;
            resourceInputs["billingGroupProperties"] = args ? args.billingGroupProperties : undefined;
            resourceInputs["tags"] = args ? args.tags : undefined;
            resourceInputs["arn"] = undefined /*out*/;
        } else {
            resourceInputs["arn"] = undefined /*out*/;
            resourceInputs["billingGroupName"] = undefined /*out*/;
            resourceInputs["billingGroupProperties"] = undefined /*out*/;
            resourceInputs["tags"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        const replaceOnChanges = { replaceOnChanges: ["billingGroupName"] };
        opts = pulumi.mergeOptions(opts, replaceOnChanges);
        super(BillingGroup.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a BillingGroup resource.
 */
export interface BillingGroupArgs {
    billingGroupName?: pulumi.Input<string>;
    billingGroupProperties?: pulumi.Input<inputs.iot.BillingGroupPropertiesPropertiesArgs>;
    /**
     * An array of key-value pairs to apply to this resource.
     */
    tags?: pulumi.Input<pulumi.Input<inputs.TagArgs>[]>;
}
