// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Resource schema for AWS::SageMaker::Device
 */
export class Device extends pulumi.CustomResource {
    /**
     * Get an existing Device resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): Device {
        return new Device(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:sagemaker:Device';

    /**
     * Returns true if the given object is an instance of Device.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Device {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Device.__pulumiType;
    }

    /**
     * The Edge Device you want to register against a device fleet
     */
    public readonly device!: pulumi.Output<outputs.sagemaker.Device | undefined>;
    /**
     * The name of the edge device fleet
     */
    public readonly deviceFleetName!: pulumi.Output<string>;
    /**
     * Associate tags with the resource
     */
    public readonly tags!: pulumi.Output<outputs.Tag[] | undefined>;

    /**
     * Create a Device resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: DeviceArgs, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.deviceFleetName === undefined) && !opts.urn) {
                throw new Error("Missing required property 'deviceFleetName'");
            }
            resourceInputs["device"] = args ? args.device : undefined;
            resourceInputs["deviceFleetName"] = args ? args.deviceFleetName : undefined;
            resourceInputs["tags"] = args ? args.tags : undefined;
        } else {
            resourceInputs["device"] = undefined /*out*/;
            resourceInputs["deviceFleetName"] = undefined /*out*/;
            resourceInputs["tags"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        const replaceOnChanges = { replaceOnChanges: ["device.deviceName"] };
        opts = pulumi.mergeOptions(opts, replaceOnChanges);
        super(Device.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a Device resource.
 */
export interface DeviceArgs {
    /**
     * The Edge Device you want to register against a device fleet
     */
    device?: pulumi.Input<inputs.sagemaker.DeviceArgs>;
    /**
     * The name of the edge device fleet
     */
    deviceFleetName: pulumi.Input<string>;
    /**
     * Associate tags with the resource
     */
    tags?: pulumi.Input<pulumi.Input<inputs.TagArgs>[]>;
}
