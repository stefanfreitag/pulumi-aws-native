// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import { input as inputs, output as outputs, enums } from "../types";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::GlobalAccelerator::Accelerator
 */
export class Accelerator extends pulumi.CustomResource {
    /**
     * Get an existing Accelerator resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): Accelerator {
        return new Accelerator(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:globalaccelerator:Accelerator';

    /**
     * Returns true if the given object is an instance of Accelerator.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Accelerator {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Accelerator.__pulumiType;
    }

    /**
     * The Amazon Resource Name (ARN) of the accelerator.
     */
    public /*out*/ readonly acceleratorArn!: pulumi.Output<string>;
    /**
     * The Domain Name System (DNS) name that Global Accelerator creates that points to your accelerator's static IPv4 addresses.
     */
    public /*out*/ readonly dnsName!: pulumi.Output<string>;
    /**
     * The Domain Name System (DNS) name that Global Accelerator creates that points to your accelerator's static IPv4 and IPv6 addresses.
     */
    public /*out*/ readonly dualStackDnsName!: pulumi.Output<string>;
    /**
     * Indicates whether an accelerator is enabled. The value is true or false.
     */
    public readonly enabled!: pulumi.Output<boolean | undefined>;
    /**
     * IP Address type.
     */
    public readonly ipAddressType!: pulumi.Output<enums.globalaccelerator.AcceleratorIpAddressType | undefined>;
    /**
     * The IP addresses from BYOIP Prefix pool.
     */
    public readonly ipAddresses!: pulumi.Output<string[] | undefined>;
    /**
     * The IPv4 addresses assigned to the accelerator.
     */
    public /*out*/ readonly ipv4Addresses!: pulumi.Output<string[]>;
    /**
     * The IPv6 addresses assigned if the accelerator is dualstack
     */
    public /*out*/ readonly ipv6Addresses!: pulumi.Output<string[]>;
    /**
     * Name of accelerator.
     */
    public readonly name!: pulumi.Output<string>;
    public readonly tags!: pulumi.Output<outputs.globalaccelerator.AcceleratorTag[] | undefined>;

    /**
     * Create a Accelerator resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args?: AcceleratorArgs, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            resourceInputs["enabled"] = args ? args.enabled : undefined;
            resourceInputs["ipAddressType"] = args ? args.ipAddressType : undefined;
            resourceInputs["ipAddresses"] = args ? args.ipAddresses : undefined;
            resourceInputs["name"] = args ? args.name : undefined;
            resourceInputs["tags"] = args ? args.tags : undefined;
            resourceInputs["acceleratorArn"] = undefined /*out*/;
            resourceInputs["dnsName"] = undefined /*out*/;
            resourceInputs["dualStackDnsName"] = undefined /*out*/;
            resourceInputs["ipv4Addresses"] = undefined /*out*/;
            resourceInputs["ipv6Addresses"] = undefined /*out*/;
        } else {
            resourceInputs["acceleratorArn"] = undefined /*out*/;
            resourceInputs["dnsName"] = undefined /*out*/;
            resourceInputs["dualStackDnsName"] = undefined /*out*/;
            resourceInputs["enabled"] = undefined /*out*/;
            resourceInputs["ipAddressType"] = undefined /*out*/;
            resourceInputs["ipAddresses"] = undefined /*out*/;
            resourceInputs["ipv4Addresses"] = undefined /*out*/;
            resourceInputs["ipv6Addresses"] = undefined /*out*/;
            resourceInputs["name"] = undefined /*out*/;
            resourceInputs["tags"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(Accelerator.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a Accelerator resource.
 */
export interface AcceleratorArgs {
    /**
     * Indicates whether an accelerator is enabled. The value is true or false.
     */
    enabled?: pulumi.Input<boolean>;
    /**
     * IP Address type.
     */
    ipAddressType?: pulumi.Input<enums.globalaccelerator.AcceleratorIpAddressType>;
    /**
     * The IP addresses from BYOIP Prefix pool.
     */
    ipAddresses?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * Name of accelerator.
     */
    name?: pulumi.Input<string>;
    tags?: pulumi.Input<pulumi.Input<inputs.globalaccelerator.AcceleratorTagArgs>[]>;
}
