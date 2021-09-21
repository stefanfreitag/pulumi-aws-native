// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::EC2::VPCGatewayAttachment
 *
 * @deprecated VPCGatewayAttachment is not yet supported by AWS Cloud Control API, so its creation will currently fail. Please use the classic AWS provider, if possible.
 */
export class VPCGatewayAttachment extends pulumi.CustomResource {
    /**
     * Get an existing VPCGatewayAttachment resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): VPCGatewayAttachment {
        pulumi.log.warn("VPCGatewayAttachment is deprecated: VPCGatewayAttachment is not yet supported by AWS Cloud Control API, so its creation will currently fail. Please use the classic AWS provider, if possible.")
        return new VPCGatewayAttachment(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:ec2:VPCGatewayAttachment';

    /**
     * Returns true if the given object is an instance of VPCGatewayAttachment.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is VPCGatewayAttachment {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === VPCGatewayAttachment.__pulumiType;
    }

    public readonly internetGatewayId!: pulumi.Output<string | undefined>;
    public readonly vpcId!: pulumi.Output<string>;
    public readonly vpnGatewayId!: pulumi.Output<string | undefined>;

    /**
     * Create a VPCGatewayAttachment resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    /** @deprecated VPCGatewayAttachment is not yet supported by AWS Cloud Control API, so its creation will currently fail. Please use the classic AWS provider, if possible. */
    constructor(name: string, args: VPCGatewayAttachmentArgs, opts?: pulumi.CustomResourceOptions) {
        pulumi.log.warn("VPCGatewayAttachment is deprecated: VPCGatewayAttachment is not yet supported by AWS Cloud Control API, so its creation will currently fail. Please use the classic AWS provider, if possible.")
        let inputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.vpcId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'vpcId'");
            }
            inputs["internetGatewayId"] = args ? args.internetGatewayId : undefined;
            inputs["vpcId"] = args ? args.vpcId : undefined;
            inputs["vpnGatewayId"] = args ? args.vpnGatewayId : undefined;
        } else {
            inputs["internetGatewayId"] = undefined /*out*/;
            inputs["vpcId"] = undefined /*out*/;
            inputs["vpnGatewayId"] = undefined /*out*/;
        }
        if (!opts.version) {
            opts = pulumi.mergeOptions(opts, { version: utilities.getVersion()});
        }
        super(VPCGatewayAttachment.__pulumiType, name, inputs, opts);
    }
}

/**
 * The set of arguments for constructing a VPCGatewayAttachment resource.
 */
export interface VPCGatewayAttachmentArgs {
    internetGatewayId?: pulumi.Input<string>;
    vpcId: pulumi.Input<string>;
    vpnGatewayId?: pulumi.Input<string>;
}
