// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::Connect::PhoneNumber
 */
export class PhoneNumber extends pulumi.CustomResource {
    /**
     * Get an existing PhoneNumber resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): PhoneNumber {
        return new PhoneNumber(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:connect:PhoneNumber';

    /**
     * Returns true if the given object is an instance of PhoneNumber.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is PhoneNumber {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === PhoneNumber.__pulumiType;
    }

    /**
     * The phone number e164 address.
     */
    public /*out*/ readonly address!: pulumi.Output<string>;
    /**
     * The phone number country code.
     */
    public readonly countryCode!: pulumi.Output<string>;
    /**
     * The description of the phone number.
     */
    public readonly description!: pulumi.Output<string | undefined>;
    /**
     * The phone number ARN
     */
    public /*out*/ readonly phoneNumberArn!: pulumi.Output<string>;
    /**
     * The phone number prefix.
     */
    public readonly prefix!: pulumi.Output<string | undefined>;
    /**
     * One or more tags.
     */
    public readonly tags!: pulumi.Output<outputs.connect.PhoneNumberTag[] | undefined>;
    /**
     * The ARN of the target the phone number is claimed to.
     */
    public readonly targetArn!: pulumi.Output<string>;
    /**
     * The phone number type
     */
    public readonly type!: pulumi.Output<string>;

    /**
     * Create a PhoneNumber resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: PhoneNumberArgs, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.countryCode === undefined) && !opts.urn) {
                throw new Error("Missing required property 'countryCode'");
            }
            if ((!args || args.targetArn === undefined) && !opts.urn) {
                throw new Error("Missing required property 'targetArn'");
            }
            if ((!args || args.type === undefined) && !opts.urn) {
                throw new Error("Missing required property 'type'");
            }
            resourceInputs["countryCode"] = args ? args.countryCode : undefined;
            resourceInputs["description"] = args ? args.description : undefined;
            resourceInputs["prefix"] = args ? args.prefix : undefined;
            resourceInputs["tags"] = args ? args.tags : undefined;
            resourceInputs["targetArn"] = args ? args.targetArn : undefined;
            resourceInputs["type"] = args ? args.type : undefined;
            resourceInputs["address"] = undefined /*out*/;
            resourceInputs["phoneNumberArn"] = undefined /*out*/;
        } else {
            resourceInputs["address"] = undefined /*out*/;
            resourceInputs["countryCode"] = undefined /*out*/;
            resourceInputs["description"] = undefined /*out*/;
            resourceInputs["phoneNumberArn"] = undefined /*out*/;
            resourceInputs["prefix"] = undefined /*out*/;
            resourceInputs["tags"] = undefined /*out*/;
            resourceInputs["targetArn"] = undefined /*out*/;
            resourceInputs["type"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(PhoneNumber.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a PhoneNumber resource.
 */
export interface PhoneNumberArgs {
    /**
     * The phone number country code.
     */
    countryCode: pulumi.Input<string>;
    /**
     * The description of the phone number.
     */
    description?: pulumi.Input<string>;
    /**
     * The phone number prefix.
     */
    prefix?: pulumi.Input<string>;
    /**
     * One or more tags.
     */
    tags?: pulumi.Input<pulumi.Input<inputs.connect.PhoneNumberTagArgs>[]>;
    /**
     * The ARN of the target the phone number is claimed to.
     */
    targetArn: pulumi.Input<string>;
    /**
     * The phone number type
     */
    type: pulumi.Input<string>;
}
