// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import { input as inputs, output as outputs, enums } from "../types";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::EC2::SpotFleet
 */
export class SpotFleet extends pulumi.CustomResource {
    /**
     * Get an existing SpotFleet resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): SpotFleet {
        return new SpotFleet(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:ec2:SpotFleet';

    /**
     * Returns true if the given object is an instance of SpotFleet.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is SpotFleet {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === SpotFleet.__pulumiType;
    }

    public readonly spotFleetRequestConfigData!: pulumi.Output<outputs.ec2.SpotFleetSpotFleetRequestConfigData>;

    /**
     * Create a SpotFleet resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: SpotFleetArgs, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.spotFleetRequestConfigData === undefined) && !opts.urn) {
                throw new Error("Missing required property 'spotFleetRequestConfigData'");
            }
            inputs["spotFleetRequestConfigData"] = args ? args.spotFleetRequestConfigData : undefined;
        } else {
            inputs["spotFleetRequestConfigData"] = undefined /*out*/;
        }
        if (!opts.version) {
            opts = pulumi.mergeOptions(opts, { version: utilities.getVersion()});
        }
        super(SpotFleet.__pulumiType, name, inputs, opts);
    }
}

/**
 * The set of arguments for constructing a SpotFleet resource.
 */
export interface SpotFleetArgs {
    spotFleetRequestConfigData: pulumi.Input<inputs.ec2.SpotFleetSpotFleetRequestConfigDataArgs>;
}
