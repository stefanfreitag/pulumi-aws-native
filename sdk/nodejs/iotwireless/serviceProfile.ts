// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * An example resource schema demonstrating some basic constructs and validation rules.
 */
export class ServiceProfile extends pulumi.CustomResource {
    /**
     * Get an existing ServiceProfile resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): ServiceProfile {
        return new ServiceProfile(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:iotwireless:ServiceProfile';

    /**
     * Returns true if the given object is an instance of ServiceProfile.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is ServiceProfile {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === ServiceProfile.__pulumiType;
    }

    /**
     * Service profile Arn. Returned after successful create.
     */
    public /*out*/ readonly arn!: pulumi.Output<string>;
    /**
     * LoRaWAN supports all LoRa specific attributes for service profile for CreateServiceProfile operation
     */
    public readonly loRaWan!: pulumi.Output<outputs.iotwireless.ServiceProfileLoRaWanServiceProfile | undefined>;
    /**
     * Name of service profile
     */
    public readonly name!: pulumi.Output<string | undefined>;
    /**
     * A list of key-value pairs that contain metadata for the service profile.
     */
    public readonly tags!: pulumi.Output<outputs.Tag[] | undefined>;

    /**
     * Create a ServiceProfile resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args?: ServiceProfileArgs, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            resourceInputs["loRaWan"] = args ? args.loRaWan : undefined;
            resourceInputs["name"] = args ? args.name : undefined;
            resourceInputs["tags"] = args ? args.tags : undefined;
            resourceInputs["arn"] = undefined /*out*/;
        } else {
            resourceInputs["arn"] = undefined /*out*/;
            resourceInputs["loRaWan"] = undefined /*out*/;
            resourceInputs["name"] = undefined /*out*/;
            resourceInputs["tags"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(ServiceProfile.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a ServiceProfile resource.
 */
export interface ServiceProfileArgs {
    /**
     * LoRaWAN supports all LoRa specific attributes for service profile for CreateServiceProfile operation
     */
    loRaWan?: pulumi.Input<inputs.iotwireless.ServiceProfileLoRaWanServiceProfileArgs>;
    /**
     * Name of service profile
     */
    name?: pulumi.Input<string>;
    /**
     * A list of key-value pairs that contain metadata for the service profile.
     */
    tags?: pulumi.Input<pulumi.Input<inputs.TagArgs>[]>;
}
