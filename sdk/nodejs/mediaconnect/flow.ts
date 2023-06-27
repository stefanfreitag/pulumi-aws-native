// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Resource schema for AWS::MediaConnect::Flow
 */
export class Flow extends pulumi.CustomResource {
    /**
     * Get an existing Flow resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): Flow {
        return new Flow(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:mediaconnect:Flow';

    /**
     * Returns true if the given object is an instance of Flow.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Flow {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Flow.__pulumiType;
    }

    /**
     * The Availability Zone that you want to create the flow in. These options are limited to the Availability Zones within the current AWS.
     */
    public readonly availabilityZone!: pulumi.Output<string | undefined>;
    /**
     * The Amazon Resource Name (ARN), a unique identifier for any AWS resource, of the flow.
     */
    public /*out*/ readonly flowArn!: pulumi.Output<string>;
    /**
     * The Availability Zone that you want to create the flow in. These options are limited to the Availability Zones within the current AWS.(ReadOnly)
     */
    public /*out*/ readonly flowAvailabilityZone!: pulumi.Output<string>;
    /**
     * The name of the flow.
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * The source of the flow.
     */
    public readonly source!: pulumi.Output<outputs.mediaconnect.FlowSource>;
    /**
     * The source failover config of the flow.
     */
    public readonly sourceFailoverConfig!: pulumi.Output<outputs.mediaconnect.FlowFailoverConfig | undefined>;

    /**
     * Create a Flow resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: FlowArgs, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.source === undefined) && !opts.urn) {
                throw new Error("Missing required property 'source'");
            }
            resourceInputs["availabilityZone"] = args ? args.availabilityZone : undefined;
            resourceInputs["name"] = args ? args.name : undefined;
            resourceInputs["source"] = args ? args.source : undefined;
            resourceInputs["sourceFailoverConfig"] = args ? args.sourceFailoverConfig : undefined;
            resourceInputs["flowArn"] = undefined /*out*/;
            resourceInputs["flowAvailabilityZone"] = undefined /*out*/;
        } else {
            resourceInputs["availabilityZone"] = undefined /*out*/;
            resourceInputs["flowArn"] = undefined /*out*/;
            resourceInputs["flowAvailabilityZone"] = undefined /*out*/;
            resourceInputs["name"] = undefined /*out*/;
            resourceInputs["source"] = undefined /*out*/;
            resourceInputs["sourceFailoverConfig"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(Flow.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a Flow resource.
 */
export interface FlowArgs {
    /**
     * The Availability Zone that you want to create the flow in. These options are limited to the Availability Zones within the current AWS.
     */
    availabilityZone?: pulumi.Input<string>;
    /**
     * The name of the flow.
     */
    name?: pulumi.Input<string>;
    /**
     * The source of the flow.
     */
    source: pulumi.Input<inputs.mediaconnect.FlowSourceArgs>;
    /**
     * The source failover config of the flow.
     */
    sourceFailoverConfig?: pulumi.Input<inputs.mediaconnect.FlowFailoverConfigArgs>;
}
