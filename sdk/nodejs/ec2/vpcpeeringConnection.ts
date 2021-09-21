// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import { input as inputs, output as outputs, enums } from "../types";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::EC2::VPCPeeringConnection
 *
 * @deprecated VPCPeeringConnection is not yet supported by AWS Cloud Control API, so its creation will currently fail. Please use the classic AWS provider, if possible.
 */
export class VPCPeeringConnection extends pulumi.CustomResource {
    /**
     * Get an existing VPCPeeringConnection resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): VPCPeeringConnection {
        pulumi.log.warn("VPCPeeringConnection is deprecated: VPCPeeringConnection is not yet supported by AWS Cloud Control API, so its creation will currently fail. Please use the classic AWS provider, if possible.")
        return new VPCPeeringConnection(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:ec2:VPCPeeringConnection';

    /**
     * Returns true if the given object is an instance of VPCPeeringConnection.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is VPCPeeringConnection {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === VPCPeeringConnection.__pulumiType;
    }

    public readonly peerOwnerId!: pulumi.Output<string | undefined>;
    public readonly peerRegion!: pulumi.Output<string | undefined>;
    public readonly peerRoleArn!: pulumi.Output<string | undefined>;
    public readonly peerVpcId!: pulumi.Output<string>;
    public readonly tags!: pulumi.Output<outputs.ec2.VPCPeeringConnectionTag[] | undefined>;
    public readonly vpcId!: pulumi.Output<string>;

    /**
     * Create a VPCPeeringConnection resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    /** @deprecated VPCPeeringConnection is not yet supported by AWS Cloud Control API, so its creation will currently fail. Please use the classic AWS provider, if possible. */
    constructor(name: string, args: VPCPeeringConnectionArgs, opts?: pulumi.CustomResourceOptions) {
        pulumi.log.warn("VPCPeeringConnection is deprecated: VPCPeeringConnection is not yet supported by AWS Cloud Control API, so its creation will currently fail. Please use the classic AWS provider, if possible.")
        let inputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.peerVpcId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'peerVpcId'");
            }
            if ((!args || args.vpcId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'vpcId'");
            }
            inputs["peerOwnerId"] = args ? args.peerOwnerId : undefined;
            inputs["peerRegion"] = args ? args.peerRegion : undefined;
            inputs["peerRoleArn"] = args ? args.peerRoleArn : undefined;
            inputs["peerVpcId"] = args ? args.peerVpcId : undefined;
            inputs["tags"] = args ? args.tags : undefined;
            inputs["vpcId"] = args ? args.vpcId : undefined;
        } else {
            inputs["peerOwnerId"] = undefined /*out*/;
            inputs["peerRegion"] = undefined /*out*/;
            inputs["peerRoleArn"] = undefined /*out*/;
            inputs["peerVpcId"] = undefined /*out*/;
            inputs["tags"] = undefined /*out*/;
            inputs["vpcId"] = undefined /*out*/;
        }
        if (!opts.version) {
            opts = pulumi.mergeOptions(opts, { version: utilities.getVersion()});
        }
        super(VPCPeeringConnection.__pulumiType, name, inputs, opts);
    }
}

/**
 * The set of arguments for constructing a VPCPeeringConnection resource.
 */
export interface VPCPeeringConnectionArgs {
    peerOwnerId?: pulumi.Input<string>;
    peerRegion?: pulumi.Input<string>;
    peerRoleArn?: pulumi.Input<string>;
    peerVpcId: pulumi.Input<string>;
    tags?: pulumi.Input<pulumi.Input<inputs.ec2.VPCPeeringConnectionTagArgs>[]>;
    vpcId: pulumi.Input<string>;
}
