// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::EC2::CustomerGateway
 */
export class CustomerGateway extends pulumi.CustomResource {
    /**
     * Get an existing CustomerGateway resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): CustomerGateway {
        return new CustomerGateway(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:ec2:CustomerGateway';

    /**
     * Returns true if the given object is an instance of CustomerGateway.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is CustomerGateway {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === CustomerGateway.__pulumiType;
    }

    /**
     * For devices that support BGP, the customer gateway's BGP ASN.
     */
    public readonly bgpAsn!: pulumi.Output<number>;
    /**
     * CustomerGateway ID generated after customer gateway is created. Each customer gateway has a unique ID.
     */
    public /*out*/ readonly customerGatewayId!: pulumi.Output<string>;
    /**
     * A name for the customer gateway device.
     */
    public readonly deviceName!: pulumi.Output<string | undefined>;
    /**
     * The internet-routable IP address for the customer gateway's outside interface. The address must be static.
     */
    public readonly ipAddress!: pulumi.Output<string>;
    /**
     * One or more tags for the customer gateway.
     */
    public readonly tags!: pulumi.Output<outputs.Tag[] | undefined>;
    /**
     * The type of VPN connection that this customer gateway supports.
     */
    public readonly type!: pulumi.Output<string>;

    /**
     * Create a CustomerGateway resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: CustomerGatewayArgs, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.bgpAsn === undefined) && !opts.urn) {
                throw new Error("Missing required property 'bgpAsn'");
            }
            if ((!args || args.ipAddress === undefined) && !opts.urn) {
                throw new Error("Missing required property 'ipAddress'");
            }
            if ((!args || args.type === undefined) && !opts.urn) {
                throw new Error("Missing required property 'type'");
            }
            resourceInputs["bgpAsn"] = args ? args.bgpAsn : undefined;
            resourceInputs["deviceName"] = args ? args.deviceName : undefined;
            resourceInputs["ipAddress"] = args ? args.ipAddress : undefined;
            resourceInputs["tags"] = args ? args.tags : undefined;
            resourceInputs["type"] = args ? args.type : undefined;
            resourceInputs["customerGatewayId"] = undefined /*out*/;
        } else {
            resourceInputs["bgpAsn"] = undefined /*out*/;
            resourceInputs["customerGatewayId"] = undefined /*out*/;
            resourceInputs["deviceName"] = undefined /*out*/;
            resourceInputs["ipAddress"] = undefined /*out*/;
            resourceInputs["tags"] = undefined /*out*/;
            resourceInputs["type"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        const replaceOnChanges = { replaceOnChanges: ["bgpAsn", "deviceName", "ipAddress", "type"] };
        opts = pulumi.mergeOptions(opts, replaceOnChanges);
        super(CustomerGateway.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a CustomerGateway resource.
 */
export interface CustomerGatewayArgs {
    /**
     * For devices that support BGP, the customer gateway's BGP ASN.
     */
    bgpAsn: pulumi.Input<number>;
    /**
     * A name for the customer gateway device.
     */
    deviceName?: pulumi.Input<string>;
    /**
     * The internet-routable IP address for the customer gateway's outside interface. The address must be static.
     */
    ipAddress: pulumi.Input<string>;
    /**
     * One or more tags for the customer gateway.
     */
    tags?: pulumi.Input<pulumi.Input<inputs.TagArgs>[]>;
    /**
     * The type of VPN connection that this customer gateway supports.
     */
    type: pulumi.Input<string>;
}
