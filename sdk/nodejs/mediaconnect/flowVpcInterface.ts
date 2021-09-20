// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Resource schema for AWS::MediaConnect::FlowVpcInterface
 */
export class FlowVpcInterface extends pulumi.CustomResource {
    /**
     * Get an existing FlowVpcInterface resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): FlowVpcInterface {
        return new FlowVpcInterface(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:mediaconnect:FlowVpcInterface';

    /**
     * Returns true if the given object is an instance of FlowVpcInterface.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is FlowVpcInterface {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === FlowVpcInterface.__pulumiType;
    }

    /**
     * The Amazon Resource Name (ARN), a unique identifier for any AWS resource, of the flow.
     */
    public readonly flowArn!: pulumi.Output<string>;
    /**
     * Immutable and has to be a unique against other VpcInterfaces in this Flow.
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * IDs of the network interfaces created in customer's account by MediaConnect.
     */
    public /*out*/ readonly networkInterfaceIds!: pulumi.Output<string[]>;
    /**
     * Role Arn MediaConnect can assumes to create ENIs in customer's account.
     */
    public readonly roleArn!: pulumi.Output<string>;
    /**
     * Security Group IDs to be used on ENI.
     */
    public readonly securityGroupIds!: pulumi.Output<string[]>;
    /**
     * Subnet must be in the AZ of the Flow
     */
    public readonly subnetId!: pulumi.Output<string>;

    /**
     * Create a FlowVpcInterface resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: FlowVpcInterfaceArgs, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.flowArn === undefined) && !opts.urn) {
                throw new Error("Missing required property 'flowArn'");
            }
            if ((!args || args.name === undefined) && !opts.urn) {
                throw new Error("Missing required property 'name'");
            }
            if ((!args || args.roleArn === undefined) && !opts.urn) {
                throw new Error("Missing required property 'roleArn'");
            }
            if ((!args || args.securityGroupIds === undefined) && !opts.urn) {
                throw new Error("Missing required property 'securityGroupIds'");
            }
            if ((!args || args.subnetId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'subnetId'");
            }
            inputs["flowArn"] = args ? args.flowArn : undefined;
            inputs["name"] = args ? args.name : undefined;
            inputs["roleArn"] = args ? args.roleArn : undefined;
            inputs["securityGroupIds"] = args ? args.securityGroupIds : undefined;
            inputs["subnetId"] = args ? args.subnetId : undefined;
            inputs["networkInterfaceIds"] = undefined /*out*/;
        } else {
            inputs["flowArn"] = undefined /*out*/;
            inputs["name"] = undefined /*out*/;
            inputs["networkInterfaceIds"] = undefined /*out*/;
            inputs["roleArn"] = undefined /*out*/;
            inputs["securityGroupIds"] = undefined /*out*/;
            inputs["subnetId"] = undefined /*out*/;
        }
        if (!opts.version) {
            opts = pulumi.mergeOptions(opts, { version: utilities.getVersion()});
        }
        super(FlowVpcInterface.__pulumiType, name, inputs, opts);
    }
}

/**
 * The set of arguments for constructing a FlowVpcInterface resource.
 */
export interface FlowVpcInterfaceArgs {
    /**
     * The Amazon Resource Name (ARN), a unique identifier for any AWS resource, of the flow.
     */
    flowArn: pulumi.Input<string>;
    /**
     * Immutable and has to be a unique against other VpcInterfaces in this Flow.
     */
    name: pulumi.Input<string>;
    /**
     * Role Arn MediaConnect can assumes to create ENIs in customer's account.
     */
    roleArn: pulumi.Input<string>;
    /**
     * Security Group IDs to be used on ENI.
     */
    securityGroupIds: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * Subnet must be in the AZ of the Flow
     */
    subnetId: pulumi.Input<string>;
}
