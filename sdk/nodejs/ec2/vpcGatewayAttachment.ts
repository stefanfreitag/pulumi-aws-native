// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::EC2::VPCGatewayAttachment
 */
export class VpcGatewayAttachment extends pulumi.CustomResource {
    /**
     * Get an existing VpcGatewayAttachment resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): VpcGatewayAttachment {
        return new VpcGatewayAttachment(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:ec2:VpcGatewayAttachment';

    /**
     * Returns true if the given object is an instance of VpcGatewayAttachment.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is VpcGatewayAttachment {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === VpcGatewayAttachment.__pulumiType;
    }

    /**
     * Used to identify if this resource is an Internet Gateway or Vpn Gateway Attachment 
     */
    public /*out*/ readonly attachmentType!: pulumi.Output<string>;
    /**
     * The ID of the internet gateway. You must specify either InternetGatewayId or VpnGatewayId, but not both.
     */
    public readonly internetGatewayId!: pulumi.Output<string | undefined>;
    /**
     * The ID of the VPC.
     */
    public readonly vpcId!: pulumi.Output<string>;
    /**
     * The ID of the virtual private gateway. You must specify either InternetGatewayId or VpnGatewayId, but not both.
     */
    public readonly vpnGatewayId!: pulumi.Output<string | undefined>;

    /**
     * Create a VpcGatewayAttachment resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: VpcGatewayAttachmentArgs, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.vpcId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'vpcId'");
            }
            resourceInputs["internetGatewayId"] = args ? args.internetGatewayId : undefined;
            resourceInputs["vpcId"] = args ? args.vpcId : undefined;
            resourceInputs["vpnGatewayId"] = args ? args.vpnGatewayId : undefined;
            resourceInputs["attachmentType"] = undefined /*out*/;
        } else {
            resourceInputs["attachmentType"] = undefined /*out*/;
            resourceInputs["internetGatewayId"] = undefined /*out*/;
            resourceInputs["vpcId"] = undefined /*out*/;
            resourceInputs["vpnGatewayId"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        const replaceOnChanges = { replaceOnChanges: ["vpcId"] };
        opts = pulumi.mergeOptions(opts, replaceOnChanges);
        super(VpcGatewayAttachment.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a VpcGatewayAttachment resource.
 */
export interface VpcGatewayAttachmentArgs {
    /**
     * The ID of the internet gateway. You must specify either InternetGatewayId or VpnGatewayId, but not both.
     */
    internetGatewayId?: pulumi.Input<string>;
    /**
     * The ID of the VPC.
     */
    vpcId: pulumi.Input<string>;
    /**
     * The ID of the virtual private gateway. You must specify either InternetGatewayId or VpnGatewayId, but not both.
     */
    vpnGatewayId?: pulumi.Input<string>;
}
