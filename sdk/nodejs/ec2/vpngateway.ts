// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import { input as inputs, output as outputs, enums } from "../types";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::EC2::VPNGateway
 *
 * @deprecated VPNGateway is not yet supported by AWS Cloud Control API, so its creation will currently fail. Please use the classic AWS provider, if possible.
 */
export class VPNGateway extends pulumi.CustomResource {
    /**
     * Get an existing VPNGateway resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): VPNGateway {
        pulumi.log.warn("VPNGateway is deprecated: VPNGateway is not yet supported by AWS Cloud Control API, so its creation will currently fail. Please use the classic AWS provider, if possible.")
        return new VPNGateway(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:ec2:VPNGateway';

    /**
     * Returns true if the given object is an instance of VPNGateway.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is VPNGateway {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === VPNGateway.__pulumiType;
    }

    public readonly amazonSideAsn!: pulumi.Output<number | undefined>;
    public readonly tags!: pulumi.Output<outputs.ec2.VPNGatewayTag[] | undefined>;
    public readonly type!: pulumi.Output<string>;

    /**
     * Create a VPNGateway resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    /** @deprecated VPNGateway is not yet supported by AWS Cloud Control API, so its creation will currently fail. Please use the classic AWS provider, if possible. */
    constructor(name: string, args: VPNGatewayArgs, opts?: pulumi.CustomResourceOptions) {
        pulumi.log.warn("VPNGateway is deprecated: VPNGateway is not yet supported by AWS Cloud Control API, so its creation will currently fail. Please use the classic AWS provider, if possible.")
        let inputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.type === undefined) && !opts.urn) {
                throw new Error("Missing required property 'type'");
            }
            inputs["amazonSideAsn"] = args ? args.amazonSideAsn : undefined;
            inputs["tags"] = args ? args.tags : undefined;
            inputs["type"] = args ? args.type : undefined;
        } else {
            inputs["amazonSideAsn"] = undefined /*out*/;
            inputs["tags"] = undefined /*out*/;
            inputs["type"] = undefined /*out*/;
        }
        if (!opts.version) {
            opts = pulumi.mergeOptions(opts, { version: utilities.getVersion()});
        }
        super(VPNGateway.__pulumiType, name, inputs, opts);
    }
}

/**
 * The set of arguments for constructing a VPNGateway resource.
 */
export interface VPNGatewayArgs {
    amazonSideAsn?: pulumi.Input<number>;
    tags?: pulumi.Input<pulumi.Input<inputs.ec2.VPNGatewayTagArgs>[]>;
    type: pulumi.Input<string>;
}
