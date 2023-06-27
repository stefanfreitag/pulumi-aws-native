// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::EC2::EIP
 */
export class EIP extends pulumi.CustomResource {
    /**
     * Get an existing EIP resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): EIP {
        return new EIP(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:ec2:EIP';

    /**
     * Returns true if the given object is an instance of EIP.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is EIP {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === EIP.__pulumiType;
    }

    /**
     * The Allocation ID of the EIP generated by resource.
     */
    public /*out*/ readonly allocationId!: pulumi.Output<string>;
    /**
     * Indicates whether the Elastic IP address is for use with instances in a VPC or instance in EC2-Classic.
     */
    public readonly domain!: pulumi.Output<string | undefined>;
    /**
     * The ID of the instance.
     */
    public readonly instanceId!: pulumi.Output<string | undefined>;
    /**
     * A unique set of Availability Zones, Local Zones, or Wavelength Zones from which Amazon Web Services advertises IP addresses.
     */
    public readonly networkBorderGroup!: pulumi.Output<string | undefined>;
    /**
     * The PublicIP of the EIP generated by resource.
     */
    public /*out*/ readonly publicIp!: pulumi.Output<string>;
    /**
     * The ID of an address pool that you own. Use this parameter to let Amazon EC2 select an address from the address pool.
     */
    public readonly publicIpv4Pool!: pulumi.Output<string | undefined>;
    /**
     * Any tags assigned to the EIP.
     */
    public readonly tags!: pulumi.Output<outputs.ec2.EIPTag[] | undefined>;
    /**
     * The PublicIP of the EIP generated by resource through transfer from another account
     */
    public readonly transferAddress!: pulumi.Output<string | undefined>;

    /**
     * Create a EIP resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args?: EIPArgs, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            resourceInputs["domain"] = args ? args.domain : undefined;
            resourceInputs["instanceId"] = args ? args.instanceId : undefined;
            resourceInputs["networkBorderGroup"] = args ? args.networkBorderGroup : undefined;
            resourceInputs["publicIpv4Pool"] = args ? args.publicIpv4Pool : undefined;
            resourceInputs["tags"] = args ? args.tags : undefined;
            resourceInputs["transferAddress"] = args ? args.transferAddress : undefined;
            resourceInputs["allocationId"] = undefined /*out*/;
            resourceInputs["publicIp"] = undefined /*out*/;
        } else {
            resourceInputs["allocationId"] = undefined /*out*/;
            resourceInputs["domain"] = undefined /*out*/;
            resourceInputs["instanceId"] = undefined /*out*/;
            resourceInputs["networkBorderGroup"] = undefined /*out*/;
            resourceInputs["publicIp"] = undefined /*out*/;
            resourceInputs["publicIpv4Pool"] = undefined /*out*/;
            resourceInputs["tags"] = undefined /*out*/;
            resourceInputs["transferAddress"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(EIP.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a EIP resource.
 */
export interface EIPArgs {
    /**
     * Indicates whether the Elastic IP address is for use with instances in a VPC or instance in EC2-Classic.
     */
    domain?: pulumi.Input<string>;
    /**
     * The ID of the instance.
     */
    instanceId?: pulumi.Input<string>;
    /**
     * A unique set of Availability Zones, Local Zones, or Wavelength Zones from which Amazon Web Services advertises IP addresses.
     */
    networkBorderGroup?: pulumi.Input<string>;
    /**
     * The ID of an address pool that you own. Use this parameter to let Amazon EC2 select an address from the address pool.
     */
    publicIpv4Pool?: pulumi.Input<string>;
    /**
     * Any tags assigned to the EIP.
     */
    tags?: pulumi.Input<pulumi.Input<inputs.ec2.EIPTagArgs>[]>;
    /**
     * The PublicIP of the EIP generated by resource through transfer from another account
     */
    transferAddress?: pulumi.Input<string>;
}
