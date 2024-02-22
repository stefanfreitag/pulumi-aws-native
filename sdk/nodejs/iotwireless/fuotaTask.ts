// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Create and manage FUOTA tasks.
 */
export class FuotaTask extends pulumi.CustomResource {
    /**
     * Get an existing FuotaTask resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): FuotaTask {
        return new FuotaTask(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:iotwireless:FuotaTask';

    /**
     * Returns true if the given object is an instance of FuotaTask.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is FuotaTask {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === FuotaTask.__pulumiType;
    }

    /**
     * FUOTA task arn. Returned after successful create.
     */
    public /*out*/ readonly arn!: pulumi.Output<string>;
    /**
     * Multicast group to associate. Only for update request.
     */
    public readonly associateMulticastGroup!: pulumi.Output<string | undefined>;
    /**
     * Wireless device to associate. Only for update request.
     */
    public readonly associateWirelessDevice!: pulumi.Output<string | undefined>;
    /**
     * FUOTA task description
     */
    public readonly description!: pulumi.Output<string | undefined>;
    /**
     * Multicast group to disassociate. Only for update request.
     */
    public readonly disassociateMulticastGroup!: pulumi.Output<string | undefined>;
    /**
     * Wireless device to disassociate. Only for update request.
     */
    public readonly disassociateWirelessDevice!: pulumi.Output<string | undefined>;
    /**
     * FUOTA task firmware update image binary S3 link
     */
    public readonly firmwareUpdateImage!: pulumi.Output<string>;
    /**
     * FUOTA task firmware IAM role for reading S3
     */
    public readonly firmwareUpdateRole!: pulumi.Output<string>;
    /**
     * FUOTA task status. Returned after successful read.
     */
    public /*out*/ readonly fuotaTaskStatus!: pulumi.Output<string>;
    /**
     * FUOTA task LoRaWAN
     */
    public readonly loRaWan!: pulumi.Output<outputs.iotwireless.FuotaTaskLoRaWan>;
    /**
     * Name of FUOTA task
     */
    public readonly name!: pulumi.Output<string | undefined>;
    /**
     * A list of key-value pairs that contain metadata for the FUOTA task.
     */
    public readonly tags!: pulumi.Output<outputs.Tag[] | undefined>;

    /**
     * Create a FuotaTask resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: FuotaTaskArgs, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.firmwareUpdateImage === undefined) && !opts.urn) {
                throw new Error("Missing required property 'firmwareUpdateImage'");
            }
            if ((!args || args.firmwareUpdateRole === undefined) && !opts.urn) {
                throw new Error("Missing required property 'firmwareUpdateRole'");
            }
            if ((!args || args.loRaWan === undefined) && !opts.urn) {
                throw new Error("Missing required property 'loRaWan'");
            }
            resourceInputs["associateMulticastGroup"] = args ? args.associateMulticastGroup : undefined;
            resourceInputs["associateWirelessDevice"] = args ? args.associateWirelessDevice : undefined;
            resourceInputs["description"] = args ? args.description : undefined;
            resourceInputs["disassociateMulticastGroup"] = args ? args.disassociateMulticastGroup : undefined;
            resourceInputs["disassociateWirelessDevice"] = args ? args.disassociateWirelessDevice : undefined;
            resourceInputs["firmwareUpdateImage"] = args ? args.firmwareUpdateImage : undefined;
            resourceInputs["firmwareUpdateRole"] = args ? args.firmwareUpdateRole : undefined;
            resourceInputs["loRaWan"] = args ? args.loRaWan : undefined;
            resourceInputs["name"] = args ? args.name : undefined;
            resourceInputs["tags"] = args ? args.tags : undefined;
            resourceInputs["arn"] = undefined /*out*/;
            resourceInputs["fuotaTaskStatus"] = undefined /*out*/;
        } else {
            resourceInputs["arn"] = undefined /*out*/;
            resourceInputs["associateMulticastGroup"] = undefined /*out*/;
            resourceInputs["associateWirelessDevice"] = undefined /*out*/;
            resourceInputs["description"] = undefined /*out*/;
            resourceInputs["disassociateMulticastGroup"] = undefined /*out*/;
            resourceInputs["disassociateWirelessDevice"] = undefined /*out*/;
            resourceInputs["firmwareUpdateImage"] = undefined /*out*/;
            resourceInputs["firmwareUpdateRole"] = undefined /*out*/;
            resourceInputs["fuotaTaskStatus"] = undefined /*out*/;
            resourceInputs["loRaWan"] = undefined /*out*/;
            resourceInputs["name"] = undefined /*out*/;
            resourceInputs["tags"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(FuotaTask.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a FuotaTask resource.
 */
export interface FuotaTaskArgs {
    /**
     * Multicast group to associate. Only for update request.
     */
    associateMulticastGroup?: pulumi.Input<string>;
    /**
     * Wireless device to associate. Only for update request.
     */
    associateWirelessDevice?: pulumi.Input<string>;
    /**
     * FUOTA task description
     */
    description?: pulumi.Input<string>;
    /**
     * Multicast group to disassociate. Only for update request.
     */
    disassociateMulticastGroup?: pulumi.Input<string>;
    /**
     * Wireless device to disassociate. Only for update request.
     */
    disassociateWirelessDevice?: pulumi.Input<string>;
    /**
     * FUOTA task firmware update image binary S3 link
     */
    firmwareUpdateImage: pulumi.Input<string>;
    /**
     * FUOTA task firmware IAM role for reading S3
     */
    firmwareUpdateRole: pulumi.Input<string>;
    /**
     * FUOTA task LoRaWAN
     */
    loRaWan: pulumi.Input<inputs.iotwireless.FuotaTaskLoRaWanArgs>;
    /**
     * Name of FUOTA task
     */
    name?: pulumi.Input<string>;
    /**
     * A list of key-value pairs that contain metadata for the FUOTA task.
     */
    tags?: pulumi.Input<pulumi.Input<inputs.TagArgs>[]>;
}
