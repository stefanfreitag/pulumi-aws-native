// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import { input as inputs, output as outputs, enums } from "../types";
import * as utilities from "../utilities";

/**
 * The AWS::EC2::TransitGatewayConnect type
 */
export class TransitGatewayConnect extends pulumi.CustomResource {
    /**
     * Get an existing TransitGatewayConnect resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): TransitGatewayConnect {
        return new TransitGatewayConnect(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:ec2:TransitGatewayConnect';

    /**
     * Returns true if the given object is an instance of TransitGatewayConnect.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is TransitGatewayConnect {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === TransitGatewayConnect.__pulumiType;
    }

    /**
     * The creation time.
     */
    public /*out*/ readonly creationTime!: pulumi.Output<string>;
    /**
     * The Connect attachment options.
     */
    public readonly options!: pulumi.Output<outputs.ec2.TransitGatewayConnectTransitGatewayConnectOptions>;
    /**
     * The state of the attachment.
     */
    public /*out*/ readonly state!: pulumi.Output<string>;
    /**
     * The tags for the attachment.
     */
    public readonly tags!: pulumi.Output<outputs.ec2.TransitGatewayConnectTag[] | undefined>;
    /**
     * The ID of the Connect attachment.
     */
    public /*out*/ readonly transitGatewayAttachmentId!: pulumi.Output<string>;
    /**
     * The ID of the transit gateway.
     */
    public /*out*/ readonly transitGatewayId!: pulumi.Output<string>;
    /**
     * The ID of the attachment from which the Connect attachment was created.
     */
    public readonly transportTransitGatewayAttachmentId!: pulumi.Output<string>;

    /**
     * Create a TransitGatewayConnect resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: TransitGatewayConnectArgs, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.options === undefined) && !opts.urn) {
                throw new Error("Missing required property 'options'");
            }
            if ((!args || args.transportTransitGatewayAttachmentId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'transportTransitGatewayAttachmentId'");
            }
            inputs["options"] = args ? args.options : undefined;
            inputs["tags"] = args ? args.tags : undefined;
            inputs["transportTransitGatewayAttachmentId"] = args ? args.transportTransitGatewayAttachmentId : undefined;
            inputs["creationTime"] = undefined /*out*/;
            inputs["state"] = undefined /*out*/;
            inputs["transitGatewayAttachmentId"] = undefined /*out*/;
            inputs["transitGatewayId"] = undefined /*out*/;
        } else {
            inputs["creationTime"] = undefined /*out*/;
            inputs["options"] = undefined /*out*/;
            inputs["state"] = undefined /*out*/;
            inputs["tags"] = undefined /*out*/;
            inputs["transitGatewayAttachmentId"] = undefined /*out*/;
            inputs["transitGatewayId"] = undefined /*out*/;
            inputs["transportTransitGatewayAttachmentId"] = undefined /*out*/;
        }
        if (!opts.version) {
            opts = pulumi.mergeOptions(opts, { version: utilities.getVersion()});
        }
        super(TransitGatewayConnect.__pulumiType, name, inputs, opts);
    }
}

/**
 * The set of arguments for constructing a TransitGatewayConnect resource.
 */
export interface TransitGatewayConnectArgs {
    /**
     * The Connect attachment options.
     */
    options: pulumi.Input<inputs.ec2.TransitGatewayConnectTransitGatewayConnectOptionsArgs>;
    /**
     * The tags for the attachment.
     */
    tags?: pulumi.Input<pulumi.Input<inputs.ec2.TransitGatewayConnectTagArgs>[]>;
    /**
     * The ID of the attachment from which the Connect attachment was created.
     */
    transportTransitGatewayAttachmentId: pulumi.Input<string>;
}
